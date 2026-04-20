from rich.table import Table
from rich import box


def color(v):
    return "[green]YES[/green]" if v else "[red]NO[/red]"


def score_color(s):
    if s >= 80:
        return f"[green]{s}[/green]"
    elif s >= 50:
        return f"[yellow]{s}[/yellow]"
    return f"[red]{s}[/red]"


def create_table():

    table = Table(box=box.SIMPLE, style='cyan')

    table.add_column("Name", style="cyan")
    table.add_column("Type", style="magenta")
    table.add_column("Connection(SOCKS)", justify="left")
    table.add_column("Domain(DNS)", justify="left")
    table.add_column("Network(TCP)", justify="left")
    table.add_column("Web(HTTP)", justify="left")
    table.add_column("Delay(ms)", justify="left")
    table.add_column("Score", justify="left")

    return table