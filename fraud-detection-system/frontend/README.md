# Frontend — React + D3.js Dashboard

This directory will contain the React application for the fraud-detection dashboard.

## Planned Features

- **Alert Explorer** — sortable, filterable table of fraud alerts with risk scores.
- **Transaction Graph** — D3.js force-directed graph showing account → transaction → user relationships pulled from Neo4j.
- **Risk Heat-map** — D3.js calendar heat-map of anomaly scores over time.
- **Real-time Updates** — WebSocket connection to the FastAPI backend for live alert streaming.

## Getting Started (once implemented)

```bash
cd fraud-detection-system/frontend
npm install
npm start
```
