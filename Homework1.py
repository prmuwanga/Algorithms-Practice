def second_highest(A) -> int: 
    max_value = 0
    second_max = 0

    for num in A: 
        if max_value < num: 
            max_value = num

    for j in A: 
        #base case to exclude max value 
        if j == max_value:
            continue 
            
        if (j < max_value) && (j>=second_max): 
        
        second_max = j

        
def second_highest(A): 
    less = A.min()
    high = A.max()

    for num in A: 
        if num > max:



    A.sort()
    return A[-2]


5

A= [0, 19034, 20_000, 5, 6353, 10834678282]


print(second_highest(A))
