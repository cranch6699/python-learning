from typing import List

def average(grades: List[int]) -> float:
    return sum(grades) / len(grades)

print(average([90, 80, 100]))  # Output: 90.0

from typing import Optional

def greet(name: Optional[str] = None) -> str:
    if name:
        return f"Hello, {name}"
    return "Hello, Guest"

print(greet())

from typing import List, Dict

def average2(grades: List[int]) -> float:
    return sum(grades) / len(grades)

def format_user(user: Dict[str, str]) -> str:
    return f"{user['name']} <{user['email']}>"

print(
    average2([10,20,30]),
    format_user({'name':'Name 1', 'email':'Name 2'})  
    )

from typing import TypedDict

class User(TypedDict):
    name: str
    email: str
    
from typing import TypedDict

class User2(TypedDict):
    name: str
    email: str
    age: int

def format_user_2(user: User2) -> str:
    return f"{user['name']} ({user['age']}) <{user['email']}>"

u = {"name": "Alice", "email": "alice@example.com", "age": 30}
print(format_user_2(u))

def example(*args, **kwargs):
    print(args)
    print(kwargs)

example(1, 2, "test", user="Alice", user2="user2")
# exercise 1
from typing import Optional

def format_contact(name: str, phone: str, city: Optional[str] = None) -> str:
    return f"{name} ({phone})" + (f" [{city}]" if city else "")

print(format_contact("Alice", "123-456", "NYC"))
print(format_contact("Bob", "999-999"))
# exercise 2
def sum_number(*kargs: int) -> int:
    return {sum(kargs)}
print(sum_number(1,2,3,4))
# exercise 3
class UserProfile(TypedDict):
    name: str
    age: int
    email: str

u = {"name": "Alice", "email": "alice@example.com", "age": 30}
def describe_user(user: UserProfile) ->str:
    return f"name is {user['name']} age is {user['age']} email is {user['email']}"    
print(describe_user(u)) 

