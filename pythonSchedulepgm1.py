#Python Schedule is the package in python

#Schedule is in-process scheduler for periodic jobs that use the builder pattern for configuration. 
# Schedule lets you run Python functions (or any other callable) periodically at pre-determined intervals using a simple, human-friendly syntax.
#Schedule Library is used to schedule a task at a particular time every day or a particular day of a week.

# Please note that it is *intended behavior that run_pending() does not run missed jobs*. 
# For example, if you've registered a job that should run every minute and you only call run_pending() 



import schedule
import time

def wish():
    print("Hello Everyone Welcome to Data Sirpi")

#While loop - If the condition is true the pgm will execute

while True: 
    schedule.every(1).seconds.do(wish) #schedule.every(1).seconds.do(func) function will call every 1 seconds. 
    schedule.run_pending() #And with the help schedule.run_pending() we will check whether the scheduler has a pending function to run or not.
    time.sleep(1)

    


