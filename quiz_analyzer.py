# CHUA, FORREST ZELLINE M.

quiz = []

for i in range(1, 6):
    quiz.append(int(input(f"Enter Quiz {i} Score: ")))

print(f"""===== QUIZ SCORE REPORT =====
Quiz Scores: {quiz}
Number of Quizzes: {len(quiz)}
Total Score: {sum(quiz)}
Average Score: {sum(quiz)/len(quiz):.2f}
Highest Score: {max(quiz)}
Lowest Score: {min(quiz)}
Ascending: {sorted(quiz)}
Descending: {sorted(quiz, reverse=True)}
Original Scores: {quiz}""")
