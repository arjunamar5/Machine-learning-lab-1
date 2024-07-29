def count_pairs_with_sum(arr, t):
    c = 0
    s = set()
    
    for number in arr:
        complement = t - number
        if complement in s:
            c += 1
        s.add(number)
    
    return c

# Given list
arr = [2, 7, 4, 1, 3, 6]
t = 10

# Count pairs
pair_count = count_pairs_with_sum(arr, t)
print(f"Number of pairs with sum {t}: {pair_count}")
