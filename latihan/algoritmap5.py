i = 1

while (i <= 200):
    j = 2

    while(j<= (i/j)):
        if not (i % j):
            break
        j = j+1

    if j > (i/j): 
        print(i, "adalah bilangan prima")
    i = i + 1
    
print("Terimakasih")


    