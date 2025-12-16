
Each folder represents a **layer of abstraction** in building agentic AI systems.

---

## 01. Foundations — Core LLM & LangChain Primitives
**Folder:** `01_foundation/`

This section focuses on the **atomic building blocks** of LLM applications.

### What’s Covered
- Prompt templates
- Runnable interfaces
- Sequential and parallel chains
- Tool invocation fundamentals
- Basic chatbots and utilities
- Input / output schemas

### Key Concepts
- Deterministic prompt design
- Structured message passing
- Chaining vs routing
- Runnable composition
- Tool calling mechanics

### Why This Matters
Strong agent systems fail if the fundamentals are weak.  
This section ensures **clarity, predictability, and correctness** before introducing complexity.

---

## 02. Retrieval-Augmented Generation (RAG) Systems
**Folder:** `02_rag_systems/`

This layer introduces **knowledge grounding**, a requirement for nearly all real-world LLM applications.

### What’s Covered
- Document loaders (web, YouTube, file-based)
- Chunking strategies
- Embedding model selection
- Vector retrieval pipelines
- RAG-powered chatbots

### Key Concepts
- Why retrieval beats prompting alone
- Chunk size vs recall trade-offs
- Embedding model selection rationale
- Retrieval failure modes

### Why This Matters
This section shows how LLMs move from:
> *“generative text models”*  
to  
> *“knowledge-aware systems”*

Every serious production LLM system uses RAG.

---

## 03. Agent Systems — Tool Use, Planning & Reasoning
**Folder:** `03_agent_systems/`

This section introduces **true agentic behavior**.

### What’s Covered
- Tool-using agents
- API-based agents
- Task planning agents
- Content generation agents
- Automated reply systems
- Multi-step decision agents

### Key Concepts
- Tool grounding vs hallucination
- Explicit planning and delegation
- Role-based agent prompts
- Structured outputs for reliability

### Why This Matters
This is where LLMs stop being **text generators** and start becoming **decision-making systems**.

---

## 04. LangGraph Workflows — Control, State & Orchestration
**Folder:** `04_workflows_langgraph/`

This layer introduces **explicit execution graphs**, enabling reliable and inspectable agent behavior.

### What’s Covered
- Sequential and parallel workflows
- Conditional branching
- State propagation
- Evaluation and feedback loops
- Iterative refinement graphs
- Mathematical and reasoning workflows

### Key Concepts
- Deterministic control flow
- State-driven execution
- Graph-based reasoning
- Multi-node evaluation strategies

### Why This Matters
LangGraph enables:
- Debuggable AI systems
- Human intervention points
- Reliable retries and evaluations

This is essential for **production-grade agents**.

---

## 05. End-to-End Applications & Agent Communication
**Folder:** `05_end_to_end_apps/`

This is the **systems integration layer**, where everything comes together.

### What’s Coveredj
- Agent–Client Protocol (ACP)
- Agent-to-Agent (A2A) communication
- Streaming agent responses
- Human-in-the-loop APIs
- Supervisor–worker multi-agent systems
- FastAPI-powered agent services

### Key Concepts
- Protocol-driven communication
- Streaming execution
- Human approval workflows
- Multi-agent coordination
- Separation of concerns at system level

### Why This Matters
This section mirrors **how agent systems are actually deployed**:
- Backend services
- Frontend consumers
- API-based interaction
- Human + AI collaboration

---

## Design Philosophy

This repository follows a few strict principles:

- **Explicit is better than implicit**
- **Graphs over magic**
- **Protocols over monoliths**
- **Humans stay in the loop**
- **Agents have clear roles**

Every project favors **clarity and reliability** over clever shortcuts.

---

## Tech Stack
- Python
- LangChain
- LangGraph
- FastAPI
- Google Gemini (via `langchain-google-genai`)
- Pydantic
- AsyncIO
- Vector databases (local / pluggable)

All tools and patterns used here are:
- Open-source
- Industry-relevant
- Production-aligned

---

## Who This Repo Is For
- ML Engineers building agentic systems
- Backend Engineers integrating LLM APIs
- Data Scientists moving into LLM engineering
- Anyone preparing for **Agentic AI / Applied LLM roles**

---

## How to Use This Repository
- Browse folders in order (recommended)
- Each folder contains its own focused README
- Treat this repo as a **reference implementation**
- Clone and adapt patterns, not just code

---

### Setup
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
---

## Final Note
This repository is not about showing *what LLMs can do*.

It is about showing **how to design, control, and ship AI systems that don’t break in production**.