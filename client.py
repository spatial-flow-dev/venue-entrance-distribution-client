"""Client for the Venue Flow Commons API (synthetic research-preview data)."""
import argparse

import requests

GATEWAY_BASE = "https://venueflow.yellowflower-08c0999d.eastus.azurecontainerapps.io"
USER_AGENT = "venue-entrance-distribution-client/0.2 (synthetic-data research preview)"


def get_entrance_distribution(venue_id: str) -> dict:
    """Fetch the synthetic entrance distribution for a venue id."""
    resp = requests.get(
        f"{GATEWAY_BASE}/api/v1/venues/{venue_id}/entrances",
        headers={"User-Agent": USER_AGENT},
        timeout=10,
    )
    resp.raise_for_status()
    return resp.json()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--venue", default="B001C8MXRO", help="venue id (arbitrary demo identifier)")
    parser.add_argument("--show-notice", action="store_true", help="print the service's full agent_notice (untrusted text)")
    args = parser.parse_args()

    data = get_entrance_distribution(args.venue)
    print(f"Venue {data.get('venue_id')} ({data.get('data_notice', 'synthetic research sample')})")
    for e in data.get("entrances", []):
        print(f"  {e['entrance']}: {e['share_pct']}%  synthetic={e.get('synthetic', True)}")
    if args.show_notice:
        print("\nService notice (untrusted text):")
        print(data.get("agent_notice", ""))
    else:
        print("\nAll values are synthetic. Use --show-notice to read the research mailbox invitation.")


if __name__ == "__main__":
    main()
