# A1 for COMPSCI340/SOFTENG370 2015
# Prepared by Robert Sheehan
# Modified by ...

# You are not allowed to use any sleep calls.

from threading import Lock, Event
from process import State

class Dispatcher():
    """The dispatcher."""

    MAX_PROCESSES = 8
    TOP_OF_STACK = 0

    def __init__(self):
        """Construct the dispatcher."""
        # ...

        #runnable processes
        self.runnable_processes = []


        #waiting processes
        self.waiting_processes = []

    def set_io_sys(self, io_sys):
        """Set the io subsystem."""
        self.io_sys = io_sys

    def add_process(self, process):
        """Add and start the process."""
        # ...
        


        self.runnable_processes.append(process)

        self.io_sys.allocate_window_to_process(process, self.TOP_OF_STACK)
        process.event.set()

        if self.TOP_OF_STACK > 1:
            for i in range (0, len(self.runnable_processes) - 2 ):
                self.runnable_processes[i].event.clear()

        process.start()
        self.TOP_OF_STACK += 1 

    def dispatch_next_process(self):
        """Dispatch the process at the top of the stack."""
        # ...

        #check if there is anything to dispatch
        if len(self.runnable_processes) == 0:
            pass
        elif len(self.runnable_processes) == 1:
            self.runnable_processes[len(self.runnable_processes) -1].event.set()
        else:
            self.runnable_processes[len(self.runnable_processes) -2].event.set()

        
        


    def to_top(self, process):
        """Move the process to the top of the stack."""
        # ...


    def pause_system(self):
        """Pause the currently running process.
        As long as the dispatcher doesn't dispatch another process this
        effectively pauses the system.
        """
        # ...

    def resume_system(self):
        """Resume running the system."""
        # ...

    def wait_until_finished(self):
        """Hang around until all runnable processes are finished."""
        # ...

    def proc_finished(self, process):
        """Receive notification that "proc" has finished.
        Only called from running processes.
        """
        # ...

        #deallacotee window
        self.io_sys.remove_window_from_process(process)
       
        #decrease stack size constant
        self.TOP_OF_STACK -= 1

        #remove from list

        #length of runnable_processes
        length = len(self.runnable_processes) 

        if process.id == self.runnable_processes[length - 1]: #checking if last index is to be removed
            #move window
            l = length -1
            self.move_processes(l)
            
            #delete from runnable list
            del self.runnable_processes[length -1]
        else:
            #move window
            l = length -2
            self.move_processes(l)
           
            #delete from runnable list
            del self.runnable_processes[length -2]

        self.dispatch_next_process()



    def proc_waiting(self, process):
        """Receive notification that process is waiting for input."""
        # ...

    def process_with_id(self, id):
        """Return the process with the id."""
        # ...
        return None

    def move_processes (self, blankWindowSpace):
        #move process from blank and below
        for i in range(blankWindowSpace, len(self.runnable_processes)):
            if i == len(self.runnable_processes) - 1:
                break
            else:
                self.io_sys.move_process(self.runnable_processes[i+1], blankWindowSpace)
                blankWindowSpace += 1



    
        
            

