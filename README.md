# ChatGPT-cli-helper

get chatGPT to help you generate shell commands directly from your CLI

Example usage: `ai "list all python files in my current directory"`

![chatgpt_demo_v0 0 1](https://user-images.githubusercontent.com/14957264/221429391-661a5a72-e3ef-4b64-a789-4eb72dffd081.gif)

# Pre-requisites

## Tools

Required Installations:

* `sudo apt install python` or `brew install python` (tested on 3.10.10)
* `pip install openai`

Optional:

* `sudo apt install xclip`

## OpenAI API key

1. go to <https://platform.openai.com/account/api-keys> and generate an API key
2. create a file called `.openai-key` and place it in a folder called `keys` the root directory of the project.
i.e `keys/.openai-key`

Note: You may need to provide your billing details for the openAI API to allow your
requests. You can set a maximum dollar spend amount limit to something you can
live with. 😄💸

# Instructions

## Step 1: For Everyone

Modify the constants found at the top of `main.py` file to your specific needs.

```python
# keys folder in the root of the project with the api key in a file named `.openai-key`
API_KEY_LOCATION = Path("keys") / ".openai-key"
OS_VERSION = "ubuntu 20.04 running on wsl2"
SHELL_TYPE = "bash"
```

## Step 2: Depending on your Shell, OS and System

### Bash on WSL2

1. Add the snippet below to your `~./.bashrc` file and update the path to your
   python script location mine is `~/.my_toolbox/chatgpt-cli-helper/src/main.py`

```bash
function ai() {
    local ai_cmd=$(python ~/.my_toolbox/chatgpt-cli-helper/src/main.py "$1")
    echo "$ai_cmd"                                     # print the selected command
    # optionally:
    # For bash on wsl2 with access to windows executables
    # local ai_cmd=$(python ~/.my_toolbox/chatgpt-cli-helper/src/main.py "$1" | clip.exe) # copy the command to clipboard
    # printf "\033[G\033[K%s" "$ai_cmd"                  # place the command on the command line buffer
}
```

> IMPORTANT:  
> Remember to relaunch your shell for changes to take effect or do `source ~/.bashrc`
