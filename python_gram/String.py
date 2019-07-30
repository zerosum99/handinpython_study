from typing import TypeVar

AnyStr = TypeVar('AnyStr', str, bytes)

def concat(a: AnyStr, b: AnyStr) -> AnyStr:
    """
    >>> concat("foo", "bar")
    'foobar'
    >>> concat(b"foo", b"bar")
    b'foobar'
    >>> concat("foo", b"bar")
    Traceback (most recent call last):
       ...
    TypeError: must be str, not bytes
    """
    
    return a + b