# LangGraph Core Workflows & Reasoning Patterns

## Overview
This directory contains **core LangGraph workflows** that demonstrate how
stateful, graph-based execution can be used to orchestrate LLM calls,
deterministic computations, and conditional reasoning.

These projects focus on **how control flows through a graph**, how state is
mutated across nodes, and how LangGraph enables:
- Parallel execution
- Conditional branching
- Structured evaluation
- Deterministic + LLM hybrid workflows

They intentionally avoid UI, deployment, or full agent abstractions.

---

## What This Section Covers
The projects in this folder demonstrate:

- StateGraph construction and compilation
- Explicit state typing with `TypedDict`
- Sequential and parallel node execution
- Conditional routing based on computed state
- Hybrid graphs (LLM + deterministic logic)
- Evaluation and scoring pipelines

These workflows form the **execution backbone** for agents, evaluators,
and production-grade orchestration systems.

---

## Included Projects

### 1. Chained Prompt Graph (Blog Generation & Evaluation)
**Folder:** `chained_prompt_graph/`

**Concept Demonstrated:**
- Sequential LLM orchestration using LangGraph

**Workflow:**
1. Generate blog outline from title
2. Generate blog content from outline
3. Evaluate content quality against outline

**Key Ideas:**
- State accumulation across nodes
- Multi-step prompt chaining
- Evaluation as a first-class graph node
- Clear separation of generation and validation

**Why It Matters:**
This pattern mirrors real-world content pipelines where generation is followed
by automated quality checks before approval or publishing.

**Typical Use Cases:**
- Content generation systems
- Editorial review pipelines
- Automated documentation workflows

---

### 2. Decision Workflow Graph (Parallel Metrics + Aggregation)
**Folder:** `decision_workflow_graph/`

**Concept Demonstrated:**
- Parallel computation with state merging

**Workflow:**
- Strike rate calculation
- Boundary-per-ball calculation
- Boundary percentage calculation
- Unified summary generation

**Key Ideas:**
- Fan-out from `START` into parallel nodes
- Independent deterministic computations
- State aggregation before final output
- No LLM dependency

**Why It Matters:**
This shows that LangGraph is not just for LLMs — it can orchestrate
purely deterministic logic with the same execution semantics.

**Typical Use Cases:**
- Analytics pipelines
- KPI computation systems
- Business rule orchestration

---

### 3. Essay Evaluation Workflow (Multi-Criteria LLM Scoring)
**Folder:** `essay_workflow_graph/`

**Concept Demonstrated:**
- Parallel LLM-based evaluation with structured outputs

**Workflow:**
- Language quality evaluation
- Depth of analysis evaluation
- Clarity of thought evaluation
- Final aggregated feedback + average score

**Key Ideas:**
- Structured LLM outputs via Pydantic models
- Parallel evaluation paths
- Score accumulation using reducers
- Final synthesis node

**Why It Matters:**
This is a canonical **LLM evaluation graph**, suitable for grading,
review systems, and quality assurance pipelines.

**Typical Use Cases:**
- Automated essay grading
- LLM output evaluation
- Educational technology platforms

---

### 4. Quadratic Equation Reasoning Graph
**Folder:** `quadratic_eq_reasoning_graph/`

**Concept Demonstrated:**
- Conditional branching based on computed state

**Workflow:**
1. Display equation
2. Compute discriminant
3. Route execution based on discriminant value
   - Real roots
   - Repeated roots
   - No real roots

**Key Ideas:**
- Conditional edges via `add_conditional_edges`
- Deterministic reasoning paths
- Mathematical logic expressed as a graph

**Why It Matters:**
This demonstrates **symbolic reasoning and decision trees** implemented
using LangGraph’s routing primitives.

**Typical Use Cases:**
- Rule-based reasoning engines
- Math solvers
- Decision-support systems

---

### 5. Simple LLM Graph (Single-Node QA)
**Folder:** `simple_llm_graph/`

**Concept Demonstrated:**
- Minimal LangGraph setup for LLM invocation

**Workflow:**
- Single LLM question–answer node

**Key Ideas:**
- Graph as an execution wrapper around an LLM call
- Explicit state definition
- Clean START → END flow

**Why It Matters:**
This is the **simplest possible LangGraph**, useful for understanding
graph semantics before introducing branching or parallelism.

**Typical Use Cases:**
- Learning LangGraph basics
- Prototyping graph-based execution
- Replacing ad-hoc LLM calls with structured workflows

---

## Design Philosophy
- Explicit state over hidden memory
- Graph-based control instead of linear scripts
- Deterministic + LLM hybrid execution
- One core concept per workflow

Each project is intentionally small, readable, and reusable as a
building block for larger systems.

---

## How This Fits Into the Larger Repository
This folder represents the **execution and reasoning layer** of the repository.

It sits:
- Above LangChain foundations (runnables, prompts)
- Below agents and multi-agent systems

These patterns are reused in:
- Agent decision graphs
- Evaluation pipelines
- RAG orchestration
- Human-in-the-loop systems

---

## Intended Audience
- ML engineers learning LangGraph internals
- Developers building structured LLM workflows
- Engineers designing deterministic + AI hybrids
- Practitioners moving beyond linear chains