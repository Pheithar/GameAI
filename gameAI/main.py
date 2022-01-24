import click

from gameAI.gameEngine.main import PyGame

WINDOWS_SIZE = (1024, 512)
FRAME_RATE = 60


@click.command()
@click.argument("action", type=str)
def main(action: str) -> None:
    """
    Run specified action
    """

    pg_instance = PyGame(WINDOWS_SIZE, FRAME_RATE)

    pg_instance.init(action)


if __name__ == "__main__":
    main()
