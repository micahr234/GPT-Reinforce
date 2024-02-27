import LLM
from colorama import Fore, Back, Style

if __name__ == '__main__':
    llm = LLM.LLM(api_key="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")

    context = "You are an assistant coder."
    llm.add_context(context)
    print(Fore.YELLOW + context + Style.RESET_ALL)

    user_input = (
        "Create a text based game in python code. Start the game by stating the objective. "
        "At each step tell the player what actions are possible and ask the player to choose the next action. "
        "When the player chooses an action, tell them what reward (if any) they will receive and what the next state of the "
        "game is. If the player chooses an invalid action ask them to choose a valid action and list all valid actions in quotes. "
        "Do not generate comments or examples, only generate code."
        "\n"
        "\n"
        "```python\n"
        "# Example of how to play the game\n"
        "game = Game()\n"
        "state = game.start()\n"
        "print(state)\n"
        "\n"
        "while True:\n"
        "\tuser_input = input()\n"
        "\tstate, reward, end = game.step(user_input)\n"
        "\tprint(state)\n"
        "\tprint(reward)\n"
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
