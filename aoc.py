import datetime
import os
import shutil
import typer
from pathlib import Path


# Constants
CWD = Path(os.getcwd())
AOCD_DIR = CWD / 'aocd'
AOC_TEMPLATE = CWD / 'aoc_template.py'
os.environ['AOCD_DIR'] = str(AOCD_DIR)
TODAY = datetime.datetime.today()

typer_app = typer.Typer()

@typer_app.command()
def r(year: int = int(TODAY.year), day: int = int(TODAY.day), part: int = 0, input_data: str = "", submit: bool = False):
    """
    Run the solution for the given year and day.
    :param year: The year of the puzzle.
    :param day: The day of the puzzle.
    :param part: The part of the puzzle to run, 0 for both parts.
    :param input_data: The input to use for the puzzle. If a single digit number is given, it will use the example input indexed by that number.
    :param submit: Whether to submit the answer to the AoC website.
    """
    year_create = not (year_dir := (CWD / f"{year}")).exists()
    day_create = not (day_dir := (year_dir / f'day{day:02}')).exists()
    if year_create or day_create:
        if year_create:
            os.makedirs(year_dir)
            with open(year_dir / '__init__.py', 'w') as f:
                f.write('')
        if day_create:
            os.makedirs(day_dir)
            with open(day_dir / '__init__.py', 'w') as f:
                f.write('')
        shutil.copy(AOC_TEMPLATE, day_dir / f'day{day:02}.py')
        print(f"Just initialized year {year} day {day} files, riddle me this!")
        exit(0)
    puzzle = aocd.models.Puzzle(year=year, day=day)
    is_example_exec = (len(input_data) == 1 and input_data.isnumeric())
    if not input_data:
        input_data = puzzle.input_data
    elif is_example_exec:
        input_data = puzzle.examples[int(input_data)].input_data
    module = f'{year}.day{day:02}.day{day:02}'
    solution = __import__(module, fromlist=[''])
    response = solution.solve(input_data, part)
    if not is_example_exec and submit:
        if part == 1 and not puzzle.answer_a:
            aocd.submit(response, part='a', day=day, year=year)
        if part == 2 and not puzzle.answer_b:
            aocd.submit(response, part='b', day=day, year=year)
        if part == 0:
            if not puzzle.answer_a:
                aocd.submit(response[0], part='a', day=day, year=year)
            if not puzzle.answer_b:
                aocd.submit(response[1], part='b', day=day, year=year)



@typer_app.command()
def print_answer(year: int = int(TODAY.year), day: int = int(TODAY.day), part: int = 1):
    """
    Print the answer for the given year and day and part.
    :param year: The year of the puzzle.
    :param day: The day of the puzzle.
    :param part: The part of the puzzle.
    """
    puzzle = aocd.models.Puzzle(year=year, day=day)
    print(f"Answer for year {year} day {day} part {part}: {puzzle.answers[part-1]}")


@typer_app.command()
def examples(year: int = int(TODAY.year), day: int = int(TODAY.day)):
    """
    Print the examples for the given year and day.
    :param year: The year of the puzzle.
    :param day: The day of the puzzle.
    """
    puzzle = aocd.models.Puzzle(year=year, day=day)
    for i, example in enumerate(puzzle.examples):
        print(f"Example {i}: {example.input_data}")


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


