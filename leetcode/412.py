class Solution:
    def fizzBuzz(self, n):
        my_list = []
        
        for num in range(1, n + 1):
            my_string = ""
            
            if(num % 3 != 0 and num % 5 != 0):
                my_string = str(num)
                
            if num % 3 == 0:
                my_string = my_string + "Fizz"
                
            if num % 5 == 0:
                my_string = my_string + "Buzz"
            
            my_list.append(my_string)
               
        return my_list