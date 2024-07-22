cake_width = int(input())
cake_len = int(input())
cake = cake_len * cake_width
piece_count = 0
diff = 0
cake_diff = cake
while True:
    gotten_pieces = input()
    if gotten_pieces == "STOP":
        if cake_diff >= 0:
            print(f"{diff} pieces are left.")
            break
        else:
            print(f"No more cake left! You need {diff} pieces more.")
            break
    gotten_pieces = int(gotten_pieces)
    piece_count += gotten_pieces
    cake_diff -= gotten_pieces
    diff = abs(cake - piece_count)
    if cake_diff < 0:
        print(f"No more cake left! You need {diff} pieces more.")
        break