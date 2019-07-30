
from typing import TypeVar, Iterable, Tuple

T = TypeVar('T', int, float, complex)
Vector = Iterable[Tuple[T, T]]

def inproduct(v: Vector[T]) -> T:
    """
       >>> inproduct([(1,2)])
       2
    """
    return sum(x*y for x, y in v)
def dilate(v: Vector[T], scale: T) -> Vector[T]:
    """
       >>> dilate([(1,2)],"a")
       2
    """
    return ((x * scale, y * scale) for x, y in v)