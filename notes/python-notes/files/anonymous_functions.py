# normal functions
def compute(number):
    return number*2 + 1


print("Normal function: ", compute(4))

#  ____anonymous function____

# compute = lambda number: number*2 + 1

# print("Anonymous Function: ", compute(4))

scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein",
                 "Arthus C. Clarke", "Frank Herbert", "Orson Scott Card",
                 "Douglas Adams", "H. G. Wells", "Leigh Bracket"]

# sort the names using the last name
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)

# functions tha make functions


def build_quadratic_function(a, b, c):
    """Return a function f(x) = ax^2 + bx + c"""

    return lambda x: a*x**2 + b*x + c


f = build_quadratic_function(2, 3, -5)
print(f(0))
print(f(1))
print(f(2))
