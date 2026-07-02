#write a python function that will take any number oof arguements and sum them 

#*args is a parameter that will pack all arguements into a tuple,
#It is useful for a functionthat accpets varying amount of arguements

def sum(*agrs):
    
    total_sum = 0
    for arg in agrs:
        total_sum += arg
    print(total_sum)

sum(12,23)
sum(12,23, 23)
sum(12,23,14, 23)

