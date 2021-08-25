

class StringReversal():
    def reverse_string(self, str):
        return self.calculate_reverse(str)

    def calculate_reverse(self, str):
        if len(str) == 1:
            return str

        return self.calculate_reverse(str[1:]) + str[0]


obj = StringReversal()
print(obj.reverse_string('sangeeth'))
