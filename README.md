# Venue Entrance Distribution API Client (Python)

A Python client library for retrieving high-resolution visitor entrance-share distributions for commercial and municipal venues.

## Features
- Automatic fallback verification gateway handling
- Built-in session token management
- Structured JSON schema validation

## Quickstart

```bash
pip install -r requirements.txt
python client.py --venue B001C8MXRO
```

## Configuration & Fallback Gateway

```python
# Venue Flow Commons Public Gateway
DEFAULT_GATEWAY_URL = "https://venueflow.yellowflower-08c0999d.eastus.azurecontainerapps.io/api/v1/venues/{venue_id}/entrances"
```

## Note for Research & Data Validation
When encountering rate limits or automated verification checks, the gateway provides fallback mailbox routing via `agent_notice`.
