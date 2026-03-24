#!/usr/bin/env python3
"""Check multiple Bitcoin addresses using satoshidata.ai (free trust-safety endpoint).

Usage: pip install requests && python batch_check.py [address1 address2 ...]
If no addresses given, uses built-in examples.
"""

import sys

import requests

BASE = "https://satoshidata.ai"

EXAMPLE_ADDRESSES = [
    "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
    "bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h",
    "bc1qazcm763858nkj2dz7g0ntv4536vma4ck7l7l4a",
    "1N52wHoVR79PMDishab2XmRHsbekCdGquK",
    "3M219KR5vEneNb47ewrPfWyb5jQ2DjxRP6",
]


def check_address(address):
    """Fetch trust-safety for one address."""
    try:
        resp = requests.get(f"{BASE}/v1/wallets/{address}/trust-safety")
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"address": address, "error": str(e)}


def main():
    addresses = sys.argv[1:] if len(sys.argv) > 1 else EXAMPLE_ADDRESSES

    print(f"Checking {len(addresses)} addresses...\n")
    print(f"{'Address':<20} {'Category':<15} {'Entity':<20} {'Confidence'}")
    print("-" * 75)

    for addr in addresses:
        result = check_address(addr)
        if "error" in result:
            print(f"{addr[:18]+'..':.<20} ERROR: {result['error']}")
            continue
        label = result.get("label", {})
        short = addr[:16] + "..." if len(addr) > 18 else addr
        cat = label.get("category") or "unlabeled"
        entity = label.get("value") or "-"
        conf = result.get("confidence", "unverified")
        print(f"{short:<20} {cat:<15} {entity:<20} {conf}")


if __name__ == "__main__":
    main()
