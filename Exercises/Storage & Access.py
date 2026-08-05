# Storage and Access

# Writing to a file
with open("student.txt", "w") as file:
    file.write("Name: Teddy\n")
    file.write("Course: FNB App Academy 2026\n")

# Reading from the file
with open("student.txt", "r") as file:
    content = file.read()

print("File Content:")
print(content)
