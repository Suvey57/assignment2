# class py_solution:
#    def is_valid_parenthese(self, str1):
#         stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
#         for parenthese in str1:
#             if parenthese in pchar:
#                 stack.append(parenthese)
#             elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
#                 return False
#         return len(stack) == 0

# print(py_solution().is_valid_parenthese("(){}[]"))
# print(py_solution().is_valid_parenthese("()[{)}"))
# print(py_solution().is_valid_parenthese("()"))
open_list = ["[","{","("] 
close_list = ["]","}",")"] 
  
# Function to check parentheses 
def check(myStr): 
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "Unbalanced"
    if len(stack) == 0: 
        return "Balanced"
    else: 
        return "Unbalanced"
  
string = input("enter format of perenthesis to be checked if it is balanced or not::")
print(string,"-", check(string)) 
  
