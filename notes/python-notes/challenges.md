#### Essential Python Challenges

```
def multiplier():
    def multiply(x):
        return [i * x for i in range(5)]

print(multiplier())

list = ['a', 'b', 'c', 'd', 'e']
print list[10:]
```

The above code will output [], and will not result in an IndexError.

As one would expect, attempting to access a member of a list using an index that exceeds the number of members (e.g., attempting to access list[10] in the list above) results in an IndexError. However, attempting to access a slice of a list at a starting index that exceeds the number of members in the list will not result in an IndexError and will simply return an empty list.

What makes this a particularly nasty gotcha is that it can lead to bugs that are really hard to track down since no error is raised at runtime.

```
list = [ [ ], [] ] * 5
print(list)
```

Given a list of N numbers, use a single list comprehension to produce a new list that only contains those values that are:
(a) even numbers, and
(b) from elements in the original list that had even indices

```
list = [ 1 , 3 , 5 , 8 , 10 , 13 , 18 , 36 , 78 ]

```

A simple solution to this problem would be as follows:

```
[x for x in list[::2] if x%2 == 0]
```

For example, given the following list:

```
#        0   1   2   3    4    5    6    7    8
list = [ 1 , 3 , 5 , 8 , 10 , 13 , 18 , 36 , 78 ]
```

the list comprehension [x for x in list[::2] if x%2 == 0] will evaluate to:

```
[10, 18, 78]
```

The expression works by first taking the numbers that are at the even indices, and then filtering out all the odd numbers.

How do you list the functions in a module?

```
Use the dir() method to list the functions in a module.

For example:

import some_module
print dir(some_module)
```

Write a function that prints the least integer that is not present in a given list and cannot be represented by the summation of the sub-elements of the list.

E.g. For a = [1,2,5,7] the least integer not represented by the list or a slice of the list is 4, and if a = [1,2,2,5,7] then the least non-representable integer is 18.

```
import  itertools
sum_list = []
stuff = [1,2, 5, 7]
for L in range(0, len(stuff)+1):
    for subset in itertools.combinations(stuff, L):
        sum_list.append(sum(subset))

new_list = list(set(sum_list))
new_list.sort()
for each in range(0,new_list[-1]+2):
    if each not in new_list:
        print(each)
        break
```

What will be the output of the code below? Explain your answer.

```
def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3
```

How would you modify the definition of extendList to produce the presumably desired behavior?

```
The output of the above code will be:

list1 = [10, 'a']
list2 = [123]
list3 = [10, 'a']
Many will mistakenly expect list1 to be equal to [10] and list3 to be equal to ['a'], thinking that the list argument will be set to its default value of [] each time extendList is called.

However, what actually happens is that the new default list is created only once when the function is defined, and that same list is then used subsequently whenever extendList is invoked without a list argument being specified. This is because expressions in default arguments are calculated when the function is defined, not when it’s called.

list1 and list3 are therefore operating on the same default list, whereas list2 is operating on a separate list that it created (by passing its own empty list as the value for the list parameter).

The definition of the extendList function could be modified as follows, though, to always begin a new list when no list argument is specified, which is more likely to have been the desired behavior:

def extendList(val, list=None):
  if list is None:
    list = []
  list.append(val)
  return list
With this revised implementation, the output would be:

list1 = [10]
list2 = [123]
list3 = ['a']
```
