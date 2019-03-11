numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
num_sum = 0
count = 0
for num in numbers:
    num_sum = num_sum + num
    count = count + 1 
    if count == 5:
        break
print("Sum of first ",count,"integers is: ", num_sum)

def outside():
       a = 10
       def inside():
           a = 20
           print("Inside a ->", a)
       inside()
       print("outside a->", a)
outside()

def prime(n):
    even = []
    prime = []
    print("incoming list a->", n)
    if len(n) > 1:
        for i in n:
            if i % 2 == 1:
                prime.append(i)      
            else:
                even.append(i)
    print(
        "This list has {} prime numbers and {} even numbers".format(
            len(prime), len(even)))

prime([22, 24, 8, 10])


class Robber:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    def attack(self, victim):
        victim.health = victim.health - self.damage 



you = Robber("Vic")
me = Robber("B")
print(me.health)

you.attack(me)
print(me.health)
