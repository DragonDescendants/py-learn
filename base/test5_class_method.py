def greet():
    print("你好")


class Monkey:
    def __init__(self, name):
        self.name = name
        print("monkey,up!")

    def hello(self):
        print("monkey" + self.name + "来了")

    def bye(self):
        print("monkey" + self.name + "走了")


greet()
m = Monkey("God")
m.hello()
m.bye()
