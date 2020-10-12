def days_represented(a) :
#     total = 0
#     days = []
#     for each in trips :
#         num = max(each) - min(each) + 1
#         total = total + num
#
#         rng = range(min(each), max(each) + 1)
#         for each in rng :
#             days.append(each)
#
#     index = 0
#     doubles = 0
#     for each in sorted(days) :
#         if index + 1 == len(days) :
#             break
#         if each == sorted(days)[index + 1] :
#             doubles = doubles + 1
#
#         index = index + 1
#
#     return total - doubles
#
# # couldn't quite get this to work with count
#     total = 0
#     days = []
#     for each in trips :
#         num = max(each) - min(each) + 1
#         total = total + num
#
#         rng = range(min(each), max(each) + 1)
#         for each in rng :
#             days.append(each)
#
#     doubles = 0
#     for each in days :
#         if days.count(each) > 1 :
#             doubles = doubles + 1
#
#     doubles = int(doubles / 2)
#
#     return total - doubles
    som = [i for x, y in a]
    print(som)
    # return len({i for x, y in a for i in range(x, y + 1)})

# print(days_represented([[10,17],[200,207]]))
# print(days_represented([[10,15],[25,35]]))
# print(days_represented([[204, 243], [100, 103], [151, 189], [97, 106], [207, 222], [175, 175], [103, 108]]))
print(days_represented([[100, 103], [97, 106]]))
