# Agent Communication, Coordination & Control Patterns

## Overview
This directory demonstrates **advanced agent communication and orchestration patterns**
beyond simple chains and graphs.

The projects here focus on **how agents talk to each other, how humans interact with
running workflows, and how execution is coordinated across protocols, roles, and systems**.

Rather than focusing on task correctness, these examples emphasize:
- Communication protocols
- Streaming execution
- Human-in-the-loop control
- Multi-agent supervision
- Separation of concerns between agents

---

## What This Section Covers
The projects in this folder demonstrate:

- Agent–Client Protocols (ACP)
- Agent-to-Agent (A2A) communication
- Streaming agent responses
- Human-in-the-loop graph interruptions
- Supervisor–worker multi-agent architectures
- Tool-constrained agents with strict role boundaries

These patterns are commonly used in **production-grade agent systems**, not demos.

---

## Included Projects

---

### 1. ACP (Agent–Client Protocol) — Client & Server
**Folder:** `ACP/`

**Concept Demonstrated:**
- Streaming communication between a client and an agent server using ACP

#### Components
- `client.py`: Asynchronous ACP client
- `server.py`: ACP agent server with coordinated multi-agent execution

#### Workflow
1. Client sends a natural-language request
2. Server streams intermediate reasoning and progress events
3. Multiple agents (flight, hotel, weather) are coordinated
4. Final structured plan is streamed back to the client

#### Key Ideas:
- Event-based streaming (`MessagePartEvent`, `MessageCompletedEvent`)
- Decoupled client/server execution
- Protocol-driven agent invocation
- Agent coordination behind a single endpoint

#### Why It Matters:
This mirrors **real production deployments**, where:
- Frontends consume streamed agent outputs
- Backends orchestrate multiple specialized agents
- Clients never directly control agent internals

**Typical Use Cases:**
- Agent-backed APIs
- Chat-based assistants with live updates
- LLM microservices

---

### 2. A2A (Agent-to-Agent) Protocol Simulation
**Folder:** `A2A/`

**Concept Demonstrated:**
- Direct agent-to-agent communication using protocol-style messages

#### Workflow
1. Agents publish **agent cards** for discovery
2. Client agent selects agents based on capabilities
3. Communication occurs via JSON-RPC–style messages
4. Responses are aggregated into a final plan

#### Key Ideas:
- Agent discovery via capability metadata
- Explicit sender/receiver roles
- Protocol-based task delegation
- No centralized graph — coordination emerges from messages

#### Why It Matters:
A2A patterns are foundational for:
- Distributed agent systems
- Federated AI services
- Marketplace-style agent ecosystems

This example cleanly separates:
- **Who can do what**
- **Who talks to whom**
- **How tasks are routed**

---

### 3. Human-in-the-Loop LangGraph Workflow
**Folder:** `human_in_loop_graph/`

**Concept Demonstrated:**
- Pausing and resuming graph execution based on human input

#### Workflow
1. Graph execution begins automatically
2. Execution halts at an `interrupt`
3. User input is collected via FastAPI
4. Graph resumes from the interruption point
5. Final state is returned once complete

#### Key Ideas:
- `interrupt()` as a first-class control primitive
- Stateful resumption using thread IDs
- External API-driven continuation
- Explicit checkpointing (in-memory for demo)

#### Why It Matters:
Human-in-the-loop control is essential for:
- Approval workflows
- Risk-sensitive decisions
- Interactive agents
- Regulated environments

This pattern enables **AI + human collaboration**, not full automation.

---

### 4. Multi-Agent Supervisor Architecture
**Folder:** `multi_agent/`

**Concept Demonstrated:**
- Supervisor–worker agent orchestration

#### Architecture
- **Supervisor Agent**
  - Classifies the task
  - Routes work
  - Coordinates responses
- **Research Agent**
  - Retrieves factual data only
- **Math Agent**
  - Performs numeric computation only

#### Key Ideas:
- Strict role isolation
- Tool-constrained agents
- No agent solves the entire task alone
- Supervisor never performs work itself

#### Why It Matters:
This is a **production-grade multi-agent pattern** that:
- Prevents hallucination
- Improves reliability
- Scales better than monolithic agents

Used heavily in:
- Enterprise copilots
- Decision-support systems
- Analytical assistants

---

## Design Philosophy
- Communication over monoliths
- Explicit protocols instead of implicit behavior
- Clear separation of agent responsibilities
- Streaming and interruption as first-class concepts

These examples intentionally trade simplicity for **architectural realism**.

---

## How This Fits Into the Larger Repository
This folder represents the **coordination and control layer**.

It builds on:
- LangChain foundations
- LangGraph execution semantics

And enables:
- Distributed agents
- Human-supervised systems
- Protocol-driven AI services
- Multi-agent collaboration at scale

---

## Intended Audience
- ML engineers building agent platforms
- Backend engineers integrating LLM services
- Developers designing AI protocols
- Teams moving from single-agent to multi-agent systems