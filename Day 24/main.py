# # with open("my_file.txt") as file:
# #     contents = file.read()
# #     print(contents)
# #
# with open("my_file.txt", mode="w") as file:
#     contents = file.write("New text.")
#     print(contents)
PLACEHOLDER = "[name]"

with open("invited_names.txt", "r") as file:
    names = file.readlines()

with open("starting_letter1.docx") as letter:
    letter_content = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"{stripped_name}.docx", mode = "w") as completed_letter:
            completed_letter.write(new_letter)

