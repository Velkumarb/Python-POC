#Python Schedule is the inbuilt package in python

#Schedule is in-process scheduler for periodic jobs that use the builder pattern for configuration. 
# Schedule lets you run Python functions (or any other callable) periodically at pre-determined intervals using a simple, human-friendly syntax.
#Schedule Library is used to schedule a task at a particular time every day or a particular day of a week.

# import schedule
# import time
 
# # Functions setup
# def sudo_placement():
#     print("Get ready for Sudo Placement at DS")
 
# def good_luck():
#     print("Good Luck for Test")
 
# def work():
#     print("Study and work hard")
 
# def bedtime():
#     print("It is bed time go rest")
     
# def ds():
#     print("Shaurya says DS")
 
# # Task scheduling
# # After every 10mins geeks() is called.
# schedule.every(1).minutes.do(geeks)
 
# # After every hour geeks() is called.
# schedule.every().hour.do(ds)
 
# # Every day at 12am or 00:00 time bedtime() is called.
# schedule.every().day.at("00:00").do(bedtime)
 
# # After every 5 to 10mins in between run work()
# schedule.every(5).to(10).minutes.do(work)
 
# # Every monday good_luck() is called
# schedule.every().monday.do(good_luck)
 
# # Every tuesday at 18:00 sudo_placement() is called
# schedule.every().tuesday.at("18:00").do(sudo_placement)
 
# Loop so that the scheduling task
# keeps on running all time.
while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)

