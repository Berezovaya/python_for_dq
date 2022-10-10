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
    News(txt='Something happened', city='London')
    Ad(txt='I want to sell a bike', exp_date='01/03/2023')
    Joke(txt="If I got 50 cents for every failed math exam, I'd have $6.30 now.", author="Vasya")
