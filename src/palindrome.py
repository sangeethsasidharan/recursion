
class Palindrome:
    def palindrome(self, word):
        return self.check_palindrome(word)

    def check_palindrome(self, word):
        # base condition if 1 char return true
        if len(word) == 1:
            return True
        # base condition if 2  ,if matching return true else false
        if len(word) == 2:
            return word[0] == word[1]

        # smallest work on call, 1st and last char checked if true recursively call remaining word
        if word[0] == word[-1]:
            return self.check_palindrome(word[1:-1])
        else:
            return False


obj = Palindrome()
print(obj.palindrome('malayalam'))
