def prime_numbers(number_range):
    from math import sqrt
    prime_numbers_list=[]
    for i in range(2,number_range):
        prime_numbers_list.append(i)
    for p in range(2,int(sqrt(number_range))):
        for m in range(p*2,number_range,p):
            if m in prime_numbers_list:
                prime_numbers_list.remove(m)
    print(prime_numbers_list)
 
