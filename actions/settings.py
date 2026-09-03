# -*- coding: utf-8 -*-
"""Settings action — Configuration reference for TRX Drainer Tool"""

from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule
from rich import box
from system.ui import console


def action_settings():
    console.print()
    console.print(Rule("[bold red]SETTINGS[/]", style="red"))
    table = Table(show_header=True, header_style="bold red", border_style="dim", box=box.SIMPLE)
    table.add_column("Parameter", style="green")
    table.add_column("Type", style="dim")
    table.add_column("Default", style="yellow")
    table.add_column("Description", style="dim")
    table.add_row("target_wallets", "list", "[]", "TRON addresses to monitor")
    table.add_row("destination_wallet", "string", '""', "Receiving wallet address")
    table.add_row("drain_mode", "string", '"sweep"', "sweep or selective")
    table.add_row("min_balance_trx", "int", "100", "Minimum TRX to trigger drain")
    table.add_row("include_trc20", "bool", "true", "Also drain TRC20 tokens")
    table.add_row("trc20_tokens", "list", '["USDT",...]', "TRC20 tokens to drain")
    table.add_row("rpc_endpoint", "string", '"trongrid"', "TRON RPC URL")
    table.add_row("energy_optimize", "bool", "true", "Use fee delegation")
    table.add_row("auto_confirm", "bool", "true", "Auto-confirm transactions")
    table.add_row("fee_limit", "int", "10000000", "Max fee in SUN")
    panel = Panel(table, title="[bold] config.json Reference [/]", border_style="red", box=box.ROUNDED)
    console.print(panel)
    console.print()
    console.print("[dim]Edit config.json directly or use menu options 4-5 to configure interactively.[/]")
    console.print()
