from datetime import datetime, timedelta
import os

today = datetime.now().strftime("%Y-%m-%d")


def read_today(today):
    if not os.path.exists(f'{today}.txt'):
        file = open(f'{today}.txt', 'w')
        file.close()
        return ['TOTAL_TIME:', '0:00:00', 'LOG:']

    file = open(f'{today}.txt', 'r')
    study_duration = file.read().split('\n')
    file.close()
    return study_duration


def calc_elapsed_time(stored, studied):
    elapsed_time = datetime.strptime(stored, "%H:%M:%S") + studied
    elapsed_time = elapsed_time.strftime("%H:%M:%S")
    return elapsed_time


def write_today(study_duration):
    global block
    today_data = read_today(today)

    today_data[1] = calc_elapsed_time(today_data[1], study_duration)
    today_data.append(
        f"Date {datetime.now().strftime('%m/%d/%Y, %H:%M:%S')} - Time Spent {str(study_duration).split('.')[0]}")

    today_data_string = '\n'.join(str(line) for line in today_data)

    file = open(f'{today}.txt', 'w')
    file.write(today_data_string)
    file.close()


def start_menu():
    print('Starting timer...')
    while True:
        startup_time = datetime.now()
        stop = input('Press enter to stop the timer')
        total_time = datetime.now() - startup_time

        write_today(total_time)

        continue_execution = input('Press [Y] to start a new timer or any other key to stop: ').upper()
        if continue_execution != 'Y':
            print('Stopping timer...')
            break
        print('Starting new timer...')


start_menu()
