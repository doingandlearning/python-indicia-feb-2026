import numpy as np

# Student test scores
math_scores = [85, 92, 78, 88, 95]
science_scores = [90, 88, 85, 92, 89]

bonus_math = []
for score in math_scores:
    bonus_math.append(score + 5)

# To calculate average:
avg_math = sum(math_scores) / len(math_scores)

# To add math and science scores together:
total_scores = []
for i in range(len(math_scores)):
    total_scores.append(math_scores[i] + science_scores[i])


math_scores_np = np.array(math_scores)
science_scores_np = np.array(science_scores)
math_scores_with_bonus = math_scores_np + 5  # vector maths
print(math_scores_np, math_scores_with_bonus)

print(math_scores_np.mean())
print(math_scores_np + science_scores_np)

numbers = np.linspace(0, 100, 17)
print(numbers)
print(np.std(math_scores_np))