
glb_var = 100

def add(x,y) :
    print(locals())
    print("globals ",add.__globals__["glb_var"])
    return x+y

print(add.__module__)
print(add.__globals__["add"])