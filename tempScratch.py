from itertools import product

def find_combinations(lists, target_sum):
    all_combinations = product(*lists)

    valid_combinations = [
        combination for combination in all_combinations if sum(combination) == target_sum
    ]

    return valid_combinations

# Example usage
lists = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

target_sum = 20



result_combinations = find_combinations(lists, target_sum)

#print("Combinations with the sum of", target_sum, ":", result_combinations)
lst=["5","3",".",".","7",".",".",".","."]
char_to_remove="."
remove_char_from_list = lambda my_list, char_to_remove: list(filter(lambda x: x != char_to_remove, my_list))

# Example usage
remove_char_from_list(lst,char_to_remove=char_to_remove)

isNotRepeating=lambda l: False if len(l)!= len(set(l)) else True
flag=isNotRepeating(lst)
print(flag)

