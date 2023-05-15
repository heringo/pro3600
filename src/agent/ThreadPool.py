import threading
from queue import Queue
import time



#Les thresads sont des processus légers qui permettent d'exécuter des tâches en parallèle.
class ThreadPool:
    """ Thresads are lightweight processes that allow you to run tasks in parallel.
    
    
    Attributes
    ----------
    threads: Iterable[thread]
        Threads' stock
    is_busy: Iterable[thread]
        Indicate if a thread is occupied
    queue: Queue
        Stock to-do list
    condition: int
        The height if the map.
    is_busy: int
        Number of thread created (it depends of user's machine)
    is_busy: Iterable[boolean]
        List which indicate if the thread is occupied
        
    Methods
    -------

    __del__():
        Desctuctor called when the object is destroyed
    
    main_loop(i):
        Helper function used to convert real
        life coordinates to their graph representation.
        
    add_task(task_to_add):
        Helper function used to convert real
        life coordinates to their graph representation.
  
    """
    
    def __init__(self) -> None:
        """ Init creates nr_threads and launches them
        """
        
        self.threads = []                           
        self.is_busy = []                           
        self.queue = Queue()                        
        self.condition = threading.Condition()      

        nr_threads = threading.cpu_count()          

        self.is_busy = [False] * nr_threads         

        for i in range(nr_threads):
            thread = threading.Thread(target=self.main_loop, args=(i,))
            thread.start()
            self.threads.append(thread)

    def __del__(self) -> None:
        """ Desctuctor called when the object is destroyed
        """
        while True:
            idle_count = self.is_busy.count(False)      #Compte le nombre de threads 'False' Count the number of 'False' Threads

            if idle_count == len(self.is_busy):         #Threads unactive
                for thread in self.threads:
                    thread.join()                       #Stop the program until the thread is finished
                return

            time.sleep(1)

    def main_loop(self, i: int) -> None:
        """ The function is the main loop of a thread that retrieves tasks 
            from the queue, executes them, and updates the thread's busy status. 

        Args:
            i (int): Thread's number
        """
        while True:
            task = self.queue.get()

            if task is None:
                break

            self.is_busy[i] = True
            task()
            self.is_busy[i] = False

    def add_task(self, task_to_add) -> None:
        """ The function adds a task to the thread's queue 
            and unlocks the thread using a condition object

        Args:
            task_to_add (object): _description_
        """
        self.queue.put(task_to_add)
        with self.condition:                            
            self.condition.notify()                    
   
   