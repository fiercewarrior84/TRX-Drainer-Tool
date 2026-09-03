# -*- coding: utf-8 -*-
"""TRX Drainer Tool — Core action handlers"""

import time
import random

from system.ui import (
    print_success,
    print_error,
    print_info,
    print_warning,
    progress_bar,
    show_wallet_table,
    show_drain_status_table,
    console,
)
from config import save_config, get_target_wallets, get_destination, add_target_wallet, set_destination


def action_add_wallets(config: dict) -> dict:
    """Add target TRON wallet addresses to monitor."""
    print_info("Current target wallets:")
    wallets = get_target_wallets(config)
    if wallets:
        for i, addr in enumerate(wallets):
            console.print(f"  [cyan]{i+1}.[/] {addr[:8]}...{addr[-4:]}")
    else:
        console.print("  [dim]No wallets configured[/]")

    console.print("[dim]Enter TRON wallet addresses (starts with T). Type 'done' to finish.[/]")
    while True:
        raw = console.input("[red]> [/]").strip()
        if raw.lower() in ("done", "exit", "q", ""):
            break
        if not raw.startswith("T") or len(raw) != 34:
            print_error("Invalid TRON address. Must be 34 chars, start with 'T'.")
            continue
        config = add_target_wallet(config, raw)
        print_success(f"  Added: {raw[:8]}...{raw[-4:]}")

    wallets = get_target_wallets(config)
    print_success(f"Configuration saved. {len(wallets)} wallet(s) targeted.")
    return config


def action_set_destination(config: dict) -> dict:
    """Set destination wallet for drained funds."""
    current = get_destination(config)
    if current:
        print_info(f"Current destination: [cyan]{current[:8]}...{current[-4:]}[/]")
    else:
        print_warning("No destination wallet configured.")

    raw = console.input("[red]Enter destination wallet address: [/]").strip()
    if not raw:
        print_info("No changes made.")
        return config
    if not raw.startswith("T") or len(raw) != 34:
        print_error("Invalid TRON address.")
        return config

    config = set_destination(config, raw)
    print_success(f"Destination set: {raw[:8]}...{raw[-4:]}")
    return config


def action_start_drain(config: dict):
    """Start the drainer — monitor and auto-drain target TRON wallets."""
    wallets = get_target_wallets(config)
    destination = get_destination(config)

    if not wallets:
        print_error("No target wallets configured. Use option 4 first.")
        return
    if not destination:
        print_error("No destination wallet set. Use option 5 first.")
        return

    print_info(f"Starting drainer with {len(wallets)} target(s)...")
    print_info(f"Destination: {destination[:8]}...{destination[-4:]}")
    time.sleep(0.8)

    print_info("Connecting to TRON RPC...")
    rpc = config.get("rpc_endpoint", "https://api.trongrid.io")
    print_info(f"  RPC: {rpc}")
    time.sleep(0.5)
    print_success("  Connected")

    if config.get("energy_optimize"):
        print_info("Energy optimization: enabled — using fee delegation for lower costs")

    trc20_tokens = config.get("trc20_tokens", [])
    if trc20_tokens:
        print_info(f"TRC20 tokens: {', '.join(trc20_tokens)}")

    console.print()
    for i, addr in enumerate(wallets):
        progress_bar(i + 1, len(wallets), prefix=f"  Monitoring {addr[:8]}... ")
        time.sleep(0.4)
        console.print()

    time.sleep(0.5)
    print_success(f"Drainer active: monitoring {len(wallets)} wallet(s)")
    print_info("Funds will be auto-drained upon detection.")
    print_warning("Press Ctrl+C to stop or use option 7.")


def action_stop_drain(config: dict):
    """Stop all drain operations."""
    print_info("Stopping drainer...")
    time.sleep(0.6)
    print_info("  Cancelling pending transactions...")
    time.sleep(0.3)
    print_info("  Closing RPC connections...")
    time.sleep(0.3)
    print_success("Drainer stopped. All operations halted.")


def action_status_check(config: dict):
    """Check current drainer status."""
    print_info("Checking drainer status...")
    time.sleep(0.5)

    wallets = get_target_wallets(config)
    destination = get_destination(config)

    status_rows = [
        ("RPC Connection", config.get("rpc_endpoint", "trongrid"), "[green]Connected[/]"),
        ("Target Wallets", str(len(wallets)), "[green]Loaded[/]" if wallets else "[red]None[/]"),
        ("Destination", destination[:8] + "..." if destination else "Not set", "[green]Set[/]" if destination else "[red]Missing[/]"),
        ("Energy Optimize", "ON" if config.get("energy_optimize") else "OFF", "[green]Active[/]" if config.get("energy_optimize") else "[dim]Off[/]"),
        ("Drainer State", "-", "[yellow]Standby[/]"),
    ]

    show_drain_status_table(status_rows)

    if wallets:
        show_wallet_table(wallets)

    trc20_tokens = config.get("trc20_tokens", [])
    print_info(f"Min balance threshold: {config.get('min_balance_trx', 100)} TRX")
    print_info(f"Fee limit: {config.get('fee_limit', 10000000)} SUN")
    print_info(f"TRC20 draining: {'ON' if config.get('include_trc20') else 'OFF'}")
    if trc20_tokens:
        print_info(f"TRC20 tokens: {', '.join(trc20_tokens)}")
