# a = [1, 2, 3, 4, 1, 5, 3, 5, 2, 4, 2, 4, 1, 5]
a =['a', 'b', 'cat', 'b', 'a', 'dog', 'e', 'f', 'greg', 'h', 'greg', 1, 1, 2, 2]

b = []

for i in a:
    if i not in b:
        b.append(i)

print(b)