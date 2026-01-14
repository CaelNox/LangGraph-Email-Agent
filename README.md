# AI Email Agent System

## Overview

This project implements an agentic AI system that automates email operations typically handled by an executive or operations assistant. The system processes incoming emails, determines intent and urgency, routes actions, generates responses, requests approvals when required, schedules follow ups, and escalates unresolved cases.

The focus of the project is long running, stateful agent orchestration using LangGraph, with observability and evaluation enabled through LangSmith. This is not a chatbot. It models real operational decision making over time.

---

## Key Capabilities

- Intent classification for incoming emails  
- Urgency estimation with SLA deadline assignment  
- Action routing across reply, ignore, follow up, and escalation paths  
- Automated reply drafting with human in the loop approval gating  
- Retry on rejection logic with escalation after repeated failures  
- Follow up scheduling and SLA violation detection  
- Persistent agent state and execution history  
- Full execution tracing and evaluation via LangSmith  

---

## Agent Architecture

The system is composed of multiple specialized agents, each responsible for a single operational decision.

Intent Classifier  
Classifies emails into business critical, informational, spam, or follow up required categories.

Urgency Estimator  
Determines urgency levels and computes SLA deadlines based on content and sender context.

Action Router  
Selects the next action path such as reply, ignore, follow up, or escalation.

Reply Generator  
Drafts context aware email responses using a HuggingFace hosted language model.

Approval Gate  
Implements human in the loop approval for sensitive or high risk responses.

Follow Up Monitor  
Tracks unresolved threads, schedules follow ups, and flags SLA violations.

Escalation Handler  
Escalates email threads after repeated approval rejection or SLA breaches.

---

## Workflow Design

LangGraph orchestrates the system as a deterministic, stateful workflow graph.

The graph supports conditional branching based on agent outputs, retry loops for rejected approvals, explicit terminal states, and long running state propagation across agents. This mirrors real world operational workflows rather than single turn model calls.

---

## Observability and Evaluation

LangSmith is integrated to provide:

- End to end execution traces across all agents  
- Latency analysis per decision path  
- Action distribution monitoring  
- Approval and rejection behavior analysis  
- Debugging support for agent misclassification  

The system is instrumented for future quantitative evaluation without requiring changes to agent logic.

---

## Technology Stack

Languages  
Python

Frameworks  
LangGraph  
LangChain  

Libraries  
HuggingFace  
Pydantic  
python dotenv  

Developer Tools  
LangSmith  
VS Code  
Git  

---

## Project Structure

ai email agent  
├── agents  
│   ├── intent_classifier.py  
│   ├── urgency_estimator.py  
│   ├── action_router.py  
│   ├── reply_generator.py  
│   ├── approval_gate.py  
│   ├── follow_up_monitor.py  
│   └── escalation_handler.py  
├── graph  
│   └── email_workflow.py  
├── data  
│   └── sample_emails.py  
├── schemas  
│   └── state.py  
├── .env  
└── README.md  

---

## Model Configuration

The system uses a HuggingFace hosted language model through LangChain.

Model  
deepseek ai DeepSeek V3.2

Interface  
HuggingFaceEndpoint with ChatHuggingFace

Temperature  
0.5

Authentication is handled via environment variables loaded using python dotenv.

---

## How to Run

1. Create and activate a Python virtual environment  
2. Install project dependencies  
3. Set the HUGGINGFACEHUB_API_TOKEN in a .env file  
4. Run the LangGraph workflow from the project root  
5. Inspect execution traces and evaluations in LangSmith  

---

## Why This Project

Early stage teams lose time and opportunities due to unmanaged inboxes, missed follow ups, and delayed decisions. This project demonstrates how agentic AI can replace manual operational workflows with reliable, observable, and extensible automation.

The emphasis is on system design, state management, and real decision logic rather than prompt engineering alone.

---

## Future Extensions

- Calendar and scheduling integration  
- CRM and ticketing system connectors  
- Persistent multi day state storage  
- Automated evaluation datasets for LangSmith  
- Role based approval policies  

---

## Author Name

Aditya Prakash Gupta
