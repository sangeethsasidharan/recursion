import datetime

class Fibinosky:
    def fibinosky_series(self, n):
        return self.fibonisky_lis(n, [])

    def find_fibinosky_series(self, n):
        if (n == 0) | (n == 1):
            return n

        return self.find_fibinosky_series(n-1) + self.find_fibinosky_series(n-2)

    def fibonisky_lis(self, n, resul):
        if n < 0:
            return resul
        d1 = datetime.datetime.now()
        self.fibonisky_lis(n-1, resul)
        resul.append(self.find_fibinosky_series(n))
        d2 = datetime.datetime.now()
        print((d2 - d1), len(resul), resul)
        return resul


obj = Fibinosky()

print(obj.fibinosky_series(100))


