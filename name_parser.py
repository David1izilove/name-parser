import re
import os


class Finder:

    def __init__(self, text_file, names_list):
        self.text_file = text_file
        self.names_list = names_list

    def read_txt_file(self):
        """open and read txt file"""
        if not os.stat(self.text_file).st_size == 0:
            txt_file = open(self.text_file)
            return txt_file
        else:
            raise Exception('The text file is empty')

    def parser(self):
        """this method will find the names in the text file"""
        list_of_results = []
        for name in self.names_list:
            list_of_results.append((name + ' -> ' + '\n'))
            for line_number, line_text in enumerate(self.read_txt_file(), 1):
                if name in line_text:
                    matches = re.finditer(name, line_text)
                    matches_indexes = [match.start() for match in matches]
                    result = f"[lineNumber= {str(line_number)}, " \
                             f"charIndex= {','.join(str(index) for index in matches_indexes)}]"
                    list_of_results.append((result + '\n'))
        return ''.join(list_of_results)

    def result(self):
        if self.parser():
            return self.parser()
        else:
            return 'No results'


file_path = 'text.txt'
user_input = input('Enter name/s: ')
users_list = user_input.replace(' ', '').split(',')

finder = Finder(text_file=file_path, names_list=users_list)
print(finder.result())


