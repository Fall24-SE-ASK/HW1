def odd_even(x):
    return x % 2 == 0

def show_result(x):
    ans = 'even' if odd_even(x) else 'odd'
    print(f'{x} is {ans}')

show_result(5)
show_result(11)
show_result(16)
