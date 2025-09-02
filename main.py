age = 17 
price = 10.5  
name = "Karina"  
is_student = True 
classmates = ["Alice", "Bob", "Charlie"]  
grades = {"Alice": 90, "Bob": 85, "Charlie": 92}  
prices = (9.99, 19.99, 29.99)  
number = {1, 2, 3, 4, 5}  
friends = ["David", "Eva", "Frank"]
i_heve_mom = False 

a = [age, price, name, is_student, classmates, grades, prices, number, friends, i_heve_mom] 
b = 0 

for item in a:  
    b += 1 
    print(f"{b} {item} is of type {type(item)}")  

