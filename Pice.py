class Родительский:
    head = True
    def __init__(self):
        self.about()


class Дочерний(Родительский):
    def about(self):
        print("я студент")


