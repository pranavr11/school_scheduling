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
        self.classTimes = [('7:30','8:30'), ('8:35','9:35'), ('9:40','10:40'), ('10:45', '11:45'), ('11:45', '12:15'), ('12:15', '12:25'), ('12:30', '12:50'), ('12:55', '13:15'),('13:20', '13:40'), ('13:45', '14:05')]
        self.classNames = {"a":["Computer Science", "Web Design", "Spanish 3 Honors", "AP Physics 1", "Lunch", "Office Hours", "Computer Science", "Web Design", "Spanish 3 Honors", "AP Physics 1" ],
                            "b":["PE", "Geometry Honors", "US 1 Honors", "English Honors", "Lunch", "Office Hours","PE", "Geometry Honors", "US 1 Honors", "English Honors",]}
        className = ""
        self.schoolDay = "a"
        self.blockNumber = 0
        #current_time = datetime.now().time()
        self.current_time = "18:34"
        self.current_time = datetime.strptime(self.current_time, "%H:%M")

    #schoolDay = input("Is today an A day or a B day?")[0].lower()
     # current time with seconds, datetime format
 # converts current time to string from datetime and truncates seconds, used for finding what class I'm in
    def current_class(self, canPrint):
        for classTime in self.classTimes:
            start_time = datetime.strptime(self.classTimes[self.blockNumber][0], "%H:%M")
            end_time = datetime.strptime(self.classTimes[self.blockNumber][1], "%H:%M")
            final_class = datetime.strptime(self.classTimes[-1][1], "%H:%M")
            initial_class = datetime.strptime(self.classTimes[0][0], "%H:%M")
            self.ifGap = False

            #print('current_time:', self.current_time, 'start_time:', start_time, 'end_time:', end_time,
                        #'initial_class:', initial_class, 'final_class:', final_class)

            if self.current_time <= end_time and self.current_time >= start_time:
                className = self.classNames[self.schoolDay][self.blockNumber]
                if canPrint:
                    print("Your current class is " + className + ", block " + str(self.blockNumber+1) + self.schoolDay.upper() + "." )
                break
            elif self.current_time > final_class and self.current_time < datetime.strptime("23:59", "%H:%M"):
                if canPrint:
                    print("School has ended for the day.")
                self.blockNumber = 0
                break
            elif self.current_time >= datetime.strptime("00:00", "%H:%M") and self.current_time < initial_class:
                if canPrint:
                    print("School hasn't started yet.")
                self.blockNumber = 0
                break
            elif self.current_time >= end_time and self.current_time <= datetime.strptime(self.classTimes[self.blockNumber + 1][0], "%H:%M"):
                if canPrint:
                    print("This is the gap between " + self.classNames[self.schoolDay][self.blockNumber] + " and " + self.classNames[self.schoolDay][self.blockNumber+1])
                self.ifGap = True
                break
            else:
                # print('else case')
                self.blockNumber += 1
        return self.blockNumber



    # blockNumber = current_class() + 1
          #FIX AFTER CURRENT TIME  #office hours b
    def next_class(self):
        if self.ifGap:
            self.blockNumber = s.current_class(False)
            nextClassName = self.classNames[self.schoolDay][self.blockNumber+1]
            remaining_time =  datetime.strptime(self.classTimes[self.blockNumber+1][0], "%H:%M") - self.current_time
            remaining_time = remaining_time.total_seconds()//60

            if self.current_time > datetime.strptime(self.classTimes[-1][1], "%H:%M") and self.current_time < datetime.strptime("23:59", "%H:%M"):
                    print("No more classes")
            else:
                print("Your next class, " + str(nextClassName) + "(" + str(self.blockNumber+2) + str(self.schoolDay.upper()) + ")" + ","" will start in " + str(int(remaining_time)) + " minutes.")
                print(self.blockNumber)
        else:
            self.blockNumber = s.current_class(False)+1
            nextClassName = self.classNames[self.schoolDay][self.blockNumber]
            remaining_time =  datetime.strptime(self.classTimes[self.blockNumber][0], "%H:%M") - self.current_time
            remaining_time = remaining_time.total_seconds()//60
        # converts string back to datetime, this time without seconds
            if self.current_time > datetime.strptime(self.classTimes[-1][1], "%H:%M") and self.current_time < datetime.strptime("23:59", "%H:%M"):
                    print("No more classes.")
            else:
                print("Your next class, " + str(nextClassName) + "(" + str(self.blockNumber+1) + str(self.schoolDay.upper()) + ")" + ","" will start in " + str(int(remaining_time)) + " minutes.")


s = Schedule()
s.current_class(True) # STILL works for now
s.next_class()
