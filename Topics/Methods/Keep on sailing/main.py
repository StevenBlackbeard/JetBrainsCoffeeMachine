# our class Ship
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    # the old sail method that you need to rewrite
    def sail(self, destination):
        return f'The {self.name} has sailed for {destination}!'


black_pearl = Ship("Black Pearl", 800)
print(black_pearl.sail(input()))

# # our class Ship
# class Ship:
#     def __init__(self, name, capacity, dest):
#         self.name = name
#         self.capacity = capacity
#         self.cargo = 0
#         self.dest = dest
#
#     def sail(self):
#         print("The {0} has sailed for {1}!".format(self.name, self.dest))
#
#
# black_pearl = Ship("Black Pearl", 800, input())
# black_pearl.sail()
