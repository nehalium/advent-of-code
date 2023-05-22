import datetime


def run_file(date):
    year = date.year
    day = date.day
    file = '../{year}/day-{day}/challenge1.py'.format(year=year, day=day)
    with open(file) as f:
        code = compile(f.read(), file, 'exec')
        exec(code)


if __name__ == '__main__':
    pass
    # run_file(datetime.datetime.now())
