from typing import TypedDict, Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# LangGraph imports
from langgraph.types import interrupt, Command
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver ########### Cant use this for prod


# -------------------------
# STATE
# -------------------------
class LemonadeState(TypedDict):
    lemonade_type: Optional[str]
    lemons: Optional[int]
    water: Optional[str]
    refill: Optional[int]


# -------------------------
# NODES
# -------------------------
def add_lemons(state: LemonadeState):
    print("*****In Add Lemons node*****")
    return {**state, "lemons": 2}


def set_lemonade_type(state: LemonadeState):
    print("*****In Lemonade Type node*****")
    choice = interrupt("What type of lemonade would you like? (sweet or salty)")

    if choice in ["sweet", "salty"]:
        return {**state, "lemonade_type": choice}

    return {**state, "lemonade_type": "no correct choice given"}


def add_water(state: LemonadeState):
    print("*****In Add Water node*****")
    return {**state, "water": "200ml"}


def refill_cup(state: LemonadeState):
    print("*****In Refill Cup node*****")
    refill_count = state.get("refill", 0) + 1
    return {**state, "refill": refill_count}


# -------------------------
# WORKFLOW GRAPH
# -------------------------
workflow = StateGraph(LemonadeState)

workflow.add_node("set_lemonade_type", set_lemonade_type)
workflow.add_node("add_lemons", add_lemons)
workflow.add_node("add_water", add_water)
workflow.add_node("refill_cup", refill_cup)

workflow.add_edge(START, "add_lemons")
workflow.add_edge("add_lemons", "set_lemonade_type")
workflow.add_edge("set_lemonade_type", "add_water")
workflow.add_edge("add_water", "refill_cup")
workflow.add_edge("refill_cup", END)

checkpointer = InMemorySaver()
workflow_graph = workflow.compile(checkpointer=checkpointer)


# -------------------------
# FASTAPI SETUP
# -------------------------
app = FastAPI(
    title="Lemonade Factory example API",
    version="1.0.0",
    description="LangGraph powered Lemonade Factory example",
)

# Allow all CORS (optional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------
# USER INPUT MODEL
# -------------------------
class UserInput(BaseModel):
    order_id: str
    message: str = ""
    thread_id: str


# -------------------------
# INTERRUPT MANAGEMENT
# -------------------------
pending_interrupts = {}


# -------------------------
# API ENDPOINT
# -------------------------
@app.post("/lemonade/")
def process_lemonade_order(user_input: UserInput):

    input_state = {}  # empty because nodes do not use user input initially

    # ---------------------------
    # 1. HANDLE INTERRUPT RESUME
    # ---------------------------
    if pending_interrupts.get(user_input.order_id, {}).get("awaiting_input"):

        result = workflow_graph.invoke(
            Command(resume=user_input.message.strip()),
            config={"configurable": {"thread_id": user_input.thread_id}},
        )

        pending_interrupts[user_input.order_id]["awaiting_input"] = False

    # ---------------------------
    # 2. NORMAL FLOW (NO INTERRUPT)
    # ---------------------------
    else:
        pending_interrupts.pop(user_input.order_id, None)

        result = workflow_graph.invoke(
            input_state,
            config={"configurable": {"thread_id": user_input.thread_id}},
        )

    # ---------------------------
    # 3. CHECK IF INTERRUPT WAS TRIGGERED
    # ---------------------------
    if "__interrupt__" in result:
        pending_interrupts[user_input.order_id] = {"awaiting_input": True}

        return {
            "order_id": user_input.order_id,
            "response": result["__interrupt__"][0].value,  # question to user
            "thread_id": user_input.thread_id,
        }

    # ---------------------------
    # 4. FINAL OUTPUT
    # ---------------------------
    return {
        "order_id": user_input.order_id,
        "response": result,
        "thread_id": user_input.thread_id,
    }
