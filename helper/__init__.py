import json
import bs4
from pathlib import Path
import os
import requests
import dotenv
import time

dotenv.load_dotenv()

YEAR = 2020
THIS_DIR = Path(__file__).parent
TOKEN = {"session": os.environ.get("AOC_SESSION_COOKIE")}
INPUT_FILE = "inputs.json"
SUBMISSIONS_FILE = "submissions.json"
URL = f"https://adventofcode.com/{YEAR}/day/{{day}}"


def timer(func):
    def inner(*args, **kwargs):
        s = time.perf_counter()
        func(*args, **kwargs)
        return time.perf_counter() - s
    return inner


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

    solution = str(func())
    if solution is None:
        return

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

    submissions[day][part][solution] = message

    with open(THIS_DIR / SUBMISSIONS_FILE, "w") as f:
        json.dump(submissions, f)

