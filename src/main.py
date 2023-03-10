"""
Description:
    Main application entry point
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from pathlib import Path

import openai

APP_VERSION = "v0.0.2"
# keys folder in the root of the project with the api key in a file named `.openai-key`
API_KEY_LOCATION = Path("keys") / ".openai-key"
OS_VERSION = "ubuntu 20.04 running on wsl2"
SHELL_TYPE = "bash"


@dataclass
class AppConfig:
    exe_file_dir: Path
    api_key: str

    @staticmethod
    def init() -> AppConfig:
        exe_file_dir = Path(os.path.dirname(__file__))
        api_key = AppConfig._get_api_key(exe_file_dir)

        return AppConfig(exe_file_dir=exe_file_dir, api_key=api_key)

    @staticmethod
    def _get_api_key(exe_file_dir: Path):
        if api_key := os.getenv("OPENAI_API_KEY"):
            return api_key

        api_file = exe_file_dir.parent / API_KEY_LOCATION
        try:
            api_key = api_file.read_text(encoding="utf-8")
        except FileNotFoundError:
            api_key = input("Please enter your OpenAI API key: ")
            api_file.write_text(api_key, encoding="utf-8")

        return api_key


def generate_command(prompt_input):
    # generate text using GPT model
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt_input,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # extract command from generated text
    generated_text = str(response.choices[0].text)  # type: ignore
    # remove trailing and leading: `\n` then ':' then whitespace
    command = generated_text.strip("\n").strip(":").strip()
    # return command and full generated text
    return command, generated_text


def clean_terminal_line():
    # move the cursor to the beginning of the line
    sys.stdout.write("\r")
    # clear the line
    sys.stdout.write("\033[K")
    sys.stdout.flush()


def main() -> None:  # pylint: disable=missing-function-docstring
    app_config = AppConfig.init()
    openai.api_key = app_config.api_key

    primer = "you are senior systems admin. I need your help generating executable CLI \
commands in {SHELL_TYPE} on {OS_VERSION}. Please provide me with a command that I can \
execute directly, without any additional text or explanations."
    prompt_input = primer + sys.argv[1]
    cmd, _ = generate_command(prompt_input)

    clean_terminal_line()
    print(cmd, flush=True)
    # Program Done


if __name__ == "__main__":
    main()
