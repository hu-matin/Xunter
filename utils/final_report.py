from rich.console import Console

console = Console()

def generate_report(results):

    total = len(results)
    ok = len([r for r in results if r["score"] > 60])

    console.print("\n[bold cyan]===== FINAL REPORT =====[/bold cyan]")

    console.print(f"[green]Total:[/green] {total}")
    console.print(f"[yellow]Working:[/yellow] {ok}")

    console.print("\n[magenta]By Type:[/magenta]")

    types = {}

    for r in results:
        types[r["type"]] = types.get(r["type"], 0) + 1

    for k, v in types.items():
        console.print(f"[cyan]{k}[/cyan] -> [green]{v}[/green]")

    console.print("[bold cyan]========================[/bold cyan]\n")