words = input().split(',')

all_len = []
temp = 1

for i in range(len(words) - 1):
    if words[i][-1] == words[i + 1][0]:
        temp += 1
    else:
        all_len.append(temp)
        temp = 1

print(max(all_len))
