def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        print(first_child)
        return first_child
    else:
        print(second_child)
        return second_child

parent(2)