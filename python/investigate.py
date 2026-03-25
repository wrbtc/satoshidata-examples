#!/usr/bin/env python3
"""Bitcoin investigation agent in 30 lines.

Checks a list of addresses, identifies who they belong to, and flags anything suspicious.
Uses only free endpoints — no API key needed.

Usage: python investigate.py
"""

import json
from urllib.request import Request, urlopen

ADDRESSES = [
    "bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h",  # Binance cold wallet
    "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",            # Satoshi's genesis address
    "1N52wHoVR79PMDishab2XmRHsbekCdGquK",            # Bittrex
    "1GbwVw5LiEoUNijSA4QuSMBp8VhDgksDpV",            # ePay.info
]


def check(addr):
    url = f"https://satoshidata.ai/v1/wallets/{addr}/trust-safety"
    req = Request(url, headers={"User-Agent": "satoshidata-examples/1.0"})
    return json.loads(urlopen(req).read())


print("Bitcoin Address Investigation")
print("=" * 60)
for addr in ADDRESSES:
    r = check(addr)
    label = r.get("label", {})
    assessment = r.get("assessment", {})
    entity = label.get("value") or "Unknown"
    category = label.get("category") or "unlabeled"
    state = assessment.get("state", "?")
    headline = assessment.get("headline", "No data")

    flag = ""
    if category in ("scam", "gambling", "mixer", "darknet"):
        flag = " [SUSPICIOUS]"

    print(f"\n  {addr[:12]}...{addr[-6:]}")
    print(f"  Entity:     {entity} ({category}){flag}")
    print(f"  Assessment: {headline}")
    print(f"  Confidence: {r.get('confidence', '?')}")

print("\n" + "=" * 60)
print("Investigation complete. 0 sats spent.")
