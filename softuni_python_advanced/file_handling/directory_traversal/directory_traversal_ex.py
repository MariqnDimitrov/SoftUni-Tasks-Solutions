import os
files = {}
directory = "../"
for element in os.listdir(directory):
    f = os.path.join(directory, element)
    if os.path.isfile(f):
        ext = element.split(".")[-1]
        if ext not in files:
            files[ext] = []
        files[ext].append(element)
    else:
        for el in os.listdir(f):
            file = os.path.join(f, el)
            if os.path.isfile(file):
                ext = el.split(".")[-1]
                if ext not in files:
                    files[ext] = []
                files[ext].append(el)
with open(os.path.join(directory, "report.txt"), "w") as f:
    for ext, filename in sorted(files.items()):
        f.write(f".{ext}\n")
        for file in sorted(filename):
            f.write(f"- - - {file}\n")


