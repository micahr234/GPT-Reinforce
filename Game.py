class Game:
    def __init__(self):
        self.game_running = True
        self.location = "Start"
        self.inventory = []
        self.reward = 0

    def start_game(self):
        message = "Welcome to the adventure game!"
        message += "\n" + self.describe_location()
        message += "\n" + self.available_actions()
        return message

    def step_game(self, action):
        if not self.game_running:
            return "The game has already ended. Please restart to play again."

        self.last_action = action.lower().strip()

        if self.last_action == "quit":
            self.game_running = False
            return "Thanks for playing!"

        action_response = self.process_action(self.last_action)
        game_over_message, is_game_over = self.check_game_over()

        if is_game_over:
            self.game_running = False
            return f"{action_response}\n{game_over_message} Your reward is {self.reward} points. The adventure ends here."

        return action_response + "\n" + self.describe_location() + "\n" + self.available_actions()

    def describe_location(self):
        descriptions = {
            "Start": "You are at the beginning of a dark forest. Paths lead to the north and east.",
            "North": "You are in a clearing, with paths leading south and east.",
            "East": "You find yourself by a calm lake. There's a path leading west."
        }
        return descriptions.get(self.location, "Unknown location!")

    def available_actions(self):
        if self.location == "Start":
            return "Available actions: 'north', 'east', 'quit'"
        elif self.location == "North":
            return "Available actions: 'south', 'east', 'quit'"
        elif self.location == "East":
            return "Available actions: 'west', 'quit'"
        return "Available actions: 'quit'"

    def process_action(self, action):
        moves = {
            "north": ("North", "Start"),
            "south": ("Start", "North"),
            "east": ("East", "North"),
            "west": ("Start", "East")
        }

        if action in moves and (self.location == moves[action][1]):
            self.location = moves[action][0]
            return f"You move {action}."
        return "You can't go that way!"

    def check_game_over(self):
        if self.location == "North":
            self.reward -= 50
            return ("Oh no, a monster appears! You've been eaten.", True)
        elif self.location == "East" and "key" not in self.inventory:
            self.inventory.append("key")
            self.reward += 100
            return ("You find a shimmering key under the water and pick it up.", True)
        return ("", False)
