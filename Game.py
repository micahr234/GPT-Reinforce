class Game:
    def __init__(self):
        self.state = "start"
        self.end = False
        self.reward = 0

    def start(self):
        self.state = "You find yourself at the entrance of a mysterious dungeon."
        return "Objective: Explore the dungeon, find the treasure, and exit safely.\n" + self.state

    def step(self, action):
        if self.state.startswith("You find yourself"):
            return self.enter_dungeon(action)
        elif self.state.startswith("You are in a room"):
            return self.choose_path(action)
        elif self.state.startswith("Congratulations"):
            self.end = True
            return self.state, self.reward, self.end
        else:
            return "Invalid state.", 0, self.end

    def enter_dungeon(self, action):
        if action.lower() == "enter":
            self.state = "You are in a room with two doors. One leads left, the other right."
            return self.state, self.reward, self.end
        else:
            return 'Please choose a valid action: "Enter"', 0, self.end

    def choose_path(self, action):
        if action.lower() == "left":
            self.state = "You find a room filled with gold! You take some and proceed."
            self.reward += 100
            self.state += " Another door appears, leading outside."
            return self.state, self.reward, self.end
        elif action.lower() == "right":
            self.state = "A trap! You narrowly escape with minor injuries."
            self.reward -= 50
            return self.state, self.reward, self.end
        elif action.lower() == "proceed":
            self.state = "Congratulations! You've made it out alive with your treasure."
            self.end = True
            return self.state, self.reward, self.end
        else:
            valid_actions = '"Left", "Right", or "Proceed"' if "Another door appears" in self.state else '"Left" or "Right"'
            return f'Please choose a valid action: {valid_actions}', 0, self.end
