kor_score = [49,80,20,100,80]
math_score = [43, 60, 85, 30, 90]
eng_score = [49, 82, 48, 50, 100]
midterm_score = [kor_score, math_score,eng_score]

def hi (num, num1) :  return midterm_score[num][num1]


print(hi(0,2),hi(1,2),hi(2,2))
print(midterm_score[1][2])