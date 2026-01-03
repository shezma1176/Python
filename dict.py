#empty dictionary
my_dict={}
my_dict1={"name":"Aidah","Grade":7,"city": "Narsingdi"}
print(my_dict1)

#length

print(len(my_dict1))

#access data

print(my_dict1["name"])
print(my_dict1["Grade"])
print(my_dict1["city"])

#add item

my_dict1['Country']="Bangladesh"
print(my_dict1)

#Remove Item

my_dict1.pop('city')
print(my_dict1)

#access a particular item using get()

print(my_dict1.get('Country'))

#Clear all data

my_dict1.clear
print(my_dict1)

#loops in dictionary

my_dict1={"name":"Aidah","Grade":7,"city": "Narsingdi"}
for i in my_dict1:
    print(i)