import time

def timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_format = '{:02d}:{:02d}'.format(mins, secs)
        print(timer_format, end='\r')
        time.sleep(1)
        seconds -= 1
    
    print("Time's up!")

def main():
    try:
        seconds = int(input("Enter the time in seconds: "))
        timer(seconds)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
