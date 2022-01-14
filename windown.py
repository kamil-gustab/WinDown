import os


def date():
    date = os.system('cmd /c "date"')
    return date

def shutdown(time=60, force=False, restart=False):
    ''' Shutting down computer after time (seconds) provided as argument '''
    os.system(f'cmd /c "shutdown /c "Usage of WinDown app." /d u /s /f /t {time}"')


if __name__ == '__main__':

    print(shutdown(600))
