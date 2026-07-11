"""Create a list of 8 books.
Add 2 new books.
Remove one unavailable book.
Insert one featured book at the beginning.
Display:
Total books
First 3 books
Last 3 books
Reverse order
Check if "Python Programming" is in the library using the in operator.
Finally, sort the book names alphabetically.
"""
books=['maths','science', 'social', 'electronics', 'sociology', 'phyton' ,'biology','communication']
print(books)
books.extend("physics,signals")
print("after adding two books",books)
books.remove("sociology")
print("unavailable books",books)
books.insert(0,"PCS")
print(books)
print(len(books))
print("first three books",books[0:3])
print("last three books",books[-3:])
print("reverse order",books[::-1])
books.sort()
print("after sorting",books)
print("phyton" in books)
