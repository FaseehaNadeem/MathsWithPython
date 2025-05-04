def Find_Lcm():

  numbers = input("Enter the number:- ") # user give input in string
  string_list = numbers.split()  # it split the string
  numbers_list = []  # empty list is created
  count1 = 0
  for num in string_list: # list that convert split strings => integar onebyone
    count1 += 1
    numbers_list.append(int(num))  # .append insert the numbers into empty list
  lcm = numbers_list[0] # initialize first number as lcm
  count2 = 0
  total_count3 = 0
  for num in numbers_list[1:]: # list than start from second number to last
    count2 += 1
    # FIND GCD
    #  Using Eculidean Algorithm

    temp_num = num # real_num
    temp_lcm = lcm # real_lcm
    count3 = 0
    while True:
      count3 += 1
      remainder = lcm % num # divide two numbers and store remainder
      lcm = num            # formula: a,b= b,remainder
      num = remainder
      if num == 0:
        gcd = lcm
        # FIND LCM
        LCM = (temp_lcm * temp_num) // gcd
        print("The LCM of numbers are:-",LCM)
        break
    total_count3 += count3


  print("The first for loop iterations",count1)
  print("The second for loop iterations",count2)
  print("Total while loop iterations",total_count3)

Find_Lcm()



'''
Explanation: 
1. User Input: The user enter numbers as a string. For example, "4 6 8". 
2. Splitting the Input: The input string is split into a list of numbers. 
    If the user entered "4 6 8", it becomes ['4', '6', '8'].
3. Empty List: An empty list numbers_list is created to store the numbers in integer form.
4. Converting Strings to Integers: Then loop goes through each item in string_list 
    and converts it to an integer.
    Appending to List: Each number is converted to an integer and added to the numbers_list.
5. Initialize LCM: The first number from the list is initialized as the starting LCM.
6. Loop Through Remaining Numbers: Then second loop starts from the second number in the list 
    and goes to the last one, to calculate LCM for all numbers.
7. Store Temporary Values: temp_num stores the current number being processed, 
    and temp_lcm stores the current LCM.
8. While Loop: The while loop is used to implement
   the Euclidean Algorithm to find the GCD (Greatest Common Divisor) of two numbers.
9. Find Remainder: The remainder of dividing lcm by num is calculated using the modulus operator (%).
10. Update LCM: The value of lcm is updated to the current num.
11. Update num: The value of num is updated to the remainder.
12. Check if Remainder is Zero: If num becomes zero, it means the GCD has been found
13. GCD Found: The GCD is set to the value of lcm.
14. LCM Calculation: The LCM is calculated using the formula.
15. count1,count2,count3 i used to count the iterations.
 
'''