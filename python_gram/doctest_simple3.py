
from typing import TypeVar, Iterable, Tuple

T = TypeVar('T', int, float, complex)
Vector = Iterable[Tuple[T, T]]

def inproduct(v: Vector[T]) -> T:
    """
       >>> inproduct([(1,2)])
       2
    """
    return sum(x*y for x, y in v)