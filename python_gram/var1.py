import typing

def add(x:typing.Generic, y:typing.Generic) :
    """
       >>> add(10,10)
       20
       >>> add("Hello", "World")
       'HelloWorld'
       >>> add("Hello",10)
       Traceback (most recent call last):
       ...
       TypeError: must be str, not int
    """
    return x+y