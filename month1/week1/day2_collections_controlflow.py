#COLLECTIONS
lst1 = [23,76,34,"cycle"]

print(id(lst1))
lst2 = lst1
print(id(lst2))
lst2.append("tricycle")
print("list1 =" , lst1)
print("list2 =" , lst2)

tple1 = (4,5,2,7,7,7,54,"bike")
#tple1.append(34)
print(id(lst1))
tple2 = tple1
print(id(lst2))

set1 = {6,5,7,9,9,"car"}
set1.add("bus")
print("list ="+ str(lst1))
set1.update(lst2)
print("list =" , lst1)

dict1 = {"name":"course","age":7,"life":"10 months"}
print(type(lst1))
print("list ="+ str(lst1))
print("tuple =", tple1)
print("set ="+ str(set1))
print("dictonary ="+ str(dict1))

for i in lst1:
    if type(i) == str:
        print (i)



#############
#CHATGPT CODE 
#############

# ------------------------------
# 1. LIST (Ordered, Mutable)
# ------------------------------
print("---- LIST ----")
lst1 = [10, 20, "apple", 4.5]

print("Original list:", lst1)
print("Original list id:", id(lst1))

# Modify (mutability)
lst1.append("banana")
lst1[1] = 99
print("Modified list:", lst1)
print("List id after modification:", id(lst1))    # SAME id → proves mutability


# ------------------------------
# 2. TUPLE (Ordered, Immutable)
# ------------------------------
print("\n---- TUPLE ----")
t1 = (1, 2, "dog", 5.6)
print("Tuple:", t1)
print("Tuple id:", id(t1))

# Trying to modify tuple → should fail
try:
    t1[1] = 100
except TypeError as e:
    print("Tuple modification error (as expected):", e)

# Reassigning a new tuple (not modifying existing)
t2 = (1, 2, 3)
print("New tuple:", t2)
print("New tuple id:", id(t2))   # DIFFERENT id → proof that reassignment ≠ mutation


# ------------------------------
# 3. SET (Unordered, Unique, Mutable)
# ------------------------------
print("\n---- SET ----")
s1 = {5, 10, 5, "car", "car", 20}
print("Set removes duplicates automatically:", s1)

# Modify set
s1.add("bus")
s1.add(5)   # No duplicate added
print("After adding:", s1)

# Update from another collection
s1.update([100, 200, 100])
print("After update with list:", s1)

print("Check membership: 'car' in set? ->", "car" in s1)


# ------------------------------
# 4. DICTIONARY (Key-Value, Mutable, Ordered)
# ------------------------------
print("\n---- DICTIONARY ----")
d1 = {"name": "John", "age": 25, "role": "Engineer"}

print("Original dict:", d1)
print("Original dict id:", id(d1))

# Modify dictionary
d1["age"] = 30                     # update
d1["city"] = "Bangalore"           # add
removed = d1.pop("role")           # delete
print("Modified dict:", d1)
print("Dict id after modification:", id(d1))   # SAME id → mutability


# Looping patterns
print("\nDict keys:")
for k in d1.keys():
    print(k)

print("Dict values:")
for v in d1.values():
    print(v)

print("Dict items:")
for k, v in d1.items():
    print(k, ":", v)


# ------------------------------
# 5. NESTED ACCESS
# ------------------------------
print("\n---- NESTED STRUCTURE ----")
nested = {
    "data": [1, 2, (3, 4), {"x": 5}]
}

print("Access nested value:", nested["data"][3]["x"])
