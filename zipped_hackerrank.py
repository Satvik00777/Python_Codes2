N, X = map(int, input().split())
score = []
for _ in range(X):
    score.append(list(map(float, input().split())))
for stud in list(zip(*score)):
    print("%.1f" % (sum(stud) / len(stud)))
