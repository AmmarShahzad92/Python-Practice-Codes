staff_details = []

while True:
    name = input("Enter staff name (or 'q' to quit): ")
    if name == 'q':
        break
    
    age = int(input("Enter staff age: "))
    department = input("Enter staff department: ")
    
    staff = {'name': name, 'age': age, 'department': department}
    staff_details.append(staff)

print("Staff Details:")
for staff in staff_details:
    print("Name:", staff['name'])
    print("Age:", staff['age'])
    print("Department:", staff['department'])
    print("------------------------")

