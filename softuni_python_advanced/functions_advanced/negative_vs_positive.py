def numbers_type(*args):
    negative_sum = 0
    positive_sum = 0
    for number in args:
        if number < 0:
            negative_sum += number
        elif number > 0:
            positive_sum += number
    print(negative_sum)
    print(positive_sum)
    if abs(negative_sum) > positive_sum:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


numbers = [int(x) for x in input().split()]
numbers_type(*numbers)

