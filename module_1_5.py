#immutable_war = 1, 2, 'book', 'box'
#print(immutable_war)
#immutable_war[0] = 500
#print(immutable_war)

mutable_list = [1, 2,], ['a book', 'a box']
print(mutable_list)
print(mutable_list[1])
mutable_list[1][1] = 'a book'
print(mutable_list)