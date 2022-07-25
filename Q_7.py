
id_lst = ["A", "B", "C", "D"]
report = ["A B", "C B", "B D", "A D", "C A"]
k = 2 

# print(report)

# AA = "A B"
# print(AA[0:AA.find(" ")])
# print(AA[(-1) * AA.find(" "):])

for i in report:
    user_id = i[0:i.find(" ")]
    bad_user_id = i[(-1) * i.find(" "):]

    print("{0}유저가 {1}을(를) 신고했습니다.".format(user_id,bad_user_id))