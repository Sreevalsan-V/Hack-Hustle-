# Problem Statement

## AI-Based Internal Banking Fraud Detection System

### Background

Modern banking institutions rely on dozens of siloed monitoring tools — transaction auditing, access-control logs, and behavioural analytics — that operate in isolation. This fragmentation means that a single alert rarely paints a complete picture of a threat.

### Core Challenges

| Challenge | Impact |
|-----------|--------|
| **Fragmented monitoring** | Security teams juggle disconnected dashboards, causing critical signals to be missed or acted on too late. |
| **No correlation between fund flow and user behaviour** | Suspicious fund movements are not linked to the privileged employee who initiated or approved them, hiding insider threats in plain sight. |
| **Insider fraud risks** | Employees with elevated access can manipulate transactions, approve fictitious beneficiaries, or siphon funds gradually — actions that rule-based systems fail to flag. |
| **Delayed detection** | Batch-processing pipelines review transactions hours after they occur, giving fraudsters a wide window to cover their tracks. |

### Proposed Solution

Build a **real-time, AI-driven fraud detection platform** that:

1. **Streams** every transaction and access event through Apache Kafka for sub-second ingestion.  
2. **Correlates** fund-flow graphs with user-behaviour sequences using a Neo4j graph database to expose hidden relationships between accounts, employees, and actions.  
3. **Detects anomalies** with ML models (Isolation Forest / Graph Neural Networks) that learn normal behavioural baselines and flag deviations immediately.  
4. **Visualises** alert clusters, transaction paths, and risk scores on an interactive React + D3.js dashboard served by a FastAPI backend.

### Success Criteria

- Detection latency **< 5 seconds** from event ingestion to alert.  
- False-positive rate **< 5 %** on labelled historical data.  
- Full audit trail linking flagged transactions to responsible user accounts.
