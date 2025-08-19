import LLM
import Game
from colorama import Fore, Back, Style

if __name__ == '__main__':
    llm = LLM.LLM(api_key=os.getenv("OPENAI_API_KEY"))

    context = ("Your task is to play a text based computer game. Find out how to obtain the "
               "highest reward by playing the game multiple times. Do NOT talk to the computer "
               "as if it were a person, instead choose from the options given. Try different actions "
               "to explore the game.")
    llm.add_context(context)
    print(Fore.YELLOW + context + Style.RESET_ALL)

    quit_playing = False
    while not quit_playing:
        game = Game.Game()

        state = game.start()
        llm.add(state)
        print(Fore.GREEN + state + Style.RESET_ALL)

        while True:
            supervisor_input = input("Press any key to continue or 'q' to quit")
            if supervisor_input == 'q':
                quit_playing = True
                break

            llm_output = llm.reply()
            print(Fore.BLUE + llm_output + Style.RESET_ALL)

            state, reward, end = game.step(llm_output)
            llm.add(reward)
            llm.add(state)
            print(Fore.GREEN + reward + Style.RESET_ALL)
            print(Fore.GREEN + state + Style.RESET_ALL)
            if end:
                break

    context = "Now that you have experience playing. Summarize how to get the highest reward."
    llm.add_context(context)
    print(Fore.YELLOW + context + Style.RESET_ALL)

    llm_output = llm.reply()
    print(Fore.BLUE + llm_output + Style.RESET_ALL)
