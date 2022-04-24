

class ParentClass:

    def __init__(self, fullname):
        self.fullname = fullname

    def get_first_name(self):
        return self.fullname.split(" ")[0]

    def hey(self):
        print(f"Hello {self.get_first_name()}")


class ChildClass(ParentClass):

    def __init__(self, fullname, age=None):
        super().__init__(fullname)
        self.age = age

    def hey(self):
        if self.age and self.age < 18:
            print(f"What's up {self.get_first_name()}?")
        else:
            super().hey()


if __name__ == "__main__":

    fullname = "Alfredo Topete Escamilla"

    a = ParentClass(fullname)
    b = ChildClass(fullname)
    c = ChildClass(fullname, 14)

    a.hey()
    b.hey()
    c.hey()
