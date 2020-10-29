from datetime import datetime


'''
1) Input what school day (A/B) it is today
2) Give me the name of my current class depending on the current time and day of the week.
3) Give me the time until my next class, and maybe some other times if I feel like it
'''





'''
1) have a dictionary of tuples of start time and end time

2)have a current class in a loop that keeps track of what class using time comparison
(until current_time is greater than blockNumber end time and less than blockNumber start time; blockNumber += 1)
3)The current class function returns what calss I am in , the end time, how many minutes are left, and the name of the class.
  It will also take in the day(a or b) and return the classes based on that.
4)next_class gives me the start time of the class right after current class and the time until it starts.
5)If the final class end time is less than the current time: there are no more classes today
6) Maybe keep track of day of the week to say that there is no school on weekends and whether today is an a or b day

47) Have a 2 key dictionary of a and b with a list of all my classes, that will give me my current class depending on blockNumber
7)if current_time is greater than end time of blockNumber 1, blocknumber += 1
'''


class Schedule:
    def __init__(self):
        classTimes = [('7:30','8:30'), ('8:35','9:35'), ('9:40','10:40'), ('10:45', '11:45'), ('11:45', '12:15'), ('12:15', '12:25'), ('12:30', '12:50'), ('12:55', '13:15'),('13:20', '13:40'), ('13:45', '14:05')]
        classNames = {"a":["Computer Science", "Web Design", "Spanish 3 Honors", "AP Physics 1", "Lunch", "Office Hours", "Computer Science", "Web Design", "Spanish 3 Honors", "AP Physics 1" ], "b":["PE", "Geometry Honors", "US 1 Honors", "English Honors", "Lunch", "Office Hours","PE", "Geometry Honors", "US 1 Honors", "English Honors",]}
        className = ""
        schoolDay = "a"
        self.blockNumber = 0
        self.current_time = "8:47"
    #schoolDay = input("Is today an A day or a B day?")[0].lower()
    #current_time = datetime.now().time() # current time with seconds, datetime format
    #current_time = current_time.strftime("%H:%M") # converts current time to string from datetime and truncates seconds, used for finding what class I'm in
    def current_class():
        for classTime in classTimes:
            start_time = classTimes[blockNumber][0]
            end_time = classTimes[blockNumber][1]
            if current_time <= end_time and current_time >= start_time:
                className = classNames[schoolDay][blockNumber]
                print("Your current class is " + className + ", block " + str(blockNumber+1) + schoolDay.upper() + "." )
                break
            elif current_time > classTimes[-1][1] and current_time < "23:59":
                print("School has ended for the day.")
                blockNumber = 0
                break
            elif current_time < "00:00" and current_time > classTimes[0][0]:
                print("School hasn't started yet.")
                blockNumber = 0
                break                 #SOMETHING HERE IS GOING WRONG AND I CAN'T FIGURE IT OUT
            else:
                blockNumber += 1
        return blockNumber



    blockNumber = current_class() + 1
    ncurrent_time = datetime.strptime(str(current_time), "%H:%M")      #FIX AFTER CURRENT TIME  #office hours b
    def next_class():
        nextClassName = classNames[schoolDay][blockNumber]
        remaining_time =  datetime.strptime(classTimes[blockNumber][0], "%H:%M") - ncurrent_time
        remaining_time = remaining_time.total_seconds()//60
        # converts string back to datetime, this time without seconds
        if current_time > classTimes[-1][1] and current_time < "23:59":
                print("No more classes")
        else:
            print("Your next class, " + str(nextClassName) + "(" + str(blockNumber+1) + str(schoolDay.upper()) + ")" + ","" will start in " + str(int(remaining_time)) + " minutes.")
            print(blockNumber)
    next_class()
