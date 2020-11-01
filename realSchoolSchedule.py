from datetime import datetime

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
    def __init__(self)
    self.classTimes = [('7:30','8:30'), ('8:35','9:35'), ('9:40','10:40'), ('10:45', '11:45'), ('11:45', '12:15'), ('12:15', '12:25'), ('12:30', '12:50'), ('12:55', '13:15'),('13:20', '13:40'), ('13:45', '14:05')]
    self.classNames = {"a":["Computer Science", "Web Design", "Spanish 3 Honors", "AP Physics 1", "Lunch", "Office Hours", "Computer Science", "Web Design", "Spanish 3 Honors", "AP Physics 1" ],
                    "b":["PE", "Geometry Honors", "US 1 Honors", "English Honors", "Lunch", "Office Hours","PE", "Geometry Honors", "US 1 Honors", "English Honors",]}
    def current_class(self):
