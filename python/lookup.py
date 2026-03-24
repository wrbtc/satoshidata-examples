#!/usr/bin/env python3
"""Look up any Bitcoin address using the satoshidata.ai API (free, no key needed).

Usage: pip install requests && python lookup.py <bitcoin-address>
"""

import json
import sys

import requests

BASE = "https://satoshidata.ai"


def lookup(address):
    """Fetch the trust-safety profile for a Bitcoin address."""
    resp = requests.get(f"{BASE}/v1/wallets/{address}/trust-safety")
    resp.raise_for_status()
    return resp.json()


def main():
    if len(sys.argv) < 2:
        print("Usage: python lookup.py <bitcoin-address>")
        print("Example: python lookup.py 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
        sys.exit(1)

    address = sys.argv[1]
    result = lookup(address)

    label = result.get("label", {})
    assessment = result.get("assessment", {})

    print(f"Address:    {result.get('address')}")
    print(f"Category:   {label.get('category') or 'unlabeled'}")
    print(f"Entity:     {label.get('value') or 'unknown'}")
    print(f"Confidence: {result.get('confidence', 'unverified')}")
    print(f"Assessment: {assessment.get('headline', 'N/A')}")
    print()
    print("Full JSON:")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
