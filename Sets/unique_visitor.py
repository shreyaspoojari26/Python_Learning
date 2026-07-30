monday = {"user1", "user2", "user3", "user4"}
tuesday = {"user3", "user4", "user5", "user6"}

print("Total unique visitors:", monday | tuesday)
print("Visitors both days:", monday & tuesday)
print("New visitors on Tuesday:", tuesday - monday)
