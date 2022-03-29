from calendar import monthrange
from datetime import datetime, timedelta
from django.shortcuts import render
from django.views import generic
from django.utils.safestring import mark_safe


from meteo.utils.meteo_data_manager import get_meteo_and_city_for_an_event
from .utils import Calendar
from event.models import Evenement
from account.models import Account


class CalendarView(generic.ListView):
    model = Evenement
    template_name = "cal/cal.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get("month", None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        userid = self.request.user.id

        html_cal = cal.formatmonth(userid, withyear=True)
        context["calendar"] = mark_safe(html_cal)
        context["prev_month"] = prev_month(d)
        context["next_month"] = next_month(d)

        return context


def get_date(req_month):
    if req_month:
        date_processing = (req_month + "-1-00-00").split("-")
        date_processing = [int(v) for v in date_processing]
        date_out = datetime(*date_processing)
        return date_out.date()
    return datetime.today()


def prev_month(d):
    """
    Function enabling us to use buttons to scroll backwards throught months to display
    other months for out calendar.
    """
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = "month=" + str(prev_month.year) + "-" + str(prev_month.month)
    return month


def next_month(d):
    """
    Function enabling us to use buttons to scroll onwards throught months to display
    other months for out calendar.
    """
    days_in_month = monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = "month=" + str(next_month.year) + "-" + str(next_month.month)
    return month


def single_day_view(request, month, day):
    """
    View that display events for a specific day from the calendar.
    """
    context = {}
    user = Account.objects.get(pk=request.user.id)
    events_for_day = Evenement.objects.filter(
        event_start__day=day, event_start__month=month, user=user
    )
    events_list = []
    for event in events_for_day:
        if event.category.title == "Chantier":
            events_list.append(event)
    meteo_codes = get_meteo_and_city_for_an_event(events_list, day)
    context["event_meteo"] = meteo_codes
    context["events"] = events_for_day
    return render(request, "cal/single_day.html", context)
