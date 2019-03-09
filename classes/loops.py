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
    count = 0
    print("incoming a->", n)
    if n > 1:
        for i in range(1,n+1):
            print("This is nice", i)
            if n % i == 1:
                count = count + 1        
        if count == 2:
            return True
        else:
            return False

def find_prime(numbers):
    prime_list = list(filter(prime, numbers))
    print("This the list has {} prime numbers".format(sum(prime_list)))

find_prime([22,25,4,6])


class Robber:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    def attack(self, victim):
        victim.health = victim.health - self.damage 



you = Robber("Victoria")
me = Robber("Bonny")
print(me.health)

you.attack(me)
print(me.health)
