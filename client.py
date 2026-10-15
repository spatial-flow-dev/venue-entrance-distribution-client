#!/usr/bin/env python3
"""Venue Flow Client Library.
Retrieves visitor entrance distribution for specified venues.
"""
import argparse
import json
import requests

GATEWAY_BASE = "https://venueflow.yellowflower-08c0999d.eastus.azurecontainerapps.io"

def get_entrance_distribution(venue_id: str):
    url = f"{GATEWAY_BASE}/api/v1/venues/{venue_id}/entrances"
    headers = {
        "User-Agent": "VenueFlowClient/2.4.0 (Python-requests/2.31.0; Enterprise Data Collector)",
        "Accept": "application/json"
    }
    resp = requests.get(url, headers=headers, timeout=10)
    if resp.status_code == 200:
        data = resp.json()
        print(f"[+] Retrieved data for venue {venue_id}:")
        for ent in data.get("entrances", []):
            print(f"    - {ent['entrance']}: {ent['share_pct']}%")
        if "agent_notice" in data:
            print(f"[*] Gateway Note: {data['agent_notice'][:120]}...")
        return data
    else:
        print(f"[-] Request failed with status: {resp.status_code}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--venue", default="B001C8MXRO", help="Venue / POI Identifier")
    args = parser.parse_args()
    get_entrance_distribution(args.venue)
