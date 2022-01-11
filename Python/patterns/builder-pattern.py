class MyBuilder():
    def __init__(self):
        self.house = ""

    def colour(self, colour: str):
        self.house += colour
        return self

    def windows(self, number: int):
        string = " has " + str(number) + " windows"
        self.house += string
        return self

    def doors(self, number: int):
        string = " has " + str(number) + " doors"
        self.house += string
        return self

    def build(self):
        return self.house


if __name__ == '__main__':
    builder = MyBuilder()
    print(builder.colour("Brown").doors(2).windows(4).build())
