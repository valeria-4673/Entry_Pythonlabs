#LAB 3.4.1.6
hat_list = [1, 2, 3, 4, 5]

# Step 1
hat_list[2] = int(input("Enter an integer number: "))

# Step 2
del hat_list[-1]

# Step 3
print(len(hat_list))

#LAB 3.4.1.13

# step 1
beatles = []
print("Step 1:", beatles)

# step 2

beatles.append("John Lennon") 
beatles.append("Paul McCartney") 
beatles.append("George Harrison") 

print("Step 2:", beatles)
    
# step 3
for i in range(2):
    user_input = input("write the name you wanna add: ")
    beatles.append(user_input)
print("Step 3:", beatles)

# step 4

del beatles [3:]
print("Step 4:", beatles)

# step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))

#LAB 3.6.1.9 

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_list2 = []
my_list2.append(my_list[0])

for i in range (1, len(my_list)):
    if my_list[i] not in my_list2:
        my_list2.append(my_list[i])
    
print("The list with unique elements only:")
print(my_list2)
