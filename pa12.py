def isPalindrome(s): 
    return s == s[::-1] 
  
  
a=input("enter a string to check if it is palindrome or not::")
ans = isPalindrome(a) 
  
if ans: 
    print("Yes") 
else: 
    print("No")