# count = 0
# new_list = []
# with open('444.csv', 'r', encoding="utf-8") as data:
#     for line in data:
#         count +=1
#         if count > 7:
#             result = line.split(';')
#             # print(result)
#             new_list.append(result[1])
#             new_list.append(result[5])
#             new_list.append(result[8])
# print(new_list)

count = 0

res = []
with open('444.csv', 'r', encoding="utf-8") as data:
    for line in data:
        new_list = []
        count +=1
        if count > 7:
            result = line.split(';')
            # print(result)
            new_list.append(result[1])
            new_list.append(result[5])
            new_list.append(result[8])
            a = ';'.join(new_list)
            res.append(a)
# print(res)
count_test = 0
count_res = 0
test = set(res)
for i in test:
    # print(i + '\n')
    count_test +=1
for i in res:
    # print(i + '\n')
    count_res +=1
print(count_test)
print(count_res)