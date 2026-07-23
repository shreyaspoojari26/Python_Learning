coding = {"Shreyas", "Rahul", "Aman", "Ravi"}

robotics = {"Rahul", "Aman", "Kiran", "Ajay"}

print("All Students:", coding | robotics)

print("Both Clubs:", coding & robotics)

print("Only Coding:", coding - robotics)

print("Only Robotics:", robotics - coding)

print("Only One Club:", coding ^ robotics)
