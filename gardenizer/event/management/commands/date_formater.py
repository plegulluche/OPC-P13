from datetime import datetime


def convert_string_to_date_time_object(timestring):
    date_time_str = timestring
    seconds = ':00'
    full_date_time_str = date_time_str + seconds
    datetime_obj = datetime.strptime(full_date_time_str, f'%d/%m/%y %H:%M:%S')
    
    return datetime_obj

def convert_date_object_to_string(datetimeobj):
    time_obj = datetimeobj
    timestampstr = time_obj.strftime(f'%d/%m/%y %H:%M:%S')
    print("def time :" ,timestampstr)
    
    return timestampstr
    