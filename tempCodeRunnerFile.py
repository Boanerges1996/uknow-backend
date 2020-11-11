# A
print(data[["name", "Jan", "Feb", "Mar"]].query("state=='Texas'"))

# B
print(data[["street", "city"]].query("state=='Lowa'"))

# C
print(len(data))

# D
# Print first 2 records
print(data.head(2))