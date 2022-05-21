import datetime as dt
import schedule
import time
import threading

print(dt.datetime.now())

print(dt.date.today())

def job():
    print("Работаю")

def start_s():
    schedule.every(2).seconds.do(job)
    # нужно иметь свой цикл для запуска планировщика с периодом в 1 секунду:
    while True:
        schedule.run_pending()
        time.sleep(1)

job_thread = threading.Thread(target=start_s, daemon=1)
job_thread.start()

print(threading.active_count())

time.sleep(10)
print(1)