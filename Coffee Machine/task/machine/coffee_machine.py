import math

avail_water = int(input("Write how many ml of water the coffee machine has:"))
avail_milk = int(input("Write how many ml of milk the coffee machine has:"))
avail_beans = int(input("Write how many grams of coffee beans the coffee machine has:"))
cups = int(input("Write how many cups of coffee you will need:"))
# water = cups * 200
# milk = cups * 50
# beans = cups * 15
avail_cups = min(
    math.floor(avail_water / 200),
    math.floor(avail_milk / 50),
    math.floor(avail_beans / 15)
)
if cups == avail_cups:
    print("Yes, I can make that amount of coffee")
elif cups > avail_cups:
    print(f'No, I can make only {avail_cups} cups of coffee')
else:
    print(f'Yes, I can make that amount of coffee (and even {avail_cups - cups} more than that)')
# print(f'For {cups} cups of coffee you will need:')
# print(f'{water} ml of water\n{milk} ml of milk\n{beans} g of coffee beans')
