# Agent Systems & Tool-Oriented Workflows

## Overview
This directory contains **agent-based LLM systems** that demonstrate how large
language models can **reason, plan, make decisions, and invoke tools** to achieve
user-defined goals.

Unlike simple chains or RAG pipelines, these projects emphasize:
- Decision-making
- Conditional logic
- Tool usage
- Iterative refinement
- State-driven orchestration

Together, they represent progressively more advanced **agent architectures**
ranging from single-tool agents to multi-step LangGraph workflows.

---

## What This Section Covers
The projects in this folder demonstrate:

- Tool definition and invocation
- LLM-driven reasoning and planning
- Structured outputs for control flow
- Conditional branching and loops
- Agent orchestration using LangGraph
- Practical, real-world agent use cases

These examples focus on **agent intelligence and control**, not UI or deployment.

---

## Included Projects

### 1. API Tool Agent (Currency Conversion)
**Folder:** `api_tool_agent/`

**Concept Demonstrated:**
- Tool-using agent that integrates with an external API

**Key Ideas:**
- Custom tools defined via `@tool`
- External API invocation (currency exchange rates)
- Multi-step reasoning enforced via system prompt
- Clear separation between data fetching and computation

**Why It Matters:**
This mirrors real-world agent scenarios where LLMs must:
- Call APIs
- Chain tool outputs
- Explain results transparently to users

**Typical Use Cases:**
- Finance assistants
- API-driven automation agents
- Decision-support bots

---

### 2. Automated Reply Agent (Review Response System)
**Folder:** `automated_reply_agent/`

**Concept Demonstrated:**
- Conditional agent workflows using LangGraph

**Key Ideas:**
- Sentiment classification via structured outputs
- Issue diagnosis and urgency detection
- Conditional branching based on sentiment
- Separate response strategies for positive vs negative reviews

**Why It Matters:**
This project demonstrates **enterprise-grade agent logic**, where responses
must adapt based on structured understanding of user input rather than
free-form text generation.

**Typical Use Cases:**
- Customer support automation
- Review moderation systems
- CRM and feedback pipelines

---

### 3. Content Generation Agent (Iterative Tweet Optimization)
**Folder:** `content_generation_agent/`

**Concept Demonstrated:**
- Iterative generation–evaluation–optimization loop

**Key Ideas:**
- Creative content generation
- Structured evaluation with explicit approval criteria
- Feedback-driven refinement
- Looping until quality threshold or max iterations

**Why It Matters:**
This showcases how agents can **self-critique and improve outputs**, a core
pattern behind autonomous creative agents and production content pipelines.

**Typical Use Cases:**
- Social media content generation
- Marketing copy optimization
- Creative writing assistants

---

### 4. Task Planning Agent
**Folder:** `task_planning_agent/`

**Concept Demonstrated:**
- Goal decomposition and planning via tool-aware agents

**Key Ideas:**
- High-level goal → actionable task breakdown
- Deadline estimation using tool-based date retrieval
- Priority assignment
- Structured, human-readable output

**Why It Matters:**
Planning agents are a cornerstone of autonomous systems, enabling LLMs to
convert vague goals into executable plans.

**Typical Use Cases:**
- Personal productivity assistants
- Project planning tools
- Travel and itinerary planners

---

### 5. Tool-Using Agent (Custom Calculator Tool)
**Folder:** `tool_using_agent/`

**Concept Demonstrated:**
- Custom tool creation using `BaseTool`

**Key Ideas:**
- Strongly typed tool inputs via Pydantic
- Explicit tool schema definitions
- Deterministic tool execution
- LLM-mediated tool selection

**Why It Matters:**
This demonstrates how agents can safely delegate deterministic operations
(e.g., math, validation, business logic) to tools instead of hallucinating.

**Typical Use Cases:**
- Calculation assistants
- Rule-based decision systems
- Hybrid AI + deterministic logic pipelines

---

## Design Philosophy
- Explicit control over agent behavior
- Structured outputs over free-form reasoning
- Clear separation of reasoning, tools, and execution
- Incremental complexity across examples

Each project highlights a **core agent pattern**:
- Tool invocation
- Conditional routing
- Iterative refinement
- Planning and decomposition

---

## How This Fits Into the Larger Repository
This folder represents the **agent intelligence layer** of the repository.

It builds on:
- Prompt engineering
- Runnable abstractions
- RAG-based knowledge grounding

And enables:
- Autonomous assistants
- Multi-agent systems
- Enterprise automation workflows
- Decision-making AI systems

---

## Intended Audience
- ML engineers building agentic systems
- Developers exploring LangChain agents and LangGraph
- Engineers preparing for production LLM workflows
- Practitioners designing tool-augmented AI systems