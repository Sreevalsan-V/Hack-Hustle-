"""
models/anomaly_detection.py — Anomaly detection stub.

Planned models:
  - IsolationForestDetector  : tabular anomaly detection on transaction features.
  - GNNFraudDetector         : graph neural network on Neo4j-sourced transaction graphs.
"""


class IsolationForestDetector:
    """Stub for Isolation Forest-based anomaly detection."""

    def fit(self, X):
        # TODO: train sklearn IsolationForest on historical transaction data
        raise NotImplementedError

    def predict(self, X):
        # TODO: return anomaly scores for new transactions
        raise NotImplementedError


class GNNFraudDetector:
    """Stub for Graph Neural Network fraud detection using PyTorch Geometric."""

    def fit(self, graph_data):
        # TODO: train GNN on graph_data (torch_geometric.data.Data)
        raise NotImplementedError

    def predict(self, graph_data):
        # TODO: return node-level fraud probability scores
        raise NotImplementedError
