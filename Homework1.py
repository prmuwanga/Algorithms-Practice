def second_highest(A) -> int: 
    max_value = 0
    for num in A: 
        if max_value < num: 
            max_value = num
    return max_value

A= [0, 19034, 20_000, 5, 6353]


print(second_highest(A))
