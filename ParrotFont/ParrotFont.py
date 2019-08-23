LETTER_HEIGHT = 7


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
    # message = input("Input your message (lowercase only): ")
    # background = input("Input your background emoji: ")
    # foreground = input("Input your foreground emoji: ")
    # return message, background, foreground
    return "channel", "partyparrot", "parrotwave1"


def print_parrots(message, background, foreground, letters):
    for row in range(7):
        for letter in message:
            for pixel in letters[ord(letter) - 97][row]:
                if pixel == 0:
                    print(":" + background + ":", end='')
                elif pixel == 1:
                    print(":" + foreground + ":", end='')
        print()


def main():
    letters = read_letter_data('letters.txt')
    message, background, foreground = read_user_input()
    print_parrots(message, background, foreground, letters)


if __name__ == "__main__":
    main()
