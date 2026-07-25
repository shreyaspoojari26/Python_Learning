age = 22
has_id = True

if age > 18 and has_id:      # AND - both true
    print("Entry allowed")

if age < 18 or has_id:       # OR - any one true  
    print("Maybe allowed")

if not has_id:               # NOT - reverse
    print("No entry")
