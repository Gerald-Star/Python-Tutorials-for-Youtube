
# Define a string
my_string8 = "Hello, World!"

# Loop through each character in the string
for char in my_string8:
  print(char)

print()

for char in my_string8:
  print(char, end=" ")
#? Get the characters of a string using a loop


#? String Length
# The len() function returns the length of a string.
set_string1 = "Best World!"

print(len(set_string1))

print()

set_string2 = "The best of the best!"
print('best' in set_string2)


# Strings can be sliced using the slice operator [].
set_string3 = "Our World!"
print(set_string3[0:4])

print()

set_string4 = "Our World!"
if "Our" in set_string4:
  print("Yes, 'Our' is present in the string.")

print()  

set_string5 = "Our World!"
if "Expensive" not in set_string5:
  print("No, 'Expensive' is not present in the string.")
  
  
  