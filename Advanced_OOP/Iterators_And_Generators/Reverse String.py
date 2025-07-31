def reverse_text(text):
    curr_idx = len(text) - 1
    while curr_idx >= 0:
        yield text[curr_idx]
        curr_idx -= 1


for char in reverse_text("step"):
    print(char, end='')
