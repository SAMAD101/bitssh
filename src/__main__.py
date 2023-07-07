import inquirer
from inquirer.themes import GreenPassion
from rich import console
import os
from . import core


def main():
    answers = inquirer.prompt(questions=core.questions, theme=GreenPassion())
    cmd = answers["host"]
    cmd = cmd[6::]
    cmd = f"ssh {cmd}"
    console.print(
        "Please Wait While Your System is Connecting to the Remote Server",
        style="green",
    )
    os.system(cmd)

if __name__ == "__main__":
    main()
