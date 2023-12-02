thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


print("===========================================")


thislist = [100, 50, 65, 82, 23]

thislist.sort()

print(thislist)


print("===========================================")

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


print("===========================================")

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


print("===========================================")


def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

print("===========================================")




print("===========================================")