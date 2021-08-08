
mark_down = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line"]

output_text = []

while True:
    input_str = input("- Choose a formatter: ")

    if input_str == "!help":
        print("Available formatters: " + " ".join(mark_down))
        print("Special commands: !help !done")
    elif input_str == "!done":
        #"result.md"
        file = open(r"C:\Users\piotr\PycharmProjects\Markdown Editor\Markdown Editor\task\output.md", "w+")
        file.writelines(output_text)
        file.close()
        break
    elif input_str not in mark_down:
        print("Unknown formatting type or command. Please try again.")
    elif input_str in mark_down:

        input_text = None

        if input_str == "plain":
            input_text = input("- Text: ")

        elif input_str == "bold":
            text = input("- Text: ")
            input_text = '**' + text + '**'

        elif input_str == "italic":
            text = input("- Text: ")
            input_text = '*' + text + '*'

        elif input_str == "header":
            level = int(input("- Level: "))
            if level < 1 or level > 6:
                print("The level should be within the range of 1 to 6")
                pass
            text = input("- Text: ")
            input_text = ("#"*int(level)) + " " + text + "\n"

        elif input_str == "link":
            label = input("- Label: ")
            url = input("- URL: ")
            input_text = "[" + label + "]" + "(" + url + ")"

        elif input_str == "inline-code":
            text = input("- Text: ")
            input_text = "`" + text + "`"

        elif input_str == "ordered-list" or input_str == "unordered-list":

            while True:
                number_rows = int(input("- Number of rows: "))
                if number_rows < 1:
                    print("The number of rows should be greater than zero")
                else:
                    break

            index = 0
            while index < number_rows:
                index += 1
                row_text = input(f"- Row #{index}: ")
                if input_str == "ordered-list":
                    output_text.append(f"{index}. {row_text}\n")

                if input_str == "unordered-list":
                    output_text.append(f"* {row_text}\n")

            input_text = None

        elif input_str == "new-line":
            input_text = "\n"

        if input_text == "":
            pass

        if input_text is not None:
            output_text.append(input_text)
        print("".join(output_text))
