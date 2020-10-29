from datetime import datetime
class Schedule:
    def __init__(self):
        self.classTimes = [('7:30','8:30'), ('8:35','9:35'), ('9:40','0:40'), ('10:45','11:45'), ('11:45','12:15'), ('2:15', '12:25'), ('12:30','12:50'), ('12:55','13:15'),('13:20', '13:40'), ('13:45','14:05')]

        self.cassNames = {"a":["Computer Science", "Web Design", "Spanish 3 Honors", "AP Physics 1", "Lunch", "Office Hours",
                             "Computer Science", "Web Design", "Spanish 3 Honors", "AP Physics 1" ],
                           "b":["PE", "Geometry Honors", "US 1 Honors", "English Honors", "Lunch", "Office Hours","PE",
                               "Geometry Honors", "US 1 Honors", "English Honors",]}
        self.className = ""
        self.schoolDay = "a"
        self.blockNumber = 0
        self.current_time = "8:47"

    # will your inputs be in military time?
    # do the "<" and ">" operators really let you compare the time how you want?
    # would a helper function to compare any two given times help?
    def current_class(self, current_time, schoolDay):
        for blockNumber, classTime in enumerate(self.classTimes):
                print('wen:', classTime)
                start_time = datetime.strptime(classTime[0], "%H:%M")
                end_time = datetime.strptime(classTime[1], "%H:%M")
                current_time = datetime.strptime(current_time, "%H:%M")
                print(self.classTimes[0][0])
                print(f'iteration {blockNumber}')
                if current_time >= start_time and current_time <= end_time: # if we find the interval that current_time falls in
                    print('case 1')
                    classame = self.classNames[schoolDay][blockNumber]
                    print(className)
                    break
                elif current_time > datetime.strptime(self.classTimes[-1][1], "%H:%M") and current_time < datetime.strptime("23:59", "%H:%M"): # late afternoon/evening, AFTER classes case
                    print('case 2')
                    print ("School has ended for the day.")
                    break
                elif current_time <= datetime.strptime("00:00", "%H:%M") and current_time >= self.classTimes[0][0]: # early morning, BEFORE classes case
                    print('case 3')
                    print ("School hasn't started yet.")
                    break
s = Schedule()
s.current_class("7:05", 'a')
