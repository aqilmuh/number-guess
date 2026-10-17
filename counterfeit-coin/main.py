# coins = {"1": 10, "2": 10, "3": 10, "4": 10, "5": 10, "6": 10, "7": 10, "8": 10, "9": 9}

# if len(coins) % 3 == 0:
#     group1 = list(coins.values())[:len(coins)//3]
#     group2 = list(coins.values())[len(coins)//3:2*len(coins)//3]
#     group3 = list(coins.values())[2*len(coins)//3:]

# while len(group1) > 1 or len(group2) > 1 or len(group3) > 1:
#     if sum(group1) < sum(group2):
#         # counterfeit_coin = group1
#         group1, group2, group3 = group1[:len(group1)//3], group1[len(group1)//3:2*len(group1)//3], group1[2*len(coins)//3:]
#     elif sum(group2) < sum(group3):
#         # counterfeit_coin = group2
#         group1, group2, group3 = group2[:len(group2)//3], group2[len(group2)//3:2*len(group2)//3], group2[2*len(coins)//3:]
#     else:
#         # counterfeit_coin = group3
#         group1, group2, group3 = group3[:len(group3)//3], group3[len(group3)//3:2*len(group3)//3], group3[2*len(coins)//3:]
#     # counterfeit_coin = group1 if sum(group1) < sum(group2) and sum(group1) < sum(group3) else group2 if sum(group2) < sum(group1) and sum(group2) < sum(group3) else group3
#     print(f"Counterfeit coin is in group: {counterfeit_coin}")


# print(f"The counterfeit coin is: {counterfeit_coin[0]}")

n = int(input("Enter the number of coins: "))
low = 1
high = n

while low < high:
    batas = (high - low) + 1
    size = (batas + 2) // 3
    group1_left = low
    group1_right = low + size - 1
    group2_left = group1_right + 1
    group2_right = group2_left + size - 1
    group3_left = group2_right + 1
    group3_right = high

    print("Group 1: ")
    for i in range(group1_left, group1_right + 1):
        print(f"{i} ", end="")
    print()

    print("Group 2: ")
    for i in range(group2_left, group2_right + 1):
        print(f"{i} ", end="")
    print()

    c = input("Which scale is lighter? (l or r or s): ")
    if c == "l":
        high = group1_right
    elif c == "r":
        low = group2_left
        high = group2_right
    else:
        low = group3_left

print(f"The counterfeit coin is: {low}")