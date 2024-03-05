def count_vowels(word):
    count = 0
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for char in word:
        if char in vowel:
            count += 1
    return count