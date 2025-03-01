def is_prime(num):
    
        divisores = [i for i in range(2, num )]
        
        for divisor in divisores:
            if num % divisor == 0:
                return False
        return True
        
for i in range(1, 20):
	if is_prime(i + 1):
	    print(i + 1, end=" ")
print()
