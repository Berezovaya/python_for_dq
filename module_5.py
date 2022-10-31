import datetime as dt
import os


class Post:
    def __init__(self, header, txt):
        self.header = header
        self.txt = txt
        self.add_line(self.header)

    def post(self, *lines):
        with open("newsfeed.txt", "a") as file1:
            file1.write('\n'.join(lines) + '\n')
            file1.write("------------------------------")

    def add_line(self, header):
        line_length = 30 - len(header)
        self.header = '\n\n\n' + self.header + '-' * line_length


class News(Post):
    def __init__(self, txt, city):
        super().__init__(header='News ', txt=txt)
        self.city = city
        self.footer = ''
        self.add_date()
        self.post()

    def add_date(self):
        self.footer = f'{self.city}, {dt.datetime.now().strftime("%m/%d/%Y %H.%M")}'

    def post(self):
        super().post(self.header, self.txt, self.footer)


class Ad(Post):
    def __init__(self, txt, exp_date):
        super().__init__(header='Private Ad ', txt=txt)
        self.exp_date = exp_date
        self.footer = ''
        self.add_date()
        self.post()

    def add_date(self):
        self._date_diff = dt.datetime.strptime(self.exp_date, '%m/%d/%Y').date() - dt.date.today()
        self.footer = f'Actual until: {self.exp_date}, {self._date_diff.days} days left'

    def post(self):
        super().post(self.header, self.txt, self.footer)


class Joke(Post):
    def __init__(self, txt, author):
        super().__init__(header='Joke ', txt=txt)
        self.author = author
        self.footer = ''
        self.add_author()
        self.post()

    def add_author(self):
        self.footer = f'Author: {self.author}'

    def post(self):
        super().post(self.header, self.txt, self.footer)


class TextReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.lines = None
        self.read_file()
        self.process_lines()

    def read_file(self):
        with open(self.file_path, 'r') as file:
            self.lines = file.read().splitlines()

    def process_lines(self):
        try:
            for choice, info, additional_info in zip(*[iter(self.lines)] * 3):
                if choice == '1':
                    News(txt=info, city=additional_info)
                elif choice == '2':
                    Ad(txt=info, exp_date=additional_info)
                elif choice == '3':
                    Joke(txt=info, author=additional_info)
                elif choice not in ['1', '2', '3']:
                    raise Exception("\n---------------------Input file is not correct----------------\n")
        except Exception as err:
            print(err)
        else:
            os.remove(self.file_path)


t = TextReader('input.txt')

if __name__ == '__main__':
    while True:
        try:
            choice = input("\n--------------What post do you want to add? Please, choose: \n1 - News\n2 - "
                           "Advertising\n3 - Joke\n4 - Import file\n5 - Exit the program\n")
            if choice == '1':
                info = input('What happened? ')
                city = input('Please specify the city: ')
                News(txt=info, city=city)
            elif choice == '2':
                info = input('What do you want to sell? ')
                exp_date = input('Till when? ')
                Ad(txt=info, exp_date=exp_date)
            elif choice == '3':
                info = input('Tell us a joke! ')
                author = input('What is your name? ')
                Joke(txt=info, author=author)
            elif choice == '4':
                info = input('Enter path to file: ')
                TextReader(file_path=info)
            elif choice == '5':
                break
            elif choice not in ['1', '2', '3', '4', '5']:
                raise Exception("\n---------------------You must enter a number (1 or 2 or 3 or 4). "
                                "Press 5 to exit.----------------\n")
        except Exception as err:
            print(err)



