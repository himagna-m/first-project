from typing import List, Tuple, NewType, Callable, TypeVar, Generic, Protocol, Final

# 1. Type Alias
Vector = List[int]

def double_vector(v: Vector) -> Vector:
    return [x * 2 for x in v]

# 2. NewType
UserId = NewType("UserId", int)

def get_user_info(user_id: UserId) -> str:
    return f"User ID: {user_id}"

# 3. Callable
def operate(a: int, b: int, op: Callable[[int, int], int]) -> int:
    return op(a, b)

def add(x: int, y: int) -> int:
    return x + y

# 4. Generics with TypeVar
T = TypeVar("T")

class Box(Generic[T]):
    def __init__(self, item: T):
        self.item = item

    def get(self) -> T:
        return self.item

# 5. Tuple
Coordinates = Tuple[int, int]
location: Coordinates = (10, 20)

# 6. Protocol (structural subtyping)
class Flyer(Protocol):
    def fly(self) -> None: ...

class Bird:
    def fly(self) -> None:
        print("Bird flying!")

# 7. Constant (Final)
PI: Final = 3.14159

# --------- Run Everything Below ---------

# 1. Type alias usage
print("Double vector:", double_vector([1, 2, 3]))  # [2, 4, 6]

# 2. NewType usage
print(get_user_info(UserId(101)))

# 3. Callable usage
print("Sum using callable:", operate(5, 7, add))  # 12

# 4. Generics usage
int_box = Box (123)
str_box = Box("hello")
print("Box contents:", int_box.get(), str_box.get())

# 5. Tuple usage
print("Location coordinates:", location)

# 6. Protocol usage
parrot = Bird()
parrot.fly()

# 7. Final constant usage
print("Constant PI value:", PI)
