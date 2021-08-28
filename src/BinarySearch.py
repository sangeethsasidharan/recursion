
class BinarySearch:
    def binary_search(self, search_lis, ele):
        return self.find_binary_search(search_lis, ele, 0, len(search_lis)-1)

    def find_binary_search(self, search_lis, ele, lef, righ):

        mid = (lef + righ) // 2
        if lef > righ:
            return -1
        if search_lis[mid] == ele:
            return mid

        if ele<search_lis[mid]:
            return self.find_binary_search(search_lis, ele, lef, mid)
        else:
            return self.find_binary_search(search_lis, ele, mid+1, righ)


obj = BinarySearch()
print(obj.binary_search([1,2,3,4,5],3))

