import re
from datetime import datetime

class Average(object):
    def __init__(self, lst):
        self.lst = lst
    def average(self):
        """ Function calculates the average of numbers stored in list lst """

        # average
        avg = float(sum(self.lst)) / len(self.lst)
        if avg < 6:
            print "Low Average"
        elif avg > 12:
            print "High Average"
        else:
            print "Medium Average"

    @classmethod
    def initWithString(cls):
        s_str = raw_input ("Enter a string of mixed letters and numbers: ")
        return cls([int(x) for x in re.findall("\d+",s_str)]) #create and return an instance of cls i.e. Average

def article(s_str):
    lst = s_str.split("/")
    date_string = lst[3]+"-"+lst[2]+"-"+lst[1]
    article_date = datetime.strptime(date_string, "%d-%m-%Y")
    d = datetime.today()
    diff = d - article_date
    return (lst[4],date_string,diff.days)

#d=article("articles/2010/10/21/my_summer")
#print d

#lst=[2,5,10,16]
#a=Average(lst)
#a.average()
#a=Average.initWithString()
#a.average()
