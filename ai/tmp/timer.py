
def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_format = f'{mins:02}:{secs:02}'
        print(timer_format, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

if __name__ == '__main__':
    try:
        total_seconds = int(input("Enter the time in seconds: "))
        countdown_timer(total_seconds)
    except ValueError:
