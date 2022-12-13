#To Write a Python Program for Particular day and time the prgoram will run automatically

#Sched 
#time 

import schedule
import time

def villageofLearners():
    print("Monday to Friday Afternoon 2.30PM (IST) Village of Learners Team Meeting")

while True:   
    schedule.every().day.at("18:14").do(villageofLearners) 
    # schedule.every(1).seconds.do(villageofLearners)
    schedule.run_pending()
    time.sleep(1)


