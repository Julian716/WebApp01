import random
class Suerte:
    def __init__(self, number1, number2, number3):
        self.number1 = number1
        self.number2 = number2
        self.number3 = number3

    def ganador(self) -> bool:
        number = random.randint(1, 100)
        if str(number) in [self.number1, self.number2, self.number3]:
            return True
        return False