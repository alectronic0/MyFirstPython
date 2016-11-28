class MyClass:

    def __init__(self):
        self.age = "cake"

    def __init__(self, i):
        self.age = i
        self.mes = "Blah"

    def messageMe(self):
        print('This is a Message ' + self.mes + self.age)
