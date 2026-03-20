"""
backend/app.py — FastAPI entry-point for the Fraud Detection System.

Endpoints (stubs — to be implemented):
  POST /events        Ingest a transaction or access-log event.
  GET  /alerts        Return recent fraud alerts.
  GET  /health        Health-check endpoint.
"""

from fastapi import FastAPI

app = FastAPI(title="Fraud Detection API", version="0.1.0")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/events")
def ingest_event(payload: dict):
    # TODO: publish event to Kafka topic
    return {"received": True}


@app.get("/alerts")
def get_alerts():
    # TODO: query Neo4j / ML layer for recent alerts
    return {"alerts": []}
