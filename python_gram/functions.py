def add(x,y) :
    print("namespace")
    return x+y

print(globals()['add'])
print(globals()['add'](10,20))