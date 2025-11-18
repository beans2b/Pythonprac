
with open("grades.txt", "w") as f:
    f.write ("S1001,85,72,90:\nS1002,45,60,55:\nS1003,92,88,95\nS1004,70,71,68:\nS1005,50,55,50\n")

with open("grades.txt", "r") as f:
    line1= f.readline().strip().split(":")
    line2= f.readline().strip().split(":")
    line3= f.readline().strip().split(":")

line1_stud= line1[0].split(",")
Studeid1= line1_stud[0]
Ass_Score1=int(line1_stud[1])
Mid_Score1= int(line1_stud[2])
Fin_Score1=int(line1_stud[3])

line2_stud= line2[0].split(",")
Studeid2= line2_stud[0]
Ass_Score2=int(line2_stud[1])
Mid_Score2= int(line2_stud[2])
Fin_Score2=int(line2_stud[3])

line3_stud= line3[0].split(",")
Studeid3= line3_stud[0]
Ass_Score3=int(line3_stud[1])
Mid_Score3= int(line3_stud[2])
Fin_Score3=int(line3_stud[3])

Avg_score_stud1 =  (Ass_Score1 + Mid_Score1 + Fin_Score1)/3
Avg_score_stud2 =  (Ass_Score2 + Mid_Score2 + Fin_Score2)/3
Avg_score_stud3 =  (Ass_Score3 + Mid_Score3 + Fin_Score3)/3

if Avg_score_stud1 >= 70:
    print("PASS")
elif Avg_score_stud1 >= 60 and Fin_Score1 >= 65:
    print("PASS")
else:
    print("YOU FAILED BOY")

if Avg_score_stud2 >= 70:
    print("PASS")
elif Avg_score_stud2 >= 60 and Fin_Score2 >= 65:
    print("PASS")
else:
    print("YOU FAILED BOY")

if Avg_score_stud3 >= 70:
    print("PASS")
elif Avg_score_stud3 >= 60 and Fin_Score3 >= 65:
    print("PASS")
else:
    print(f"YOU FAILED BOY")

print(f"Student:{Studeid1}\nYOU PASSED\nAverage Grade:{Avg_score_stud1:.1f}")
print(f"Student:{Studeid2}\nYOU FAILED\nAverage Grade:{Avg_score_stud2:.1f}")
print(f"Student:{Studeid3}\nYOU PASSED\nAverage Grade:{Avg_score_stud3:.1f}")

