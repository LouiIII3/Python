total_score = 0
# 점수들
score_list = [70, 60, 55, 75, 95] 
for score in score_list:
    total_score = total_score + score
print(total_score/len(score_list))
