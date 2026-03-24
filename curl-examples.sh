#!/bin/bash
# satoshidata.ai — all 10 free endpoints
# No API key needed. Run any of these directly.

echo "=== Wallet Trust-Safety ==="
curl -s https://satoshidata.ai/v1/wallets/1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa/trust-safety | python3 -m json.tool

echo -e "\n=== Bitcoin Price ==="
curl -s https://satoshidata.ai/v1/price | python3 -m json.tool

echo -e "\n=== Fee Estimates ==="
curl -s https://satoshidata.ai/v1/fees/recommended | python3 -m json.tool

echo -e "\n=== Mempool Stats ==="
curl -s https://satoshidata.ai/v1/mempool/stats | python3 -m json.tool

echo -e "\n=== On-Chain Activity ==="
curl -s https://satoshidata.ai/v1/onchain | python3 -m json.tool

echo -e "\n=== Transaction Status ==="
curl -s https://satoshidata.ai/v1/tx/a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d/status | python3 -m json.tool

echo -e "\n=== Capabilities ==="
curl -s https://satoshidata.ai/v1/capabilities | python3 -m json.tool

echo -e "\n=== Timestamp Quote ==="
curl -s https://satoshidata.ai/v1/timestamp/quote | python3 -m json.tool
