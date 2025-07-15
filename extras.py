# 1. Square Elements in List
def square_elements(lst):
    result = []
    for x in lst:
        result.append(x ** 2)
    return result

nums = [1, 2, 3, 4, 5]
print("1. Squares:", square_elements(nums))


# 2. Convert Strings to Uppercase
def to_uppercase(lst):
    result = []
    for word in lst:
        result.append(word.upper())
    return result

words = ['hello', 'world', 'python']
print("2. Uppercased:", to_uppercase(words))


# 3. Add Index to Each Element
def add_index(lst):
    result = []
    for idx, value in enumerate(lst):
        result.append(f"{idx}: {value}")
    return result

values = ['a', 'b', 'c']
print("3. Indexed:", add_index(values))


# 4. Multiply Elements by 3
def multiply_by_three(lst):
    result = []
    for item in lst:
        result.append(item * 3)
    return result

arr = [2, 4, 6]
print("4. Tripled:", multiply_by_three(arr))


# 5. Length of Each Word
def get_lengths(lst):
    result = []
    for word in lst:
        result.append(len(word))
    return result

word_list = ['apple', 'banana', 'cherry']
print("5. Word Lengths:", get_lengths(word_list))


# 6. Filter Even Numbers
def filter_evens(lst):
    result = []
    for num in lst:
        if num % 2 == 0:
            result.append(num)
    return result

num_list = [10, 21, 30, 45, 60, 73]
print("6. Even Numbers:", filter_evens(num_list))


# 7. Remove Duplicates
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

dupes = [1, 2, 2, 3, 4, 4, 5]
print("7. Without Duplicates:", remove_duplicates(dupes))


# 8. Find Palindromes
def find_palindromes(lst):
    result = []
    for word in lst:
        if word == word[::-1]:
            result.append(word)
    return result

pal_words = ['madam', 'apple', 'radar', 'banana', 'level']
print("8. Palindromes:", find_palindromes(pal_words))


# 9. Merge Two Lists Element-wise
def merge_lists(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        result.append(lst1[i] + " " + lst2[i])
    return result

list1 = ['Hello', 'Good', 'See']
list2 = ['World', 'Morning', 'You']
print("9. Merged:", merge_lists(list1, list2))


# 10. Squares of Even Numbers
def even_squares(lst):
    result = []
    for num in lst:
        if num % 2 == 0:
            result.append(num ** 2)
    return result

mix_nums = [1, 2, 3, 4, 5, 6, 7]
print("10. Squares of Even Numbers:", even_squares(mix_nums))


# 11. Sort Tuples by Second Element
def sort_by_second(tuples):
    return sorted(tuples, key=lambda x: x[1])

tup_list = [(1, 3), (2, 1), (5, 0), (4, 2)]
print("11. Sorted by 2nd item:", sort_by_second(tup_list))


# 12. Count Frequency of Each Element
def count_frequencies(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

freq_list = ['a', 'b', 'a', 'c', 'b', 'a']
print("12. Frequencies:", count_frequencies(freq_list))


# 13. Remove Elements Less Than 5
def filter_five_and_up(lst):
    result = []
    for num in lst:
        if num >= 5:
            result.append(num)
    return result

nums_list = [3, 7, 2, 9, 5, 1, 6]
print("13. Elements >= 5:", filter_five_and_up(nums_list))

