def first_and_last_4(item):
    return item[:4]+item[-4:]


item = ['You', 'are', 'okay,' 'right,' 'now', 'I', 'need', 'to', 'leave']
test = first_and_last_4(item)
print(test)
