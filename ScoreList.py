try:
    f = open("ScoreList.txt", "x")
    f.close()
except:
    pass

f = open("ScoreList.txt", "w")
f.write("Amir,50\nMahsa,90\nReza,30\nAmin,10\nZahra,95\n")
f.close()

f = open("ScoreList.txt", "a")
f.write("Mohammad,70\n")
f.close()

name_list = []
score_list = []
f = open("ScoreList.txt", "r")
list = f.read()
f.close()
new_list = list.split("\n")
new_list.pop()
print("Show-List:")
for i in new_list:
    name_score_list = i.split(",")
    name_list.append(name_score_list[0])
    score_list.append(int(name_score_list[1]))
    print("name:", name_score_list[0], "***", "score:", name_score_list[1])
print("_"*30)

max=0
for i in range(len(score_list)):
    if score_list[i]>max:
        max=score_list[i]
        max_name=name_list[i]
print("max-score:", max,"name:",max_name)
print("_"*30)

min=100
for i in range(len(score_list)):
    if score_list[i]<min:
        min=score_list[i]
        min_name=name_list[i]
print("min-score:", min,"name:",min_name)
print("_"*30)

s=0
n=len(score_list)
for i in score_list:
    s+=i
avg=s/n
print("avg-score:", avg)

