class AccessModifiers():
    def __init__(self, publicInstanceVariable, protectedInstanceVariable, privateInstanceVariable):
         self.publicInstanceVariable = publicInstanceVariable
        self.protectedInstanceVariable = protectedInstanceVariable
        self.privateInstanceVariable = privateInstanceVariable

    def __privateInstanceMethod(self) -> int:
        odd_add = True
        even_add = False
        final_even_number = 0
        final_odd_number = 0
        
        for value in self.privateInstanceVariable:
            if type(value) == int:
                if value % 2 == 0:
                    if even_add:
                        final_even_number += value
                        even_add = False
                    else:
                        final_even_number -= value
                        even_add = True
                elif value % 2 == 1:
                    if odd_add:
                        final_odd_number += value
                        odd_add = False
                    else:
                        final_odd_number -= value
                        odd_add = True
        
        return final_even_number * final_odd_number
    

    def publicInstanceMethod(self) -> tuple:
        palindromes = [string for string in self.publicInstanceVariable if AccessModifiers.check_palindrome(string)]
        anagrams = [item for item in self.protectedInstanceVariable if AccessModifiers.check_anagram(item)]
        return (palindromes, anagrams, self.__privateInstanceMethod())            
            
    
