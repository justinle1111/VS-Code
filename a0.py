squares = int(input())
print("+-+")
print("| |")
indent_index = ""
plus = "+-+-+"
line = "| |"
for i in range(squares - 1):
    print(indent_index + plus)
    indent_index += "  "
    print(indent_index + line)
print(indent_index + "+-+")