# List 
list = ["tom", "bob", "lucy", "mary"]

# List elements start at 0 forward and -1 backward
print(list[3])

list.append("larry")

print(list)

# Modify List Elements

garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]

garden_waitlist[1] = "Calla"
garden_waitlist[-1] = "Alex"

print(garden_waitlist)

# Example

order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
order_list.remove("Flatbread")
print(order_list)
new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
new_store_order_list.remove("Mango")
print(new_store_order_list)


# 2D Lists

heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64]]
heights.append(["Vik", 68])

ages = [["Aaron", 15], ["Dhruti", 16]]

# Accessing 2D Lists

class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83],["Ellie", 101.5]]
print(class_name_test)

sams_score = class_name_test[2][1]
print(sams_score)

ellies_score = class_name_test[-1][-1]
print(ellies_score)

# Modifying 2D Lists

incoming_class = [["Kenny", "American", 9], ["Tanya", "Ukrainian", 9], ["Madison", "Indian", 7]]
print(incoming_class)

incoming_class[2][2] = 8
print(incoming_class)

incoming_class[-3][-3] = "Ken"
print(incoming_class)

# Review

first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]

preferred_size.append("Medium")
print(preferred_size)

customer_data = [["Ainsley","Small",True], ["Ben","Large",False], ["Chani","Medium",True], ["Depak","Medium",False]]
print(customer_data)

customer_data[2][2] = False
print(customer_data)

customer_data[1].remove(False)
print(customer_data)

customer_data_final = customer_data + [["Amit","Large",True], ["Karim","X-Large",False]]
print(customer_data_final)