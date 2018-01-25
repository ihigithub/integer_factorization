# prime divisors


def integer_factorization(i):
    if isinstance(i, int):
        denominator=2
        list_of_divisors = []
        while denominator <= i:
            if (i%denominator) == 0:
                list_of_divisors.append(denominator)
                i = i/denominator
                denominator = 1
            denominator += 1
        return list_of_divisors
    else:
        return "not an integer"

#test divisor
i=60*13*1024*2011
print integer_factorization(i)

# number_of_prime_divisors=[]
# for i in range(0,150+1):
#     number_of_prime_divisors.append(len(integer_factorization(i)))
#     # print(integer_factorization(i))
# # print number_of_prime_divisors
# most_prime_divisors = number_of_prime_divisors.index(max(number_of_prime_divisors))
# print most_prime_divisors
# print integer_factorization(most_prime_divisors)