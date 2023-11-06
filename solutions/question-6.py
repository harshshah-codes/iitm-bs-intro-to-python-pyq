def sort(L):
    sorted_L = []

    while L:    
        minimum = L[0]
        for x in L:
            if x < minimum:
                minimum = x
        
        L.remove(minimum)
        sorted_L.append(minimum)

    return sorted_L



print("String input", sort(input().split(",")))

print("Integer Input", sort(list(map(int, input().split(',')))))

