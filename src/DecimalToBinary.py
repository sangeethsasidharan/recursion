
class DecimalToBinary:
    def to_binary(self, number):
        result = ''
        return int(self.calculate_binary(number, result))

    def calculate_binary(self, number, result):
        if number == 0:
            return result
        result = str(number % 2) + result

        return self.calculate_binary(number//2, result)


obj = DecimalToBinary()
print(obj.to_binary(12))
