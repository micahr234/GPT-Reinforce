import LLM


if __name__ == '__main__':
    llm = LLM.LLM(api_key="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")
    llm.add_context("You are a chatbot. Introduce yourself and help the user.")
    while True:
        llm_reply = llm.reply()
        print("LLM:\n", llm_reply, "\n")
        user_input = input("User: \n")
        print("\n")
        llm.add(user_input)
