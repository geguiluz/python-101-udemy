def add(x, y):
    """Add two numbers together and return a result"""
    result = x + y
    return result


output_prefix = "Hola Sushi. El resultado es:"
total = add(7, 3)
message = f"{output_prefix} {total}"

print(message)
