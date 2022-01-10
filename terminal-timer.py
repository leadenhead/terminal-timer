import time
import threading
import os


class Timer:
    """ Timer """

    def __init__(self, desc='new', counts=1):
        self.start_time = time.time()
        self.duration = 0
        self.end_time = self.start_time + self.duration
        self.counts = counts
        self.description = desc

    def time_passed(self) -> float:
        return time.time() - self.start_time

    def time_remaining(self) -> float:
        return self.duration - self.time_passed()

    def get_end_time(self) -> float:
        return self.end_time

    def add_time(self, sec: float):
        self.duration += sec
        self.end_time = self.start_time + self.duration

    def restart_timer(self):
        self.start_time = time.time()

    def change_description(self):
        self.description = input(f'Enter new description for "{self.description}":\n: ')


def show_time(t: int) -> str:
    return time.strftime('%H:%M:%S', time.localtime(t))


def show_time2(t: int) -> str:
    print(t)
    return time.strftime('%H:%M:%S', time.gmtime(t))


def noname(seconds: int) -> str:
    if seconds <= 0:
        icon = '⏱'
    else:
        icon = '⏲'

    output = ''
    seconds = abs(round(seconds))

    days = seconds // 86400
    if days > 0:
        seconds = seconds % 86400
        output += f'{days:2}d '

    hours = seconds // 3600
    if hours > 0:
        seconds = seconds % 3600
        output += f'{hours:02}:'

    minutes = seconds // 60
    if minutes > 0:
        seconds = seconds % 60
        output += f'{minutes:02}:{seconds:02}'
    else:
        output += f'{seconds}'

    return f'{output} {icon}'


def print_table(timers: list) -> None:
    os.system('clear') if os.name == 'posix' else os.system('cls')
    print('')
    print(f'{"pos":>4} |{"remaining":12} | {"duration":12} | {"description":20} | {"start time":12} | {"end time":12} | {"interval":8}')
    print('-' * 80)

    for t in timers:
        print(f'{timers.index(t):4} | {noname(t.time_remaining()):>12} | {noname(t.duration):>12} | {t.description:20} | '
              f'{show_time(t.start_time):12} | {show_time(t.get_end_time())}')
    # time.sleep(1)


timers = []
# while True:
#     thr1 = threading.Thread(target=print_table(timers))

while True:
    answer = input('> ')
    if answer == '':
        timers.append(Timer())
        for t in timers:
            print(t.start_time)
    elif answer == 's':
        print_table(timers)
    elif answer == 'd':
        timers.pop()
    elif answer == 'e':
        t.change_description()
    elif answer.isdigit():
        timers[-1].add_time(int(answer))
