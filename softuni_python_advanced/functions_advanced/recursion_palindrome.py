def palindrome(word , index):
    is_palindrome = False
    if word[index] == word[-(index + 1)]:
        is_palindrome = True
    if not is_palindrome:
        return f"{word} is not a palindrome"
    if index == (len(word) // 2) - 1:
        return f"{word} is a palindrome"
    return palindrome(word, index + 1)

print(palindrome("peter", 0))



