class AC_agent:
    def __init__(self, desired_temp):
        self.desired_temp = desired_temp
        self.previous_action = None  

    def check_temperature(self, current_temp):
        if current_temp >= self.desired_temp:
            if self.previous_action != "Turn ON AC":
                self.previous_action = "Turn ON AC"
                return self.previous_action
            else:
                return "Already Exists"
        else:
            if self.previous_action != "Turn OFF AC":
                self.previous_action = "Turn OFF AC"
                return self.previous_action
            else:
                return "Already Exists"


rooms = {
    "Parents Room": 18,
    "Drawing Room": 22,
    "Gaming Room": 20,
    "Brother Room": 24
}

agent = AC_agent(22)

for room, temp in rooms.items():
    action = agent.check_temperature(temp)
    print(f"{room} → Temp {temp}°C => {action}")
