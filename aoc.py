import datetime
import os
import typer
from pathlib import Path


# Constants
CWD = Path(os.getcwd())
AOCD_DIR = CWD / 'aocd'
os.environ['AOCD_DIR'] = str(AOCD_DIR)
TODAY = datetime.datetime.today()

typer_app = typer.Typer()

@typer_app.command()
def fetch(year: int = int(TODAY.year), day: int = int(TODAY.day)):
    puzzle = aocd.models.Puzzle(year=year, day=day)
    if not (year_dir := (CWD / year)).exists():
        os.makedirs(year_dir)
        with open(year_dir / '__init__.py', 'w') as f:
            f.write('')
    if not (day_dir := (year_dir / f'day{day:02}')).exists():
        os.makedirs(day_dir)
        with open(day_dir / '__init__.py', 'w') as f:
            f.write('')
    # with open(day_dir / f'day{day:02}.txt', 'w') as f:
    #     f.write(puzzle.input_data)

@typer_app.command()
def print_answer(year: int = int(TODAY.year), day: int = int(TODAY.day), part: int = 1):
    puzzle = aocd.models.Puzzle(year=year, day=day)
    print(f"Answer for year {year} day {day} part {part}: {puzzle.answers[part-1]}")


if __name__ == "__main__":
    if not AOCD_DIR.exists():
        os.makedirs(AOCD_DIR)
    if not (AOCD_DIR / 'token').exists():
        with open(AOCD_DIR / 'token', 'w') as f:
            f.write('your_token_here')
        print(f"Please add your token to the token file in the aocd directory and run the script again.")
        print(f"Your token can be found at https://adventofcode.com/ past logging in.")
        print(f"Place token to: {AOCD_DIR / 'token'}")
        exit(0)
    import aocd
    typer_app()


