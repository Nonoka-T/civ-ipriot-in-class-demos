def count_occurrences(target_word, line):
    word_counter = 0
    words = line.lower().split()
    target_word = target_word.lower()
    for word in words:
        if word == target_word:
            word_counter = word_counter + 1
    return word_counter


with open("ice_ice_baby.txt", encoding='utf8') as file:
    total_ice_counter = 0
    for line in file:
        ice_count = count_occurrences("ict", line)
        total_ice_counter = total_ice_counter + ice_count
        if ice_count > 0:
            print(line)
            print("TOTAL ICE COUNT:", total_ice_counter)

