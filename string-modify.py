a = "Hello, World!"
print(a.upper())

print("=============================")


a = "Hello, World!"
print(a.lower())

print("=============================")

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


print("=============================")

a = "Hello, World!"
print(a.replace("H", "J"))

print("=============================")

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

print("=============================")

y = a.split(",")

for x in y:
    print(x)