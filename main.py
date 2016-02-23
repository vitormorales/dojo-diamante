__author__ = 'vitor'


class Diamond():
    result = ''

    def __init__(self, char):
        self.build_diamond(char)

    def build_diamond(self, char):
        result = self.build_pyramid(char)
        lines = result.splitlines()[:-1]
        lines.reverse()

        result += ''.join(line+'\n' for line in lines)

        self.result = result
        print(result)

    def build_pyramid(self, char_deeper):
        char_list = [x for x in range(ord('A'), ord(char_deeper)+1)]

        max_line_length = ((ord(char_deeper)-ord('A')) * 2) + 1
        pyramid = ''

        for ch in char_list:
            distance = (ord(char_deeper)-ch)
            if ch == ord('A'):
                pyramid += (" " * distance + "A")
            else:
                internal_blanks = max_line_length - (distance * 2 + 2)
                pyramid += (" " * distance + chr(ch) + " " * internal_blanks + chr(ch))

            pyramid += "\n"
        return pyramid


def main():
    Diamond('E')


if __name__ == '__main__':
    main()