def count_a(word, num_loops):
    looped_word = word * num_loops
    count = looped_word.count('a')
    return count

word = 'aha'
num_loops = 3
count = count_a(word, num_loops)
print(count)  # Output: 6