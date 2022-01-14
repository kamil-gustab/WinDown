import os
from time import sleep


def shutdown(time=60, force=False, restart=False):
    """Shutting down computer after time (seconds) provided as argument"""

    formatted_time = f'{time} sec' if time < 60 else f'{int(time/60)} min'
    comment = f'Computer will be turned off in {formatted_time}. Usage of WinDown app.'
    command = f'shutdown /c "{comment}" /t {time} /s /f'

    os.system(command)

    sleep(5)
    os.system('shutdown -a')


if __name__ == '__main__':

    shutdown(40)
