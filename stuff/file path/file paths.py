with open("file_to_read.txt") as da_file:
    insides = da_file.read()
    print(insides)

with open("file_to_read.txt", mode="a") as writing_to_this:
    writing_to_this.write("\nI wrote this in here")

with open("extra.txt", "w") as extra:
    extra.write(f"this is extra")

with open("extra.txt") as da_file:
    insides = da_file.read()
    print(insides)

