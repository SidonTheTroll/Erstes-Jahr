empl = {"John": {'Age': 30, 'Salary': 25000}, "Diya":{'Age': 28, 'Salary': 30000}}

for key in empl: 
    print("Employee:", key)
    print("Age:", str(empl[key]['Age']))
    print('Salary:', str(empl[key]["Salary"]))
