def pyth_triplet():
    for i in range(1,999):
        for j in range(i+1,999):
            for k in range(j+1, 999):
                if ((i**2 + j**2 == k**2) and (i+j+k == 1000)):
                    return(i*j*k)
                
print(pyth_triplet())
