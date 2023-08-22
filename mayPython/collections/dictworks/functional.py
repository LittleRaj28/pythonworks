lst = [1,2,3,4,5]
squares = list(map(lambda n:n**2,lst))
print(squares)

cubes = list(map(lambda n:n**3,lst))
print(cubes)

#filter

#evens
def is_even(n):
    if n%2==0:
        evens = list(filter(is_even(),lst))
        print(evens)

#odds

def is_odd(n):
    if n%2!=0:
        odds = list(filter(is_odd,lst))
        print(odds)




