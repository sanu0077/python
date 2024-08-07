myList = [1, 2, 3]
myListSquare = [x ** 2 for x in myList]
myList.insert(1,8)
print(myListSquare)
print(myList)
myListSquare = [x ** 2 for x in myList]
print(myListSquare)

m1 = [ 1, 2, 3]
m2 = m1
print(m2)
m1[0] = 99
print(m1)
