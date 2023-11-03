n = input().split(',')
n = list(map(int, n))

mid = len(n) // 2

left_part = n[ :mid]
right_part = n[mid: ]

left_sum = sum(left_part)
right_sum = sum(right_part)

if left_sum > right_sum:
    print('left-heavy')
elif left_sum < right_sum:
    print('right-heavy')
else:
    print('balanced')