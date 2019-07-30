var : int 

def add(y) :
    var = 100
    return var + y

if __name__ == "__main__" :
    print(add(5))
    print(globals()['var'])