# satoshidata.ai — Bitcoin Wallet Intelligence API

Identify any Bitcoin address. Verify transactions. Timestamp data on-chain.

- **10 free endpoints** — no API key, no signup
- **9 premium endpoints** — 21 sats per call via Lightning (L402) or $4.99/mo API key
- **14 MCP tools** — plug into Claude Desktop, Cursor, or any MCP client
- **Millions of labeled addresses** — exchanges, mining pools, scams, gambling, mixers, government seizures

## Quick start

### curl (free, no key needed)

```bash
# Identify any Bitcoin address
curl https://satoshidata.ai/v1/wallets/1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa/trust-safety

# Current Bitcoin price
curl https://satoshidata.ai/v1/price

# Fee estimates
curl https://satoshidata.ai/v1/fees/recommended

# Mempool stats
curl https://satoshidata.ai/v1/mempool/stats

# On-chain activity
curl https://satoshidata.ai/v1/onchain

# Transaction status
curl https://satoshidata.ai/v1/tx/a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d/status

# All capabilities
curl https://satoshidata.ai/v1/capabilities
```

### Python

```bash
pip install requests
python python/lookup.py bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h
```

See [`python/lookup.py`](python/lookup.py) for a single address lookup, and [`python/batch_check.py`](python/batch_check.py) for checking multiple addresses at once.

### MCP (Claude Desktop, Cursor, VS Code)

Copy [`mcp-config.json`](mcp-config.json) into your MCP client config:

```json
{
  "mcpServers": {
    "satoshidata": {
      "url": "https://smithery.ai/servers/satoshidata/wallet-intelligence"
    }
  }
}
```

This gives you 14 Bitcoin tools. Ask Claude: *"What is the trust-safety profile of bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h?"*

## Free endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/wallets/{addr}/trust-safety` | Wallet trust & safety profile |
| GET | `/v1/price` | BTC price, 24h range, RSI |
| GET | `/v1/onchain` | On-chain activity snapshot |
| GET | `/v1/fees/recommended` | Fee-rate recommendations |
| GET | `/v1/mempool/stats` | Mempool size and congestion |
| GET | `/v1/tx/{txid}/status` | Transaction state check |
| GET | `/v1/capabilities` | API capabilities summary |
| GET | `/v1/timestamp/{hash}` | Timestamp status |
| GET | `/v1/timestamp/quote` | Timestamp fee quote |
| POST | `/v1/timestamp/verify` | Verify a timestamp proof |

## Premium endpoints (21 sats per call)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/wallets/{addr}/summary` | Full wallet intelligence |
| GET | `/v1/wallets/{addr}/detail` | Label breakdown and evidence |
| GET | `/v1/wallets/{addr}/contributors` | Contributor depth |
| POST | `/v1/batch/trust-safety` | Batch up to 100 addresses |
| POST | `/v1/batch/summary` | Batch wallet summaries |
| GET | `/v1/tx/{txid}` | Full transaction lookup |
| POST | `/v1/tx/verify` | Payment verification |
| POST | `/v1/timestamp` | Submit hash for timestamping |
| GET | `/v1/timestamp/{hash}/proof` | Download timestamp proof |

## Links

- **Website**: [satoshidata.ai](https://satoshidata.ai)
- **OpenAPI spec**: [satoshidata.ai/openapi.json](https://satoshidata.ai/openapi.json)
- **Agent card**: [agent-card.json](https://satoshidata.ai/.well-known/agent-card.json)
- **Smithery**: [satoshidata/wallet-intelligence](https://smithery.ai/servers/satoshidata/wallet-intelligence)
- **Substack**: [satoshiai.substack.com](https://satoshiai.substack.com)

## License

MIT
