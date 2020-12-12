import json
import bs4
from pathlib import Path
import os
import requests
import typing as t
import dotenv
import re

dotenv.load_dotenv()

YEAR = 2020
THIS_DIR = Path(__file__).parent
TOKEN = {"session": os.environ.get("AOC_SESSION_COOKIE")}
INPUT_FILE = "inputs.json"
SUBMISSIONS_FILE = "submissions.json"
URL = f"https://adventofcode.com/{YEAR}/day/{{day}}"


def day(d: int) -> str:
    d = str(d)

    with open(THIS_DIR / INPUT_FILE) as fin:
        inputs = json.load(fin)

    if d in inputs:
        return inputs[d]

    response = requests.get(url=URL.format(day=d) + "/input", cookies=TOKEN)
    if not response.ok:
        raise ValueError("bad response")

    inputs[d] = response.text.strip()
    with open(THIS_DIR / INPUT_FILE, 'w') as fout:
        json.dump(inputs, fout)

    return inputs[d]


def submit(day: int, func):
    day = str(day)
    part = "1" if func.__name__ == "part_one" else "2"

    with open(THIS_DIR / SUBMISSIONS_FILE) as f:
        submissions = json.load(f)

    if day not in submissions:
        submissions[day] = {"1": {}, "2": {}}

    if "solution" in submissions[day][part]:
        print(f"Day {day} part {part} already solved. Solution: {submissions[day][part]['solution']}")
        return

    if (solution := func()) is None:
        return

    solution = str(solution)
    print(solution)

    if solution in submissions[day][part]:
        print(f"Solution {solution} to part {part} has already been submitted")
        return

    response = requests.post(url=URL.format(day=day) + "/answer", cookies=TOKEN,
                             data={"level": part, "answer": solution})

    if not response.ok:
        raise ValueError("bad response")

    message = bs4.BeautifulSoup(response.text, "html.parser").article.text

    if message.startswith("You gave"):
        print(message)

    if message.startswith("That's the"):
        print("correct answer")

    if message.startswith("That's not"):
        print("wrong answer", end="")
        if "too low" in message:
            print(": too low")
        elif "too high" in message:
            print(": too high")

    submissions[day][part][solution] = message

    with open(THIS_DIR / SUBMISSIONS_FILE, "w") as f:
        json.dump(submissions, f)


def prod(L):
    p = 1
    for x in L:
        p *= x
    return p


def extract_ints(s: str) -> t.List[int]:
    return [int(x) for x in re.findall(r'(\d+)', s)]
