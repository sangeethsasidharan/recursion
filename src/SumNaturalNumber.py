

class SumOfNaturalNumber:
    def natural_number(self, n):
        return self.calculate_sum(n)

    def calculate_sum(self, n):
        if n == 0:
            return 0
        return self.calculate_sum(n-1)+n


obj = SumOfNaturalNumber()
print(obj.natural_number(10))
