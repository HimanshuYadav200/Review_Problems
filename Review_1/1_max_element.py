def find_max_num1(lst):
    return max(lst)
    
def find_max_num2(lst):
    max_number=-10**100
    for i in lst:
        if(max_number<i):
            max_number=i
    return max_number        
    

list=[]
list_size=int(input("enter the size of the list: "))

for i in range(list_size):
    num=int(input("enter the number to add in list: "))
    list.append(num)
    
max_num=find_max_num2(list)   
print(f"maximum number among the 3 numbers in list is {max_num}")