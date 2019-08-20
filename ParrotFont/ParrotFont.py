LETTER_HEIGHT = 7


def read_letter_data(filename):
    file = open(filename)
    letters = []
    current_letter = []
    for line in file:
        if line != '\n':
            current_letter.append(line.split())
        else:
            letters.append(current_letter)
            current_letter = []
    return letters


def read_user_input():
    message = input("Input your message (lowercase only): ")
    background = input("Input your background emoji: ")
    foreground = input("Input your foreground emoji: ")
    return message, background, foreground


def print_parrots(message, background, foreground, letters):
    pass


def main():
    letters = read_letter_data('letters.txt')
    message, background, foreground = read_user_input()


if __name__ == "__main__":
    main()
