import LLM
import Game
from colorama import Fore, Back, Style

if __name__ == '__main__':
    llm = LLM.LLM(api_key="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")

    context = ("Your task is to play a text based computer game. Find out how to obtain the "
               "highest reward by playing the game multiple times. Do NOT talk to the computer "
               "as if it were a person, instead choose from the options given. Try different actions "
               "to explore the game.")
    llm.add_context(context)
    print(Fore.YELLOW + context + Style.RESET_ALL)

    while True:
        game = Game.Game()

        state = game.start()
        llm.add(state)
        print(Fore.GREEN + state + Style.RESET_ALL)

        while True:
            input()

            llm_output = llm.reply()
            print(Fore.BLUE + llm_output + Style.RESET_ALL)

            state, reward, end = game.step(llm_output)
            llm.add(state + str(reward))
            print(Fore.GREEN + state + str(reward) + Style.RESET_ALL)

            if end:
                break
