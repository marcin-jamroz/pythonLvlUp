from math import sqrt
import time

def prime(prime_num):
    primes = []
    tmp_num = 0
    curr_num = 2
    prime_flag = True

    while tmp_num < prime_num:
        sqr = sqrt(curr_num)

        for num in primes:
            if num > sqr:
                break
            elif curr_num % num == 0:
                prime_flag = False
                break

        if prime_flag:
            primes.append(curr_num)
            tmp_num = tmp_num + 1

        prime_flag = True
        curr_num = curr_num + 1
        
    return sum(primes)

time1 = time.time()
print(prime(1234567))
time2 = time.time()

print(time2 - time1)