def second_largest(nums):
    """ 
    function for finding second largest number
    Takes nums as a parameter
    """
    first_max=-10**100
    second_max=-10**100
    for num in nums:
        if num > first_max:
            second_max=first_max
            first_max=num
        elif first_max>num>second_max:
            second_max=num
    if second_max > -10**100:
        return second_max
    else:
        return "No second largest"
        
def main():    
    #nums=[2,11,15,66,20]
    nums=[]
    nums_size=int(input("enter the size of list: "))
    for i in range(nums_size):
        element=int(input("enter a number:"))
        nums.append(element)
       
    print(f"second largest number is :{second_largest(nums)}")
   

if __name__=="__main__":
    main()