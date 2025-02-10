def count_in_list(list, word):
    count = 0
    if not list or not word:
        return count
    for item in list:
        if item == word:
            count += 1
    return count
