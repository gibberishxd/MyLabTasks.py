def delete_words_shorter_than_number(input_string, number):
    output = []
    words = input_string.split(" ")
    for word in words:
        letters = len(word)
        if letters >= number:
            output.append(word)
    return output


input_str = input("Enter your string \n")
number_of_letters = int(input("Enter the number of letters \n"))
output_words = delete_words_shorter_than_number(input_str, number_of_letters)
for longer_word in output_words:
    print(longer_word, end=" ")