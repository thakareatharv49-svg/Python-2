print("Creating and accessing set elements")
set_a={"Apple","Orange","Banana"}
print("Created set A:",set_a)
print("\n accessing elements in set A")
for elements in set_a:
    print(elements, end=" ")
print()
print("\n Union of the elements")
set_b={"Apple","Kiwi","Cherry"}
print("created set B:",set_b)
union_set=set_a.union(set_b)
print("union of set A and set B:",union_set)
print("\n intersection of elements")
intersection_set=set_a.intersection(set_b)
print("Intersection of set A and set B:",intersection_set)
