def change_snake_case(str): 
    res = [str[0].lower()] 
    for c in str[1:]: 
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'): 
            res.append('_') 
            res.append(c.lower()) 
        else: 
            res.append(c) 
      
    return ''.join(res)

def changekebabcase(str): 
    res = [str[0].lower()] 
    for c in str[1:]: 
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'): 
            res.append('-') 
            res.append(c.lower()) 
        else: 
            res.append(c) 
      
    return ''.join(res) 
      

a=input("enter a string in camel case::")

print("the output in snake_case is::",change_snake_case(a)) 
print("the output in kebab-case is::",changekebabcase(a)) 