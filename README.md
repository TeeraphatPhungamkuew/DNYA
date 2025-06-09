
# Delta-Neutral Yield Agent (DNYA)

An autonomous DeFi yield farming agent built on top of the [Vibekit](https://github.com/EmberAGI/arbitrum-vibekit) framework for Arbitrum.  
DNYA automates delta-neutral strategies by integrating Pendle, Aave, and GMX—enabling users to earn yield while minimizing directional risk.

---

## 🔍 What It Does

This agent:
- Deposits user assets into Pendle for yield farming.
- Sells Yield Tokens (YT) for upfront gains.
- Opens short positions via GMX (or borrows via Aave) to hedge Principal Token (PT) exposure.
- Periodically monitors delta and rebalances when needed.

---

## 🧠 Architecture

- **Agent Framework:** Vibekit (MCP agent model)
- **Protocols Used:** Pendle, GMX, Aave (Arbitrum)
- **Decision Pipeline:**
  1. Detect asset deposit
  2. Split into PT / YT (Pendle)
  3. Sell YT → record upfront yield
  4. Open short on PT or borrow hedge
  5. Monitor delta, funding rates
  6. Rebalance automatically

---

## 🔗 Protocol Integrations

- [Pendle Finance](https://app.pendle.finance)
- [GMX (Perp DEX)](https://gmx.io)
- [Aave v3](https://app.aave.com)

---

## ⚙️ Project Status

| Component         | Status     |
|------------------|------------|
| Agent Template    | ✅ Drafted |
| Pendle Integration| ✅ In Progress |
| GMX Integration   | 🔄 Planned |
| PnL Dashboard     | 🔄 Planned |
| Backtesting Suite | 🔄 Planned |

---

## 🚀 Getting Started

To run the Delta-Neutral Yield Agent (DNYA) locally:

### 1. Clone the repository

```bash
git clone https://github.com/TeeraphatPhungamkuew/DNYA.git
cd DNYA

# Install dependencies (Python, Brownie, etc.)
pip install -r requirements.txt
```

---

## 📂 File Structure

```
delta-neutral-agent/
│
├── agent/               # Vibekit-compatible agent logic
│   └── dnya_agent.py
│
├── contracts/           # Optional custom smart contracts
│
├── utils/               # Strategy logic, helpers
│   └── strategy.py
│
├── README.md
└── requirements.txt
```

---

## 🪙 License

MIT License

---

## 🙌 Contributing

Pull requests and suggestions welcome. Join us on [Farcaster](https://warpcast.com/) and follow development on [Vibekit GitHub](https://github.com/EmberAGI/arbitrum-vibekit).
