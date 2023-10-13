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
        elapsed_time = datetime.now() - startup_time

        print(f'Elapsed time: {elapsed_time}')
        focused_multiplier = int(input('On a scale of 0 to 10, how focused were you during those time:'))/10
        final_elapsed_time_in_seconds = focused_multiplier * elapsed_time.total_seconds()
        final_elapsed_time = timedelta(seconds=final_elapsed_time_in_seconds)

        write_today(final_elapsed_time)
        print(f'{final_elapsed_time} has been written to {today}.txt')

        continue_execution = input('Press [Y] to start a new timer or any other key to stop: ').upper()
        if continue_execution != 'Y':
            print('Stopping timer...')
            break
        print('Starting new timer...')


start_menu()
