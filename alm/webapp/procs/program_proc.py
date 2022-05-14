from multiprocessing import Process
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
    print("Start work 4")
    time.sleep(work_time[4])
    print("End work 4")

def work0():
    print("Start work 0")
    time.sleep(work_time[0])
    print("End work 0")

if __name__ == "__main__":
    procs = []
    proc0 = Process(target=work0)
    procs.append(proc0)
    proc0.start()

    proc1 = Process(target=work1)
    procs.append(proc1)
    proc1.start()

    proc2 = Process(target=work2)
    procs.append(proc2)
    proc2.start()

    proc3 = Process(target=work3)
    procs.append(proc3)
    proc3.start()

    proc4 = Process(target=work4)
    procs.append(proc4)
    proc4.start()

    # instantiating process with arguments
    #proc = Process(target=t_func, args=(name,))
    #procs.append(proc)
    #proc.start()

    for proc in procs:
        proc.join()