class MyClass():
    def __init__(self):
        #Initialise class variable
        self.var1 = "Variable 1"

    def my_function(self):
        #Initialise local class variable
        self.var2 = "Variable 2"

    def my_function2(self):
        #Attempt to access local variable from within class
        print(self.var2)


if __name__ == '__main__':
    #Initialise class
    my_class = MyClass()

    #Access class variable
    print(my_class.var1)

    #Access local class variable
    try:
        print(my_class.var2)
    except:
        print("AttributeError")

    #Try to access local class variable within class function
    try:
        my_class.my_function2()
    except:
        print("AttributeError")

