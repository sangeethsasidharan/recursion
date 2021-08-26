

class DecimalToBinary:
    def to_binary(self, number):
        return int(self.calculate_binary(number))

    def calculate_binary(self, number):

        if number // 2 == 0:
            return str(number % 2)

        return self.calculate_binary(number//2) + str(number % 2)


obj = DecimalToBinary()
print(obj.to_binary(12322))
