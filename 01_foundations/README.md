# LangChain Foundations & Execution Patterns

## Overview
This directory contains **foundational LangChain execution patterns and primitives**
that demonstrate how LLM workflows are composed, executed, and orchestrated at a
low level using LangChain’s core abstractions.

These examples focus on **how LangChain works internally**, not on end-user
applications. They serve as building blocks for more advanced systems such as
RAG pipelines, agent frameworks, and LangGraph workflows.

---

## What This Section Covers
The projects in this folder demonstrate:

- Sequential vs parallel execution of LLM calls
- Runnable interfaces and data flow control
- Prompt templating and message construction
- Explicit conversational state handling
- Graph-based execution semantics in LangChain

This section intentionally avoids deployment or UI concerns and focuses purely on
**execution semantics and composition patterns**.

---

## Included Projects

### 1. Parallel Chain Patterns
**Folder:** `parallel_chain_patterns/`

**Concept Demonstrated:**
- Concurrent execution of independent LLM tasks using `RunnableParallel`

**Key Ideas:**
- Task decomposition
- Parallel LLM calls
- Merging multiple outputs into a downstream generation step

**Why It Matters:**
Parallel execution reduces latency and enables structured multi-output workflows
commonly used in document processing and analysis systems.

---

### 2. Sequential Chain Patterns
**Folder:** `sequential_chain_patterns/`

**Concept Demonstrated:**
- Linear, dependent LLM pipelines

**Key Ideas:**
- Output of one LLM step feeding directly into the next
- Deterministic, ordered reasoning flow

**Why It Matters:**
Sequential chains are ideal when tasks must be performed in a strict order, such as
generation → refinement → summarization pipelines.

---

### 3. Runnable Interfaces
**Folder:** `lc_runnable_interfaces/`

**Concept Demonstrated:**
- Core runnable abstractions and data routing mechanisms in LangChain

**Key Ideas:**
- `RunnablePassthrough`
- `RunnableParallel`
- Explicit control over input and output propagation

**Why It Matters:**
Runnable interfaces form the foundation for building reusable, composable,
and debuggable LLM systems. They are heavily leveraged in agent frameworks
and graph-based orchestration layers.

---

### 4. Prompt Engineering Basics
**Folder:** `prompt_engineering_basics/`

**Concept Demonstrated:**
- Structured and parameterized prompt construction

**Key Ideas:**
- System vs human message roles
- Prompt parameterization
- Domain-specific instruction injection

**Why It Matters:**
Prompt templates provide consistency, clarity, and reuse when designing LLM
interactions, especially in production-oriented systems.

---

### 5. Message Role–Based Chat (LLM Basics)
**Folder:** `message_role_based_chat/`

**Concept Demonstrated:**
- Explicit conversational state management using message roles

**Key Ideas:**
- Manual chat history maintenance
- Use of `SystemMessage`, `HumanMessage`, and `AIMessage`
- Stateless LLM with externally managed memory

**Why It Matters:**
Understanding how conversational context is constructed and preserved is a
prerequisite for introducing higher-level abstractions such as memory modules,
agents, retrieval-augmented generation, and graph-based workflows.

---

## Design Philosophy
- Minimal code, maximum conceptual clarity
- Focus on execution semantics, not applications
- Each example demonstrates **one core concept well**

These patterns are intentionally small so they can be reused as primitives
inside larger systems such as:
- Retrieval-Augmented Generation (RAG)
- Multi-agent workflows
- LangGraph-based state machines

---

## How This Fits Into the Larger Repository
This folder represents the **foundation layer** of the repository.

Higher-level directories build on these concepts to create:
- RAG systems
- Tool-using agents
- Multi-agent coordination graphs
- End-to-end LLM applications

---

## Intended Audience
- ML engineers learning LangChain internals
- Developers transitioning from scripts to structured LLM systems
- Engineers preparing for production-grade LLM orchestration