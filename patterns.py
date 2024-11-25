def centered_star_pattern(n):
    for i in range(1, n+1):
        print(' '*(n-i) + '*'*(2*i-1))

centered_star_pattern(20)

def left_aligned_star_pattern(n):
    for i in range(1, n+1):
        print('*'*i)

left_aligned_star_pattern(20)

def right_aligned_star_pattern(n):
    for i in range(1, n+1):
        print(' '*(n-i) + '*'*i)

right_aligned_star_pattern(20)

def squre_star_pattern(n):
    for i in range(1, n+1):
        print('*'*n)

squre_star_pattern(20)

def hollow_squre_star_pattern(n):
    for i in range(1, n+1):
        if i == 1 or i == n:
            print('*'*n)
        else:
            print('*' + ' '*(n-2) + '*')

hollow_squre_star_pattern(20)