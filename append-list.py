thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

print("===========================================")


thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


print("===========================================")


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


print("===========================================")

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


print("===========================================")


thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


print("===========================================")


thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)


print("===========================================")


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


print("===========================================")

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

print("===========================================")


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

print("===========================================")


thislist = ["apple", "banana", "cherry"]
del thislist



print("===========================================")

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

print("===========================================")


thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

print("===========================================")


from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

for x in range(1,10000):
  print(x)



now1 = datetime.now()

current_time1 = now1.strftime("%H:%M:%S")
print("Current Time =", current_time1)


print("===========================================")


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


print("===========================================")