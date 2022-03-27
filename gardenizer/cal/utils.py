from datetime import datetime, timedelta
from calendar import HTMLCalendar

from event.models import Evenement
from account.models import Account
from meteo.models import MeteoData


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
            d += f'<p class="calendar-event"> {event.title} <p>'
            
        if day != 0:
            return f'<td><span class="date"><a class="cal-link" href="day/{self.month}/{day}">{day}</a></span><ul> {d} </ul></td>'
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
        meteo = MeteoData.objects.all()
        events = Evenement.objects.filter(event_start__year=self.year, event_start__month=self.month,user=user)
        
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar" style="color:white;">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal