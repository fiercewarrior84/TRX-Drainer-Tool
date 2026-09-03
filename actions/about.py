# -*- coding: utf-8 -*-
"""About action — Features, supported wallets, contact"""

from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule
from rich import box
from system.ui import console


def action_about():
    console.print()
    console.print(Rule("[bold red]ABOUT[/]", style="red"))

    features_table = Table(show_header=True, header_style="bold red", border_style="dim", box=box.SIMPLE)
    features_table.add_column("Feature", style="green")
    features_table.add_column("Status", justify="center")
    for feat in [
        "Multi-wallet sweeping",
        "TRX & TRC20 token draining",
        "Real-time balance monitoring",
        "Energy-optimized transactions",
        "TronLink/Trust Wallet support",
        "Auto-confirm transactions",
        "Custom fee limits",
        "Minimum balance threshold",
        "Fee delegation for lower costs",
        "Multi-RPC failover",
        "Telegram notifications",
        "Cross-platform support",
    ]:
        features_table.add_row(feat, "[green]+[/]")

    wallets_table = Table(show_header=True, header_style="bold red", border_style="dim", box=box.SIMPLE)
    wallets_table.add_column("Wallet", style="green")
    wallets_table.add_column("Support", justify="center")
    for w in ["TronLink", "Trust Wallet", "Ledger", "ImToken", "BitKeep", "TokenPocket"]:
        wallets_table.add_row(w, "[green]Full[/]")

    tokens_table = Table(show_header=True, header_style="bold red", border_style="dim", box=box.SIMPLE)
    tokens_table.add_column("Category", style="green")
    tokens_table.add_column("Tokens", style="cyan")
    tokens_table.add_row("Native", "TRX")
    tokens_table.add_row("Stablecoins", "USDT, USDC, TUSD, USDJ")
    tokens_table.add_row("DeFi", "JST, SUN, WIN, BTT, NFT")
    tokens_table.add_row("Meme", "BTT, WIN, NFT, APENFT")

    contact_table = Table(show_header=True, header_style="bold red", border_style="dim", box=box.SIMPLE)
    contact_table.add_column("Channel", style="green")
    contact_table.add_column("Value", style="cyan")
    contact_table.add_row("Telegram", "JOIN OUR TELEGRAM CHAT")
    contact_table.add_row("TRX Address", "TDRAiN...abc123")
    contact_table.add_row("Support", "GitHub Issues or Telegram")

    console.print(Panel(features_table, title="[bold] Features [/]", border_style="red", box=box.ROUNDED))
    console.print()
    console.print(Panel(wallets_table, title="[bold] Supported Wallets [/]", border_style="red", box=box.ROUNDED))
    console.print()
    console.print(Panel(tokens_table, title="[bold] Supported Tokens [/]", border_style="red", box=box.ROUNDED))
    console.print()
    console.print(Panel(contact_table, title="[bold] Contact [/]", border_style="red", box=box.ROUNDED))
    console.print()
    console.print("[bold red]Contribution:[/] Don't forget to put stars *")
    console.print("[dim]Python 3.10+. Questions? Contact via Telegram or Issues.[/]")
    console.print()
