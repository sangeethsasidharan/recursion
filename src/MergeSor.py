
class MergeSor:
    def ge_sored(self, random_lis):
        return self.devide(random_lis)

    def devide(self, random_lis):
        sored_li = []
        if len(random_lis) == 1:
            return random_lis
        righ = len(random_lis)-1
        mid = righ//2
        return self.sor(self.devide(random_lis[0:mid+1]), self.devide(random_lis[mid+1:]), sored_li)

    def sor(self, ran1, ran2, sored_li):
        if (len(ran1) == 0) | (len(ran2) == 0):
            return sored_li+ran1+ran2
        if ran1[0] < ran2[0]:
            sored_li.append(ran1[0])
            return self.sor(ran1[1:], ran2, sored_li)
        else:
            sored_li.append(ran2[0])
            return self.sor(ran1, ran2[1:], sored_li)







obj = MergeSor()
#un_sored_lis = [6,1,5,3,2]
un_sored_lis = [100,2,32,42,4,6,22,44]
print(obj.ge_sored(un_sored_lis))