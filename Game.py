class Game:
    def __init__(self):
        self.state = "start"
        self.actions = {
            "start": ["explore", "leave"],
            "forest": ["search", "rest"],
            "cave": ["fight", "flee"],
            "invalid": []
        }
        self.rewards = {
            "explore": 10,
            "leave": -5,
            "search": 20,
            "rest": 5,
            "fight": 30,
            "flee": -10
        }
        self.end_states = ["leave", "flee"]

    def start(self):
        return "Welcome to the adventure! You are at the entrance of a dark forest. Do you want to 'explore' it or 'leave'?"

    def step(self, action):
        if self.state in self.end_states:
            return "Game over", "You lost", True
        elif action not in self.actions.get(self.state, self.actions["invalid"]):
            self.state = "invalid"
            valid_actions = "', '".join(self.actions.get(self.state, []))
            return f"Invalid action choose '{valid_actions}'", "", False
        else:
            reward = self.rewards.get(action, 0)
            reward_msg = f"You get {reward} points"
            if action == "explore":
                self.state = "forest"
                next_state = "You are in a mystical forest. Do you want to 'search' for treasure or 'rest'?"
            elif action == "search":
                self.state = "cave"
                next_state = "You found a cave. Will you 'fight' the dragon or 'flee'?"
            elif action == "rest":
                return "Game over", "You won", True
            elif action == "fight":
                return "Game over", "You won", True
            elif action == "flee":
                return "Game over", "You lost", True
            elif action == "leave":
                return "Game over", "You lost", True
            else:
                next_state = "Invalid state"
                reward_msg = ""
            return next_state, reward_msg, False