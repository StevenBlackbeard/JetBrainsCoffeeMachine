class Coffee:
    def __init__(self):
        self.action = None
        self.action_buy = None
        self.supplies = {
            'water': 400,
            'milk': 540,
            'coffee beans': 120,
            'disposable cups': 9,
            'money': 550
        }
        self.amounts = {1: {"water": -250, "milk": -0, "coffee beans": -16, "disposable cups": -1, "money": 4},
                        2: {"water": -350, "milk": -75, "coffee beans": -20, "disposable cups": -1, "money": 7},
                        3: {"water": -200, "milk": -100, "coffee beans": -12, "disposable cups": -1, "money": 6}}

    def remaining(self):
        print(f'''
The coffee machine has:
{self.supplies["water"]} ml of water
{self.supplies["milk"]} ml of milk
{self.supplies["coffee beans"]} g of coffee beans
{self.supplies["disposable cups"]} disposable cups
${self.supplies["money"]} of money
        ''')

    def fill(self):
        self.supplies["water"] += int(input("Write how many ml of water you want to add:"))
        self.supplies["milk"] += int(input("Write how many ml of milk you want to add:"))
        self.supplies["coffee beans"] += int(input("Write how many grams of coffee beans you want to add:"))
        self.supplies["disposable cups"] += int(input("Write how many disposable cups of coffee you want to add:"))

    def take(self):
        print(f'I gave you ${self.supplies["money"]}')
        self.supplies["money"] = 0

    def check(self):
        check = {}
        for key in [key for key in self.supplies.keys() if key not in "money"]:
            check[key] = self.supplies[key] > -self.amounts[self.action_buy][key]
        return check

    def buy(self):
        self.action_buy = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if self.action_buy != "back":
            self.action_buy = int(self.action_buy)
            check_vals = self.check()
            if all(check_vals.values()):
                print("I have enough resources, making you a coffee!")
                for key, value in self.amounts[self.action_buy].items():
                    self.supplies[key] += value
            else:
                not_enough = "".join([key for key, value in check_vals.items() if value == False])
                print(f'Sorry, not enough {not_enough}!')

    def take_action(self):
        while True:
            self.action = input("Write action (buy, fill, take, remaining, exit):")
            print()
            if self.action == "take":
                self.take()
                continue
            if self.action == "remaining":
                self.remaining()
                continue
            if self.action == "buy":
                self.buy()
                continue
            elif self.action == "fill":
                self.fill()
            else:
                break

test = Coffee()
test.take_action()
