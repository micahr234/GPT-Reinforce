import LLM
from colorama import Fore, Back, Style
import os

if __name__ == '__main__':
    llm = LLM.LLM(api_key=os.getenv("OPENAI_API_KEY"))

    context = "You are an assistant coder."
    llm.add_context(context)
    print(Fore.YELLOW + context + Style.RESET_ALL)

    user_input = (
        "Create a text based game in python code. Start the game by stating the objective. "
        "At each step tell the player what actions are possible and ask the player to choose the next action. "
        "When the player chooses an action, tell them what reward (if any) they will receive and what the next state of the "
        "game is. If the player chooses an invalid action ask them to choose a valid action and list all valid actions in quotes. "
        "If the player continues to choose invalid actions the game should terminate. "
        "Do not generate comments or examples, only generate code."
        "\n"
        "\n"
        "```python\n"
        "# Example of how to play the game\n"
        "game = Game()\n"
        "state = game.start() #string\n"
        "# Example introductions:\n"
        "# Welcome to the adventure! Here is how to play ... the available actions are 'enter' OR 'run'\n"
        "# A bear is chasing you find out how to escape. You can 'run' or 'clime' a tree.\n"
        "print(state)\n"
        "\n"
        "while True:\n"
        "\tuser_input = input()\n"
        "\tstate, reward, end = game.step(user_input) #string, string, bool\n"
        "\t# Example rewards:\n"
        "\t# You get 100 points\n"
        "\t# You get -1 points\n"
        "\t# You won\n"
        "\t# You lost\n"
        "\tprint(reward)\n"
        "\t# Example states:\n"
        "\t# You are now at the cave, what do you want to do? 'explore' or 'leave'\n"
        "\t# A lion is chasing you, you can 'run' or 'fight'.\n"
        "\t# You fell off the tower into the moat, 'swim' or 'dive'?\n"
        "\t# Invalid action choose 'left' or 'right'.\n"
        "\tprint(state)\n"
        "\tif end:\n"
        "\t\tbreak\n"
        "```"
    )
    llm.add(user_input)
    print(Fore.GREEN + user_input + Style.RESET_ALL)

    while True:
        llm_output = llm.reply()
        print(Fore.BLUE + llm_output + Style.RESET_ALL)

        user_input = input()
        llm.add(user_input)
