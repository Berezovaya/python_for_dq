import datetime as dt


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


if __name__ == '__main__':
    while True:
        try:
            choice = input("\n--------------What post do you want to add? Please, choose: \n1 - News\n2 - "
                           "Advertising\n3 - Joke\n4 - Exit the program\n")
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
                break
            elif choice not in ['1', '2', '3', '4']:
                raise Exception("\n---------------------You must enter a number (1 or 2 or 3). "
                                "Press 4 to exit.----------------\n")
        except Exception as err:
            print(err)



