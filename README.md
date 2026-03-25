# satoshidata.ai — Bitcoin Wallet Intelligence API

**Other Bitcoin APIs tell you the fee rate. We tell you who you're sending to.**

30M+ labeled Bitcoin addresses. Identify exchanges, mining pools, scams, gambling, government seizures — with confidence scoring on every response. No signup, no API key for free tier.

## 30-second demo

```bash
curl https://satoshidata.ai/v1/wallets/bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h/trust-safety
```

```json
{
  "address": "bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h",
  "label": { "category": "exchange", "value": "Binance" },
  "confidence": "verified",
  "evidence_tier": "strong",
  "assessment": {
    "state": "labeled",
    "headline": "Verified entity hit"
  }
}
```

## Add to your AI agent

### Claude Code
```bash
claude mcp add satoshidata --url https://satoshidata.ai/mcp/
```

### Claude Desktop
Add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "satoshidata": {
      "url": "https://satoshidata.ai/mcp/"
    }
  }
}
```

### Cursor
Add to `.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "satoshidata": {
      "url": "https://satoshidata.ai/mcp/"
    }
  }
}
```

### VS Code
Add to `.vscode/mcp.json`:
```json
{
  "servers": {
    "satoshidata": {
      "url": "https://satoshidata.ai/mcp/"
    }
  }
}
```

Then ask: *"Who owns Bitcoin address bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h?"*

## Python examples

### Investigate addresses (zero dependencies, free)

```bash
python python/investigate.py
```

Output:
```
Bitcoin Address Investigation
============================================================

  bc1qm34lsc65...j77s3h
  Entity:     Binance (exchange)
  Confidence: verified

  1N52wHoVR79P...CdGquK
  Entity:     Bittrex (exchange)
  Confidence: high

============================================================
Investigation complete. 0 sats spent.
```

### Single address lookup

```bash
pip install requests
python python/lookup.py bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h
```

### Batch check

```bash
python python/batch_check.py
```

## Free endpoints (10)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/wallets/{addr}/trust-safety` | Wallet trust & safety profile |
| GET | `/v1/price` | BTC price snapshot |
| GET | `/v1/onchain` | On-chain activity |
| GET | `/v1/fees/recommended` | Fee recommendations |
| GET | `/v1/mempool/stats` | Mempool state |
| GET | `/v1/tx/{txid}/status` | Transaction status |
| GET | `/v1/capabilities` | All capabilities |
| GET | `/v1/timestamp/{hash}` | Timestamp status |
| GET | `/v1/timestamp/quote` | Timestamp quote |
| POST | `/v1/timestamp/verify` | Verify a proof |

## Premium endpoints (21 sats / $0.01 per call)

Pay with Lightning L402 or x402 USDC on Base — per-call, no key needed. Or get a monthly API key for $4.99.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/wallets/{addr}/summary` | Full wallet intelligence |
| GET | `/v1/wallets/{addr}/detail` | Label evidence |
| GET | `/v1/wallets/{addr}/contributors` | Label contributors |
| POST | `/v1/batch/trust-safety` | Batch (up to 100) |
| POST | `/v1/batch/summary` | Batch summaries |
| GET | `/v1/tx/{txid}` | Full transaction |
| POST | `/v1/tx/verify` | Payment verification |
| POST | `/v1/timestamp` | Submit timestamp |
| GET | `/v1/timestamp/{hash}/proof` | Download proof |

## Links

- **API**: [satoshidata.ai](https://satoshidata.ai)
- **MCP**: [satoshidata.ai/mcp/](https://satoshidata.ai/mcp/)
- **OpenAPI**: [satoshidata.ai/openapi.json](https://satoshidata.ai/openapi.json)
- **Smithery**: [satoshidata/wallet-intelligence](https://smithery.ai/servers/satoshidata/wallet-intelligence)
- **Substack**: [satoshiai.substack.com](https://satoshiai.substack.com)

## License

MIT
