# import time
# from multiprocessing import Process, process

# def task():
#     for i in range(5):
#         print(f"{i} running")
#         time.sleep(2)

# if __name__ == "__main__":
#     t1=Process(target=task)
#     t2=Process(target=task)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()

#     print("program end")

# import time
# from multiprocessing import Process, current_process

# def task():
#     for i in range(5):
#         print(f"{i} running in {current_process().name}")
#         time.sleep(1)

# if __name__ == "__main__":
#     t1 = Process(target=task)
#     t2 = Process(target=task)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()

#     print("program end")

# import time
# from multiprocessing import Process, current_process    
# def task():
#     for i in range(5):
#         print(f"{i} running in {current_process().name}")
#         time.sleep(3)   

import threading
import time
def task():
    for i in range(5):
        print(f"{i} running in downloading")
        time.sleep(3)

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)
t1.start()
t2.start()

t1.join()   
t2.join()
print("program end")  

# def task():
#     for i in range(5):
#         print(f"{i} running in {current_process().name}")
#         time.sleep(2)