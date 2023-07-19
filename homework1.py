def Palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
    
print(Palindrome(input('Введите строку: ')))
