def _num_iter():#num iter
    n=2
    while True:
        n=n+1
        yield n
def _not_divisible(n):
    return lambda x: x%n > 0#any x, let x%n>0
        
def primes():
    yield 2 #yield like return but only return once, next loop will go on
    it = _num_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)


def is_palindrome(n):
    s = str(n)
    while s:
        if s[0] == s[-1]:
            s=s[1:-1]
        else:
            return False
    return True

if __name__=='__main__':
    
    print('exam1, prime_filter:')
    for n in primes():
        if n < 100:
            print(n)
        else:
            break
    print('\nexam2, palindrome_filter:')
    output=filter(is_palindrome, range(1,1000))
    print(list(output))
    
    
