from datetime import datetime


def convert_string_to_date_time_object(timestring):
    date_time_str = timestring
    date_processing = date_time_str.replace('T', '-').replace(':', '-').split('-')
    date_processing = [int(v) for v in date_processing]
    date_out = datetime(*date_processing)
    
    return date_out