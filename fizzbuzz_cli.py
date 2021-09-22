import typer
import fizzbuzz

app = typer.Typer()

@app.command()
def classic_fizzbuzz(n: int):
    """Run the classsic fizzbuzz
    """
    typer.echo_via_pager(f'{s} ' for s in fizzbuzz.classic_fizzbuzz(n))

if __name__ == '__main__':
    app()
