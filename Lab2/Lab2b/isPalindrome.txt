def isPalindrome():
    Word = input('insert a string: ')
    str = Word[::-1]
    if Word[0] == Word[(len(Word)-1)] and Word[1:(len(Word)-2)] == str[1:(len(Word)-2)]:

            print "This is a Palindrome"
            return True
    else:
        print "This is not a Palindrome"
        return False
        
