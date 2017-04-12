import _thread
import time,random
import threading

garfo = []
for i in range(5):
    garfo.append(threading.Semaphore(1))

def filosofo(f):
    f = int(f)
    comida = 100
    while comida != 0:
        #garfo da esquerda
        garfo[f].acquire()
        #garfo da direita
        garfo[(f+1) % 5].acquire()
        print("Filosofo "+str(f)+" está comendo\n")
        comida -= 1
        #time.sleep(random.randint(1,5))
        garfo[f].release()
        garfo[(f+1) % 5].release()
        print("Filosofo "+str(f)+" está pensando\n")
        #time.sleep(random.randint(1,10))

for i in range(5):
    _thread.start_new_thread(filosofo,tuple([i]))


