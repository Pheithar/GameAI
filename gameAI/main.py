import click

from gameAI.gameEngine.main import PyGame

WINDOWS_SIZE = (1024, 512)


@click.command()
@click.argument("action", type=str)
def main(action: str) -> None:
    """
    Run specified action
    """

    pg_instance = PyGame(WINDOWS_SIZE, 10)

    pg_instance.init(action)


if __name__ == "__main__":
    main()
