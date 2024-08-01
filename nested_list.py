import time

alist = [
    ('Harry', 37.21),
    ('Berry', 37.21),
    ('Tina', 37.2),
    ('Akriti', 41.0),
    ('Harsh', 39.0)
]

# Method 1
start_time = time.time()
second_highest = sorted(set([score for name, score in alist]))[1]
print('\n'.join(sorted([name for name, score in alist if score == second_highest])))
end_time = time.time()
print(f"Method 1 execution time: {end_time - start_time:.4f} seconds")

# Method 2
# start_time = time.time()
# score_set = set()
# for name, score in alist:
#     score_set.add(score)

# sorted_score = sorted(score_set)
# sorted_item = sorted_score[1] if len(sorted_score) > 1 else None
# names_with_second_highest = [name for name, score in alist if score == sorted_item]

# names_with_second_highest.sort()
# for i in names_with_second_highest:
#     print(i)
# end_time = time.time()
# print(f"Method 2 execution time: {end_time - start_time:.4f} seconds")
