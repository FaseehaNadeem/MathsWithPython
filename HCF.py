def find_hcf():
  
  import sys
  numbers = input("Enter the number:- ") # ("28 16")
  string_list = numbers.split() # split => ("28") ("16")
  numbers_list = [] # empty list
  count1 = 0
  for num in string_list:
    count1 += 1
    numbers_list.append(int(num)) # convert ("28") ("16") into (28) (16)
  if len(numbers_list) != 2:
    sys.exit("Enter only two numbers")
  a = numbers_list[0] # a = 28
  b = numbers_list[1] # b = 16
  if numbers_list[0] > numbers_list[1]:
    a = numbers_list[0]
    b = numbers_list[1]
  else:
    a = numbers_list[1]
    b = numbers_list[0]
  count2 = 0
  while b != 0:
    count2 += 1
    # By euclidean algorithm
    temp = a % b  #  divident // divisior -- 28 // 16 then remainder = 12
    # old divisior become divident (and) new divisor become remainder
    a =  b # a = 16
    b = temp  # b = 12
    if b == 0: # if b becomes 0 means remainder == 0
      break # loop breaks
  print("The HCF is",a)
  print("The for loop iteration",count1)
  print("The while loop iteration",count2)

find_hcf()



'''
Explanation:

1. First line asks the user to input two numbers separated by a space (for example, "28 16").
The input will be stored as a string.

2. Then split() method splits the input string by spaces into a list of substrings. 
   For example, "28 16" becomes ["28", "16"].

3. numbers_list = []
This initializes an empty list numbers_list that will store the converted integers.

4. Then loop iterates over each element in the string_list (which contains the numbers as strings).
Converts each string in string_list to an integer and appends it to numbers_list.
 For example, "28" becomes 28, and "16" becomes 16.

5. if len(numbers_list) != 2:
Checks if the numbers_list does not contain exactly two numbers
 (i.e., if the user has entered anything other than two numbers).
sys.exit("Enter only two numbers")
If the condition in the previous step is true, it exits the program with the message 
"Enter only two numbers."


6. Sets a to the first number in the list (e.g., 28).
   Sets b to the second number in the list (e.g., 16).

7. if numbers_list[0] > numbers_list[1]:
This checks if the first number first is greater than the second number.
If the first number is greater, it assigns a to the first number.
If the first number is greater, it assigns b to the second number.
This block will execute if the second number is greater than or equal to the first.

If the second number is greater, it assigns a to the second number.
It assigns b to the first number.

8. while b != 0:
Starts a while loop that continues until b becomes zero.
This loop is part of the Euclidean algorithm for finding the HCF.
temp = a % b
This calculates the remainder when a is divided by b (i.e., the modulus). This remainder is stored in temp.
a = b
The old divisor b becomes the new dividend a.
b = temp
The remainder (temp) becomes the new divisor b.
if b == 0:
This checks if the divisor b has become zero.
break

'''