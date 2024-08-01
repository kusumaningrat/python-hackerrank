n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

# for student in student_marks.items():
#     if student[0] == query_name:
#         score = sum(student[1])
#         the_avg = score / 3
#         print(f'{the_avg:.2f}')

if query_name in student_marks:
    the_avg = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f'{the_avg:.2f}')
