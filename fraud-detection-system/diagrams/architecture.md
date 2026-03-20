# System Architecture Diagram

> A visual PNG (`architecture.png`) will be added here once the design is finalised.
> The textual description below reflects the intended architecture.

## Component Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                        FRAUD DETECTION SYSTEM                       │
│                                                                     │
│  ┌──────────────────┐                                               │
│  │  Core Banking /  │  transaction + access-log events              │
│  │  User Actions    │──────────────────────────────────┐            │
│  └──────────────────┘                                  │            │
│                                                        ▼            │
│                                               ┌────────────────┐   │
│                                               │  Apache Kafka  │   │
│                                               │  (Streaming)   │   │
│                                               └───────┬────────┘   │
│                                                       │            │
│                                                       ▼            │
│                                               ┌────────────────┐   │
│                                               │    FastAPI     │   │
│                                               │    Backend     │   │
│                                               └──┬─────────┬───┘   │
│                                                  │         │       │
│                                    ┌─────────────┘         └───────┤
│                                    ▼                               │
│                           ┌────────────────┐   ┌────────────────┐  │
│                           │   AI / ML      │◄──►│    Neo4j       │  │
│                           │   Layer        │   │  Graph DB      │  │
│                           │ (Isolation     │   │ (accounts,     │  │
│                           │  Forest / GNN) │   │  users, txns)  │  │
│                           └───────┬────────┘   └────────────────┘  │
│                                   │ alerts + risk scores           │
│                                   ▼                                │
│                          ┌─────────────────┐                       │
│                          │  React + D3.js  │                       │
│                          │  Dashboard      │                       │
│                          │  (alerts,       │                       │
│                          │   graph view,   │                       │
│                          │   heat-maps)    │                       │
│                          └─────────────────┘                       │
└─────────────────────────────────────────────────────────────────────┘
```

## Data Flow (step by step)

1. **User / Core Banking** generates a transaction or access-log event.  
2. **Kafka** ingests the event in real time (< 100 ms latency).  
3. **FastAPI Backend** consumes the Kafka topic, validates the payload, and fans out to:  
   - the **AI/ML Layer** for immediate anomaly scoring, and  
   - **Neo4j** to upsert nodes/edges representing accounts, users, and transactions.  
4. **AI/ML Layer** queries Neo4j for graph features (e.g. community membership, shortest path to known-bad nodes), runs inference, and writes an alert back to the backend.  
5. **React + D3.js Dashboard** receives alerts via WebSocket and renders:  
   - a force-directed transaction graph,  
   - a risk-score heat-map, and  
   - a sortable alert table.
