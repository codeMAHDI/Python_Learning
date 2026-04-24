# List
digits =[1,"tarek",3,4,5 ]
print(digits)
print(digits[2])
print(digits[1].title())

# Access last element
print(digits[-1])


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message= f"My first bicycle was a {bicycles[2]}"
print(message)


# Modifying, Adding, and Removing Elements
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[1]="test"
print(motorcycles)
motorcycles.append('Test')
print(motorcycles)

motorcycles.insert(0, "12")
print(motorcycles)
del motorcycles[0]
print(motorcycles) 


# Pop
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

x= motorcycles.pop() # pop(0), index wise
print(f"X= {x}")
print(x+ " sdak")

#remove
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
