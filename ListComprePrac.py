a= [x for x in range(1,11) if x%2==0]
print(a)
noprimes = [j for i in range(2,8) for j in range(i*2, 50, i)]
print noprimes
primes = [ y for y in range(2,50) if y not in noprimes]
print primes
