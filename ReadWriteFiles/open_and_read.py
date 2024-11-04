f = open("about_me.txt", "r")

#print(f.readline(10))

#print(f.readline())

#for i in range(1, 5):
    #print(f.readline())

#print(f.readlines())
#print(f.readlines(1))  
#print(f.readlines(10))  
#print(f.readlines(100))

first_50_characters = f.read(50)

line_output = []
for i in range(1, 5):
    line_output.append(f.readline())

remaining_lines = f.readlines(100)

print("First 50 characters:", first_50_characters)
print("Output from .readline() loop:", line_output)
print("Remaining lines using .readlines(100):", remaining_lines)

f.close()
