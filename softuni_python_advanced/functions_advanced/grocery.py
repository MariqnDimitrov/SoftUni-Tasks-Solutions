def grocery_store(**kwargs):
    filtered_grocery = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    final_list = []
    for key, value in filtered_grocery.items():
        final_list.append(f"{key}: {value}")
    return "\n".join(final_list)

print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
