from datetime import datetime, timedelta
from calendar import HTMLCalendar
from event.models import Evenement
from account.models import Account

class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()
        
    #format day as a td
    #filter events by day
    def formatday(self,day,events):
        events_per_day = events.filter(event_start__day=day)
        d = ""
        for event in events_per_day:
            d += f'<li> {event.title} <li>'
            
        if day != 0:
            return f'<td><span class="date">{day}</span><ul> {d} </ul></td>'
        return '<td></td>'
    
    #format a week as tr
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'
    
    #format a month as a table
    #filter events by year and month
    def formatmonth(self,userid,withyear=True):
        user = Account.objects.get(pk=userid)
        events = Evenement.objects.filter(event_start__year=self.year, event_start__month=self.month,user=user)
        print('Event month :',events)
        print('Month : ',self.month,'Year :',self.year)
        
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal