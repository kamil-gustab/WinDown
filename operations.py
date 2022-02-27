import os

def shutdown(time=60, force='', restart=''):
    """Shutting down computer after time (seconds) provided as an argument"""

    formatted_time = f'{time} sec' if time < 60 else f'{int(time/60)} min'
    comment = f'Computer will be turned off in {formatted_time}. Usage of WinDown app.'
    command = f'shutdown {force} {restart} /c "{comment}" /t {time} /s'
    # print(f'\n{command}\n')
    # eg. use case: shutdown(time=40, force='/f', restart='/r')

    os.system(command)
    return command

def cancel_shutdown():
    """Canceling queued shutdown by using "shutdown /a" """

    os.system('shutdown /a')