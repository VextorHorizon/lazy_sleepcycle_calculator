from function import main_calculator

while True:
    try:
        sleep_time = input("Sleep time (HH:MM): ")
    except:
        print("Not a string!")
        continue
    wake_time = main_calculator(sleep_time)
    print("Recommend wake time(every 90 minute): ")
    for t in wake_time:
        print("-", t)

