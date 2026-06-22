scores = [45, 72, 88, 55, 91, 63,78, 49, 84, 60]
passing_scores = []
failing_scores = []

for score in scores:
    if score > 70:
        passing_scores.append(score)
    else:
        failing_scores.append(score)

    print("passing_scores:", passing_scores)
    print("failing_scores:",failing_scores)
    print("highest_scores:",max(scores))
    print("lowest_scores:",min(scores))
    print("number of students who passed:",len(passing_scores))

