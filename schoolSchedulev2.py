class Schedule: 
    def __init__(self):
        self.classTimes = [('7:30','8:30'), ('8:35','9:35'), ('9:40','10:40'), ('10:45', '11:45'), ('11:45', '12:15'), 
                            ('12:15', '12:25'), ('12:30', '12:50'), ('12:55', '13:15'),('13:20', '13:40'), ('13:45', '14:05')]

        self.classNames = {"a":["Computer Science", "Web Design", "Spanish 3 Honors", "AP Physics 1", "Lunch", "Office Hours",
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
                start_time = classTime[0]
                end_time = classTime[1]
                if current_time >= start_time or current_time <= end_time: # if we find the interval that current_time falls in
                    className = self.classNames[schoolDay][blockNumber]
                    print(className)
                    break
                elif current_time > self.classTimes[-1][1] and current_time < "23:59": # late afternoon/evening, AFTER classes case
                    print("School has ended for the day.")
                    break
                elif current_time < "00:00" and current_time > self.classTimes[0][0]: # early morning, BEFORE classes case
                    print("School hasn't started yet.")
                    break
                
