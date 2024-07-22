def concatenate(*args, **kwargs):
    concatenated_word = ""
    for word in args:
        concatenated_word += word
    for key, value in kwargs.items():
        if key in concatenated_word:
            concatenated_word = concatenated_word.replace(key, value)
    return concatenated_word

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))