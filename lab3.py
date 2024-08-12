from modules.fileoperation import read, write, append

################### Q1 ##########################
print(read("db.txt", "All"))  # filepath, option
print(read("db.txt", "line"))
print(read("db.txt", "lines"))
print(read("db.txt", 5))
print(read("db.txt", "X"))

################### Q2 ##########################
print(write("db.txt", "5, ahmed, html"))  # filepath, content
print(write("db.txt", 3))

################### Q3 ##########################
print(append("db.txt", "9, saad, javascript"))  # filepath, new content
