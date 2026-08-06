d = {"a": 1, "b": 2, "c": 3}

print(d.get("b")) # 2 - safer than d["b"]
print(d.get("z", 0)) # 0 - default if key not found

print(d.keys()) # dict_keys(['a', 'b', 'c'])
print(d.values()) # dict_values([1, 2, 3])
print(d.items()) # dict_items([('a', 1), ('b', 2), ('c', 3)])

d.update({"d": 4, "a": 10}) # update/add multiple
print(d) # {'a': 10, 'b': 2, 'c': 3, 'd': 4}

d.pop("b") # remove key and return value
print(d) # {'a': 10, 'c': 3, 'd': 4}
