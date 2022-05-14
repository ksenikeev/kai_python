from threading import Thread
import threading
import time
work_time = [5, 10, 2, 5, 3]

def work0():
    print("Start work 0")
    time.sleep(work_time[0])
    print("End work 0")

def work1():
    print("Start work 1")
    time.sleep(work_time[1])
    print("End work 1")

def work2():
    print("Start work 2")
    time.sleep(work_time[2])
    print("End work 2")

def work3():
    print("Start work 3")
    time.sleep(work_time[3])
    print("End work 3")

def work4():
    print("Start work 4 from " + threading.current_thread().name)
    time.sleep(work_time[4])
    print("End work 4")

def work0():
    print("Start work 0")
    time.sleep(work_time[0])
    print("End work 0")

if __name__ == "__main__":
    threads = []
    thread0 = Thread(target=work0)
    threads.append(thread0)
    thread0.start()

    thread1 = Thread(target=work1)
    threads.append(thread1)
    thread1.start()

    thread2 = Thread(target=work2)
    threads.append(thread2)
    thread2.start()

    thread3 = Thread(target=work3)
    threads.append(thread3)
    thread3.start()

    thread4 = Thread(target=work4)
    threads.append(thread4)
    thread4.start()

    # instantiating threadess with arguments
    #thread = threadess(target=t_func, args=(name,))
    #threads.append(thread)
    #thread.start()

    for thread in threads:
        thread.join()

    print("finish")
