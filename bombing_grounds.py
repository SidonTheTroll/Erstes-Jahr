d = {'Name': "Rahul", 'Salary': 10000, 'Age': 45, 'Dept': 'Sales'}

# Prints raw data
print(d) # {'Name': "Rahul", 'Salary': 10000, 'Age': 45, 'Dept': 'Sales'}
print()
# Print headers
print(d.keys()) # dict_keys(['Name', 'Salary', 'Age', 'Dept'])
print()

d = {'Name': "Rahul", 'Salary': 10000, 'Age': 45}
c = {'Name': "Sonali", 'Salary': 4000, 'Dept': 'Production'}

d.update(c) # Replace values with dictionary 'c'
# If heading are found to be unique in initial dictionary, the value will remain the same. 
print(d)
print()

c.clear() # deletes data is dictionary 
print(c)
print()

del(c) # Deletes dictionary 'c'
print(c)
