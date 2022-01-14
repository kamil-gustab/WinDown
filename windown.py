import os
from time import sleep


def date():
    return os.system('cmd /c "date"')


def shutdown(time=60, force=False, restart=False):
    """Shutting down computer after time (seconds) provided as argument"""

    time_in_mins = "less than 1" if time < 60 else int(time/60)
    comment = f'Computer will be turned off in {time_in_mins} min. Usage of WinDown app.'
    command = f'"shutdown /c "{comment}" /s /f /t {time}"'

    os.system(f'{command}')

    sleep(5)
    os.system('shutdown -a')


if __name__ == '__main__':

    shutdown(40)
