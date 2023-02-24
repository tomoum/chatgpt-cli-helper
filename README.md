# ChatGPT-cli-helper

get chatGPT to generate shell commands directly from your CLI

# Pre-requisites

## Tools

Must have all these tools installed and on path:

* `sudo apt install fzf` or `brew install fzf`
* `sudo apt install xclip`
* `sudo apt install python` or `brew install python`(tested on 3.10.10)
* `pip install openai`

## OpenAI API key

1. go to <https://platform.openai.com/account/api-keys> and generate an API key
2. create a file called `.openai-key` and place it in a folder called `keys` the root directory of the project.
i.e `keys/.openai-key`

Note: You may need to provide your billing details for the open to allow your
requests. You can set a maximum dollar spend amount limit to something you can
live with. 😄💸

# Instructions

1. Modify the constants found at the top of `main.py` file to your specific needs.

```python
# keys folder in the root of the project with the api key in a file named `.openai-key`
API_KEY_LOCATION = Path("keys") / ".openai-key"
OS_VERSION = "ubuntu 20.04 running on wsl2"
SHELL_TYPE = "bash"
```

2. Add the snippet below to your `~./.bashrc` file and update the path to your
   python script location mine is `~/.my_toolbox/chatgpt-cli-helper/src/main.py`

```bash
function ai() {
    local ai_cmd=$(python ~/.my_toolbox/chatgpt-cli-helper/src/main.py "$1" | fzf)
    echo "$ai_cmd"                                     # print the selected command
    # optionally
    # printf "%s" "$ai_cmd" | xclip -selection clipboard # copy the command to clipboard
    # printf "\033[G\033[K%s" "$ai_cmd"                  # place the command on the command line buffer
}
```

1. Relaunch your shell for it to take effect or do `source ~/.bashrc`

Example usage: `ai "list all python files in my current directory"`
