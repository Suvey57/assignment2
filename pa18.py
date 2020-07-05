import json 
  
# {key:value mapping} 
a ={"name":"John", 
   "age":31, 
    "Salary":25000} 
  
b = json.dumps(a)
print(b) 
print(json.loads(b))

  