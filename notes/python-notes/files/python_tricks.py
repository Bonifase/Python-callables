def multiplier():
    def multiply(x):
        return [i * x for i in range(5)]

print(multiplier())

list = ['a', 'b', 'c', 'd', 'e']
print list[10:]

# The above code will output [], and will not result in an IndexError.

# As one would expect, attempting to access a member of a list using an index that exceeds the number of members (e.g., attempting to access list[10] in the list above) results in an IndexError. However, attempting to access a slice of a list at a starting index that exceeds the number of members in the list will not result in an IndexError and will simply return an empty list.

# What makes this a particularly nasty gotcha is that it can lead to bugs that are really hard to track down since no error is raised at runtime.

list = [ [ ], [] ] * 5
print(list)

# Given a list of N numbers, use a single list comprehension to produce a new list that only contains those values that are:
# (a) even numbers, and
# (b) from elements in the original list that had even indices

list1 = [ 1 , 3 , 5 , 8 , 10 , 13 , 18 , 36 , 78 ]