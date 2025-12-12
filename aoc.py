import datetime
import os
import shutil
import typer
from pathlib import Path
from typing_extensions import Annotated


class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


# Constants
CWD = Path(os.getcwd())
AOCD_DIR = CWD / 'aocd'
AOC_TEMPLATE = CWD / 'aoc_template.py'
os.environ['AOCD_DIR'] = str(AOCD_DIR)
TODAY = datetime.datetime.today()

typer_app = typer.Typer()


@typer_app.command(name='r')
def run(year: Annotated[int, typer.Option("--year", "-y")] = int(TODAY.year),
        day: Annotated[int, typer.Option("--day", "-d")] = int(TODAY.day),
        part: Annotated[int, typer.Option("--part", "-p")] = 0,
        input_data: Annotated[str, typer.Option("--input", "-i")] = "",
        submit: Annotated[bool, typer.Option("--submit", "-s")] = False,
        measure: Annotated[bool, typer.Option("--measure", "-m")] = False):
    """
    Run the solution for the given year and day.
    :param year: The year of the puzzle.
    :param day: The day of the puzzle.
    :param part: The part of the puzzle to run, 0 for both parts.
    :param input_data: The input to use for the puzzle. If a single digit number is given, it will use the example input indexed by that number.
    :param submit: Whether to submit the answer to the AoC website.
    :param measure: Whether to measure the execution time.
    """
    year_create = not (year_dir := (CWD / f"{year}")).exists()
    day_create = not (day_path := (year_dir / f'day{day:02}.py')).exists()
    if year_create or day_create:
        if year_create:
            os.makedirs(year_dir)
            with open(year_dir / '__init__.py', 'w') as f:
                f.write('')
        shutil.copy(AOC_TEMPLATE, day_path)
        print(f"{Color.BOLD}{Color.GREEN}Just initialized year {year} day {day} file, riddle me this!{Color.END}")
        exit(0)
    puzzle = aocd.models.Puzzle(year=year, day=day)
    is_example_exec = (len(input_data) == 1 and input_data.isnumeric())
    if not input_data:
        input_data = puzzle.input_data
    elif is_example_exec:
        input_data = puzzle.examples[int(input_data)].input_data
    solution = __import__(f'{year}.day{day:02}', fromlist=[''])
    if measure:
        import time
        start = time.time()
    response = solution.solve(input_data, part)
    if measure:
        time_str = f'{time_diff:.4f} seconds' if (time_diff := time.time() - start) > 1.000 else f'{time_diff*1000:.4f} milliseconds'
        if part == 0:
            print(f"{Color.BOLD}{Color.BLUE}Execution time for both parts:{Color.END} {time_str}")
        if part == 1:
            print(f"{Color.BOLD}{Color.BLUE}Execution time for part 1:{Color.END} {time_str}")
        if part == 2:
            print(f"{Color.BOLD}{Color.BLUE}Execution time for part 2:{Color.END} {time_str}")
    if response == 0:
        print(f'{Color.BOLD}{Color.RED}No solution implemented for year {year} day {day} part {part}.{Color.END}')
        print(f'{Color.BOLD}{Color.RED}Will not submit empty solution.{Color.END}')
        submit = False
    if response == (0, 0):
        print(f'{Color.BOLD}{Color.RED}No solution implemented for year {year} day {day} parts 1 and 2.{Color.END}')
        print(f'{Color.BOLD}{Color.RED}Will not submit empty solutions.{Color.END}')
        submit = False
    if response[0] == 0 and response[1] > 0:
        print(f'{Color.BOLD}{Color.RED}No solution implemented for year {year} day {day} part 1.{Color.END}')
        print(f'{Color.BOLD}{Color.RED}Will not submit empty solution for part 1.{Color.END}')
        response, part = response[1], 2
    if response[1] == 0 and response[0] > 0:
        print(f'{Color.BOLD}{Color.RED}No solution implemented for year {year} day {day} part 2.{Color.END}')
        print(f'{Color.BOLD}{Color.RED}Will not submit empty solution for part 2.{Color.END}')
        response, part = response[0], 1
    if not is_example_exec and submit:
        if part == 1:
            aocd.submit(response, part='a', day=day, year=year)
        if part == 2:
            aocd.submit(response, part='b', day=day, year=year)
        if part == 0:
            aocd.submit(response[0], part='a', day=day, year=year)
            aocd.submit(response[1], part='b', day=day, year=year)



@typer_app.command(name='p')
def print_answer(year: Annotated[int, typer.Option("--year", "-y")] = int(TODAY.year),
                 day: Annotated[int, typer.Option("--day", "-d")] = int(TODAY.day),
                 part: Annotated[int, typer.Option("--part", "-p")] = 0):
    """
    Print the answer for the given year and day and part.
    :param year: The year of the puzzle.
    :param day: The day of the puzzle.
    :param part: The part of the puzzle. 0 for both parts.
    """
    puzzle = aocd.models.Puzzle(year=year, day=day)
    if part == 0:
        print(f"{Color.BOLD}{Color.BLUE}Answer for year {year} day {day} part 1:{Color.END}\n{puzzle.answers[0]}")
        print(f"{Color.BOLD}{Color.BLUE}Answer for year {year} day {day} part 2:{Color.END}\n{puzzle.answers[1]}")
    elif part in [1, 2]:
        print(f"{Color.BOLD}{Color.BLUE}Answer for year {year} day {day} part {part}:{Color.END}\n{puzzle.answers[part-1]}")


@typer_app.command(name='e')
def examples(year: Annotated[int, typer.Option("--year", "-y")] = int(TODAY.year),
             day: Annotated[int, typer.Option("--day", "-d")] = int(TODAY.day)):
    """
    Print the examples for the given year and day.
    :param year: The year of the puzzle.
    :param day: The day of the puzzle.
    """
    puzzle = aocd.models.Puzzle(year=year, day=day)
    for i, example in enumerate(puzzle.examples):
        print(f"{Color.BOLD}{Color.YELLOW}Example {i} for year {year} day {day}:{Color.END}\n{example.input_data}\n")


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


