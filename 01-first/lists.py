alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# Print len
print(len(alpha)) # 7
# Slice from 3 to end
print(alpha[3:]) # D E F G
# Slice first 3
print(alpha[:3]) #A B C
# Slice 1 to 3
print(alpha[1:3]) # B C

# Extend with another list
alpha.extend(['H', 'I'])
print(alpha)

