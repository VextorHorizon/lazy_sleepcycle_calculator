import datetime

def main_calculator(sleep_time, cycle=6):
    base_time = datetime.datetime.strptime(sleep_time, "%H:%M")
    result = []
    for i in range (1, cycle+1):
        wake_time = base_time + datetime.timedelta(minutes=90*i)
        result.append(wake_time.strftime("%H:%M"))
    return result

