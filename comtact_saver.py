def greet(name: str) -> str:
    return f"Hello {name}"

def full_name(first: str, last: str) -> str:
    return f"{first} {last}"

print(greet("Vlad"))
print(full_name("Vlad", "Pat"))
