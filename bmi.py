#WE ARE MAKING A BMI CALCULATOR 

print("PLEASE ENTER THE DETAILS\n")  


def bmi(height,weight,):
    
    sum= float(weight/(height**2))
    sum_value = round(sum, 2)
    
    if (sum > 18.5) :
        print("YOUR BODY MASS INDEX IS ",sum_value,"& YOU ARE UNDERWEIGHT")
    
    elif (18.5 <= sum < 25) :
        print("YOUR BODY MASS INDEX IS ",sum_value,"& YOU HAVE NORMAL WEIGHT")
    
    elif (25 <= sum < 30) :
        print("YOUR BODY MASS INDEX IS ",sum_value,"& YOU ARE OVER WEIGHT")

    else:
        print("YOUR BODY MASS INDEX IS ",sum_value,"& YOU ARE OBESE")
    
weight=float(input("PLEASE ENTER YOUR WEIGHT IN  KG : "))
height=float(input("PLEASE ENTER YOUR HEIGHT IN  METERS : "))

if(height>0 and weight>0) :
    pass
else:
    print("PLEASE ENTER POSITIVE VALUES ")

bmi(height,weight)
