class Angel:
    color = "white"
    feature = "wings"
    home = "Heaven"


class Demon:
    color = "red"
    feature = "horns"
    home = "Hell"


# print(Angel.color, Angel.feature, Angel.home, sep = "\n")
# print(Demon.color, Demon.feature, Demon.home, sep = "\n")

objects = [Angel(), Demon()]
for object_ in objects:
    print(object_.color)
    print(object_.feature)
    print(object_.home)