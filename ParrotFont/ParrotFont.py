LETTER_HEIGHT = 7
ASCII_BOUND = 32


def read_letter_data(filename):
    file = open(filename)
    letters = []
    current_letter = []
    for line in file:
        if line != '\n':
            current_line = []
            for pixel in line:
                if pixel == '0' or pixel == '1':
                    current_line.append(int(pixel))
            current_letter.append(current_line)
        else:
            letters.append(current_letter)
            current_letter = []
    return letters


def read_user_input():
    message = input("Input your message: ")
    background = input("Input your background emoji: ")
    foreground = input("Input your foreground emoji: ")
    return message, background, foreground


def write_parrots(message, background, foreground, letters):
    output_file = open("Parrots.txt", 'w')
    for row in range(LETTER_HEIGHT):
        for letter in message:
            for pixel in letters[ord(letter) - ASCII_BOUND][row]:
                if pixel == 0:
                    output_file.write(":" + background + ":")
                elif pixel == 1:
                    output_file.write(":" + foreground + ":")
        output_file.write("\n")


def main():
    letters = read_letter_data('letters.txt')
    message, background, foreground = read_user_input()
    write_parrots(message, background, foreground, letters)


if __name__ == "__main__":
    main()
