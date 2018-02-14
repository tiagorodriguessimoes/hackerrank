from collections import Counter
def number_needed(a, b):
    a_count = len(a)
    b_count = len(b)
    assert(a_count <= 10e4), "Variable a: Too many chars"
    assert(a_count >= 1), "Variable a: Not enough chars"
    assert(b_count <= 10e4), "Variable b: Too many chars"
    assert(b_count >= 1), "Variable b: Not enough chars"
    if(a_count == 1 and b_count == 1 and a != b):
        return 2
    else:
        a_cnt = count_charts(a)
        b_cnt = count_charts(b)
        total_set_cnt = (a_cnt - b_cnt) + (b_cnt - a_cnt)
        return sum(total_set_cnt.values())


def count_charts(s):
    cnt = Counter()
    for letter in s:
        cnt[letter] += 1
    return cnt

a = input().strip()
b = input().strip()

print(number_needed(a, b))
