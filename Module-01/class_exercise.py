
# !Question 1 
# *Given an array of numbers, write a function that prints in the console another array which contains all the even numbers in the original array, which also have even indexes only.
#       ○ Test 1: getOnlyEvens([1, 2, 3, 6, 4, 8]) prints [ 4]
#       ○ Test 2: getOnlyEvens([0, 1, 2, 3, 4]) prints [0, 2, 4]

# ?Requirement: function must print only even numbers from a given array but the chosen numbers must also have even indexes which means only even numbers with even indexes get printed  so index % 2 == 0 and number % 2 == 0

def getOnlyEvens(arr):
     result = []
     for index in range(len(arr)):
          number = arr[index]
          if index % 2 == 0 and number % 2 == 0:
               result.append(number)
          else:
               continue
               
     print(result)

getOnlyEvens([1, 2, 3, 6, 4, 8])
getOnlyEvens([0, 1, 2, 3, 4])
getOnlyEvens([22, 26, 34, 67, 80, 11, 34, 64, 99, 32, 48, 71, 65])


# !Question 2
# *Create a function that takes a two-digit number as an parameter and prints "Ok" in the console if the given string is greater than its reversed digit version. If not, the function will print "Not ok"
#      ○ Test 1: reverseCompare(72) prints "ok" because 72 > 27
#      ○ Test 2: reverseCompare(23) prints "Not ok", because 23 is not greater than 32
# ? Requirements: 2 digit input, input > reversed version = "ok" and if input < reversed = "not okay"
def reverseCompare(num):
     first_digit = num // 10 
     second_digit = num % 2 
     for reversed_number:
          return 
     if num > reversed_number:
          print("Ok")
     else:
          print("Not ok")


# !Question 3
# * Write a function that takes a positive integer and returns the factorial of the number. Notes: The factorial of 0 is 1. Ex: factorial seven is : 1 × 2 × 3 × 4 × 5 × 6 × 7. The factorial of any positive integer x is x * (x - 1) * (x - 2) * . . . . . . * 1 (ex: factorial of 4 is 4 * 3 * 2 * 1 = 24)
#     ○ Test 1: returnFactorial(5) outputs 120
#     ○ Test 2: returnFactorial(6) outputs 720
#     ○ Test 3: returnFactorial(0) outputs 1

def returnFactorial(x): ...


# !Question 4 (Meera array)
# * A Meera array is defined to be an array containing only numbers as its elements and forall n numbers in the array, the number n*2 is not in the array. So [3, 5, -2] is a Meera array because 3*2, 5*2 or 2*2 are not in the array. But [8, 3, 4] is not a Meera array because 2*4=8 and both 4 and 8 are elements found in the array. Write a function that takes an array of numbered elements and prints “I am a Meera array” in the console if its array does NOT contain n and also n*2 as number. Otherwise, the function prints “I am NOT a Meera array”
#       ○ Test 1: checkMeera([10, 4, 0, 5]) outputs “I am NOT a Meera array” because 5 * 2 is 10
#       ○ Test 2: checkMeera([7, 4, 9]) outputs “I am a Meera array”
#       ○ Test 1: checkMeera([1, -6, 4, -3]) outputs “I am NOT a Meera array” because -3 *2 is -6 

def checkMeera(arr): ...

# !Question 5 (Dual array)
# * Define a Dual array to be an array where every number occurs exactly twice. For example, {1, 2, 1, 3, 3, 2} is a dual array.The following arrays are not Dual arrays {2, 5, 2, 5, 5} (5 occurs three times instead of two times) {3, 1, 1, 2, 2} (3 occurs once instead of two times) Write a function named isDual that returns 1 if its array argument is a Dual array. Otherwise it returns 0.

def isDual(arr): ...

# !Question 6
# * Write a function that takes the number of seconds and returns the digital format clock time as a string. Time should be counted from 00:00:00.
#       ○ Examples: digitalClock(5025) as "01:23:45" 5025 seconds is 1 hour, 23 mins, 45secs.
#       ■ digitalClock(61201) as "17:00:01" No AM/PM. 24h format.
#       ■ digitalClock(87000) as "00:10:00" It's 00:10 next day.

def digitalClock(): ...