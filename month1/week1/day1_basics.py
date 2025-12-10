#VARIABLES + BASIC TYPES

x = 10
y = 3.14
name = "EdgeAI"
is_active = True

print(type(x), type(y), type(name), type(is_active))

#LIST vs TUPLE
#List is mutable
#Tuple is immutable

numbers_list = [1, 2, 3]
numbers_tuple = (1, 2, 3)
numbers_list.append(4)
print(numbers_list)

try:
    numbers_tuple.append(4)
except AttributeError as e:
    print("Tuple error:", e)

#DICTIONARY BASICS

config = {
    "model": "baseline",
    "threshold": 0.05
}
config["threshold"] = 0.1
config["device"] = "cpu"

print(config)

#MUTABILITY VS IMMUTABILITY
#int (immutable)
#list (mutable)
#id() change vs no change

a = 10
b = a
b = b + 5

print(a, b)
print(id(a), id(b))

lst1 = [1, 2, 3]
lst2 = lst1
lst2.append(4)

print(lst1, lst2)
print(id(lst1), id(lst2))

#SIMPLE FUNCTION

def percentage_change(old, new):
    return ((new - old) / old) * 100

print(percentage_change(100, 120))

#BASIC LOOP + CONDITIONAL

values = [10, 20, 5, 40]
for v in values:
    if v > 15:
        print(v, "is above threshold")

