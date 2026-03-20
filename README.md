# Hack-Hustle- — AI-Based Internal Banking Fraud Detection System

An AI-driven platform for detecting internal banking fraud in real time by correlating fund flow with privileged user behaviour using graph analytics and machine learning.

---

## Repository Structure

```
fraud-detection-system/
│
├── README.md                        ← this file
├── requirements.txt                 ← Python dependencies
│
├── backend/
│   └── app.py                       ← FastAPI application entry-point
│
├── frontend/
│   └── README.md                    ← React + D3.js dashboard notes
│
├── models/
│   └── anomaly_detection.py         ← ML anomaly-detection stub
│
├── data/
│   └── sample_transactions.csv      ← Sample transaction data
│
├── diagrams/
│   └── architecture.md              ← System architecture description
│
└── docs/
    └── problem_statement.md         ← Hackathon problem statement
```

---

## System Architecture

### Components

| Layer | Technology | Role |
|-------|-----------|------|
| **Frontend** | React, D3.js | Interactive dashboard — alert explorer, transaction graph, risk-score heat-map |
| **Backend** | FastAPI (Python) | REST + WebSocket API; routes events, serves ML predictions |
| **AI / ML** | scikit-learn, PyTorch Geometric | Isolation Forest for tabular anomalies; GNN for graph-based fraud patterns |
| **Graph Database** | Neo4j | Stores account → transaction → user relationships; enables Cypher path queries |
| **Streaming** | Apache Kafka | Sub-second ingestion of transaction and access-log events |

### Data Flow

```
User / Core Banking System
        │
        │  transaction / access event
        ▼
  ┌─────────────┐
  │   Kafka     │  ← event streaming layer
  └──────┬──────┘
         │
         ▼
  ┌─────────────┐
  │  FastAPI    │  ← REST & WebSocket backend
  │  Backend    │
  └──────┬──────┘
         │
         ├──────────────────────────┐
         ▼                          ▼
  ┌─────────────┐           ┌──────────────┐
  │  AI / ML    │           │    Neo4j     │
  │  Layer      │◄─────────►│  Graph DB    │
  │ (anomaly    │           │ (fund-flow & │
  │  detection) │           │  user graph) │
  └──────┬──────┘           └──────────────┘
         │
         │  alert + risk score
         ▼
  ┌─────────────────────────┐
  │  React + D3.js          │
  │  Dashboard              │
  │  (alerts, graph view,   │
  │   heat-maps)            │
  └─────────────────────────┘
```

---

## Quick Start

```bash
# 1. Install Python dependencies
pip install -r fraud-detection-system/requirements.txt

# 2. Start the FastAPI backend
uvicorn fraud-detection-system.backend.app:app --reload

# 3. (Frontend) — see fraud-detection-system/frontend/README.md
```

---

## Problem Statement

See [`fraud-detection-system/docs/problem_statement.md`](fraud-detection-system/docs/problem_statement.md) for the full hackathon problem statement.
