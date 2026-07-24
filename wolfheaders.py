import argparse

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.panel import Panel

from banner import print_banner
from analyzer import fetch_headers
from scorer import analyze_headers

console = Console()


def main():
    parser = argparse.ArgumentParser(
        prog="wolfheaders",
        description="Analyze HTTP Security Headers",
    )

    parser.add_argument(
        "target",
        help="Target URL or domain (e.g. example.com)"
    )

    parser.add_argument(
        "--version",
        action="version",
        version="WolfHeaders v1.0.0"
    )

    args = parser.parse_args()

    print_banner()

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:

        task = progress.add_task(
            "[cyan][1/2][/cyan] Fetching HTTP headers...",
            total=None,
        )

        try:
            response = fetch_headers(args.target)
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")
            return

        progress.update(
            task,
            description="[green]✓ Headers received"
        )

    score, total, results = analyze_headers(response["headers"])

    header_table = Table(
        title="Security Header Analysis",
        show_lines=True
    )

    header_table.add_column("Header", style="cyan")
    header_table.add_column("Status", justify="center")
    header_table.add_column("Description")

    recommendations = []

    for item in results:

        if item["present"]:
            status = "[green]✓ Present[/green]"
        else:
            status = "[red]✗ Missing[/red]"
            recommendations.append(item["header"])

        header_table.add_row(
            item["header"],
            status,
            item["description"],
        )

    console.print()
    console.print(header_table)

    recommendation_table = Table(title="Recommendations")

    recommendation_table.add_column("Missing Header", style="yellow")

    if recommendations:
        for header in recommendations:
            recommendation_table.add_row(header)
    else:
        recommendation_table.add_row(
            "[green]No recommendations. Great job![/green]"
        )

    console.print()
    console.print(recommendation_table)

    console.print()

    console.print(
        Panel.fit(
            f"""
[bold cyan]Target[/bold cyan] : {response['url']}
[bold cyan]Status[/bold cyan] : {response['status']}
[bold cyan]Security Score[/bold cyan] : {score}/{total}
[bold cyan]Headers Present[/bold cyan] : {score}
[bold cyan]Headers Missing[/bold cyan] : {total-score}
""",
            title="[bold green]Summary[/bold green]",
            border_style="green",
        )
    )

    console.print(
        "\n[dim]WolfHeaders v1.0.0 • github.com/leescripts-dev/WolfHeaders[/dim]"
    )


if __name__ == "__main__":
    main()