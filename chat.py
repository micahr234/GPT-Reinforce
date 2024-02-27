import LLM
from colorama import Fore, Back, Style

if __name__ == '__main__':
    llm = LLM.LLM(api_key="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")

    context = "You are a chatbot. Introduce yourself and help the user."
    llm.add_context(context)
    print(Fore.YELLOW + context + Style.RESET_ALL)

    while True:
        llm_output = llm.reply()
        print(Fore.BLUE + llm_output + Style.RESET_ALL)

        user_input = input()
        llm.add(user_input)
