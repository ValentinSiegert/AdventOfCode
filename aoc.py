import os
import subprocess
from pathlib import Path


# Constants
CWD = Path(os.getcwd())
AOCD_DIR = CWD / 'aocd'
os.environ['AOCD_DIR'] = str(AOCD_DIR)


if __name__ == "__main__":
    if not AOCD_DIR.exists():
        os.makedirs(AOCD_DIR)
    if not (AOCD_DIR / 'token').exists():
        with open(AOCD_DIR / 'token', 'w') as f:
            f.write('your_token_here')
        print(f"Please add your token to the token file in the aocd directory and run the script again.")
        print(f"Your token can be found at https://adventofcode.com/")
        print(f"Place token to: {AOCD_DIR / 'token'}")
        exit(0)


