import LLM
import Game

messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user", "content": "Where was it played?"}
        ]

if __name__ == '__main__':
    llm = LLM.LLM(api_key="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")
    game = Game.Game()
    prompt = ("\n\nYour task is to play a text based computer game. The goal it to find out how to obtain\n"
              " the highest reward by playing the game multiple times. Do NOT talk to the computer as\n"
              " if it where a person. Choose the action exactly as specified. Try all options\n"
              " as that will help you explore the game. Good luck.\n\n")
    prompt = prompt + str(game.start_game()) + "\n"
    while True:
        prompt = prompt + "What do you want to do?\n"
        print(prompt)
        user_action = str(llm.query(prompt))
        print(user_action)
        prompt = str(game.step_game(user_action)) + "\n"
        input()
        if not game.game_running:
            prompt = prompt + ("The game is over.\n\n")
            prompt = prompt + ("The game will restart.\n\n")
            game = Game.Game()
            prompt = prompt + str(game.start_game()) + "\n"
