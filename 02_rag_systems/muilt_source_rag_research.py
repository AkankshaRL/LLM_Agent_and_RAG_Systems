from langgraph.graph import StateGraph, END, START
from typing import TypedDict, List, Dict
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from transformers import pipeline
from dotenv import load_dotenv

load_dotenv()

class ResearchState(TypedDict):
    query: str
    docs: List[str]
    sentiment: Dict[str, int]
    fact_check: List[Dict]
    summary: str

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
sentiment_pipeline = pipeline("sentiment-analysis")  

def retriever_node(state: ResearchState):
    
    prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a research assistant. Provide 3 factual background points on the query."),
    ("human", "{query}")
])
    chain = prompt | llm
    response = chain.invoke({"query": state["query"]}).content
    return {"docs": response.split("\n")}

def sentiment_node(state: ResearchState):
    
    sentiment_counts = {"POSITIVE": 0, "NEGATIVE": 0, "NEUTRAL": 0}
    for doc in state["docs"]:
        result = sentiment_pipeline(doc)[0]["label"]
        if result in sentiment_counts:
            sentiment_counts[result] += 1
        else:
            sentiment_counts["NEUTRAL"] += 1

    return {"sentiment": sentiment_counts}

def fact_check_node(state: ResearchState):
    fact_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a fact-checking assistant. Extract claims from the text and assign confidence (0 to 1)."),
    ("human", "Text:\n{docs}")
])
    docs_text = "\n".join(state["docs"])
    chain = fact_prompt | llm
    result = chain.invoke({"docs": docs_text}).content
    
    return {"fact_check": result}

def merge_node(state: ResearchState) -> ResearchState:

    docs_text = "\n".join(state["docs"])
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a research assistant that summarizes documents."),
        ("human", "Summarize the following docs:\n{docs}")
    ])
    chain = prompt | llm
    summary = chain.invoke({"docs": docs_text}).content
    state["summary"] = summary
    return state

def output_node(state: ResearchState) -> ResearchState:

    print("\n=== Research Report ===")
    print("Query:", state["query"])
    print("\nSummary:", state["summary"])
    print("\nSentiment:", state["sentiment"])
    print("\nFact-Check:", state["fact_check"])
    print("\n=======================")
    return state

graph = StateGraph(ResearchState)

graph.add_node("Retriever", retriever_node)
graph.add_node("Sentiment", sentiment_node)
graph.add_node("FactCheck", fact_check_node)
graph.add_node("Merge", merge_node)
graph.add_node("Output", output_node)

graph.add_edge(START, "Retriever")
graph.add_edge("Retriever", "Sentiment")
graph.add_edge("Retriever", "FactCheck")

graph.add_edge("Sentiment", "Merge")
graph.add_edge("FactCheck", "Merge")

graph.add_edge("Merge", "Output")
graph.add_edge("Output", END)

app = graph.compile()

initial_state = {
    "query": "Impact of AI on jobs"
    }
app.invoke(initial_state)