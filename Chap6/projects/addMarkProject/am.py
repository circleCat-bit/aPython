import pyperclip
text = pyperclip.paste()
#split it and add mark
lines = text.split("\n")
for i in range(len(lines)):
    lines[i] = "-" + lines[i]
new_text = "\n".join(lines)
pyperclip.copy(new_text)