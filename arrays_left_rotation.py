def array_left_rotation(a, n, k):
    assert (n>=1 and n <= 100000), 'n: must be 1<= n <= 10^5'
    assert (k>=1 and k <= n), 'n: must be 1 <= d <= n'
    assert (max(a)<=1000000 and min(a)>=1), 'a: numbers in array must be 1 <= ai <= 10^6'
    assert (n == len(a)), 'n != array size'
    sol = []
    mod = k % n
    if( mod == 0):
        return a
    for i in range(len(a)):
        z = (mod + i) % n
        sol.insert(i, a[z])
    return sol


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
