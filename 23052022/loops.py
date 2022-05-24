list_data = [1, 2, 3, 4, 5]
embedded_list = [[1, 2, 3], [4, 5, 6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"},
             3: {"name": "Roscoe", "money": "$1.14"}}

# for item in dict_data.values():
#     for embed_value in item.values():
#         print(embed_value)

for num in list_data:
    if num == 3:
        print("I found three")
    elif num > 3:
        print("I've gone too far")
    else:
        print("Too soon")


