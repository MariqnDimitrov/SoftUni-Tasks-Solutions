word1, word2 = input().split()
total_sum = 0
if len(word1) > len(word2):
    for letter in range(len(word2)):
        total_sum += ord(word1[letter]) * ord(word2[letter])
    for remaining_letters in range(len(word2), len(word1)):
        total_sum += ord(word1[remaining_letters])
elif len(word2) > len(word1):
    for letter in range(len(word1)):
        total_sum += ord(word2[letter]) * ord(word1[letter])
    for remaining_letters in range(len(word1), len(word2)):
        total_sum += ord(word2[remaining_letters])
else:
    for letter in range(len(word1)):
        total_sum += ord(word2[letter]) * ord(word1[letter])
print(total_sum)