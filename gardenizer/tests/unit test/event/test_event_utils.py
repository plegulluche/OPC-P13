import datetime
from event.utils import convert_string_to_date_time_object as cstdt


def test_utils_str_to_dt_converter():
    time_string = "2022-03-28T19:51"
    date_out = cstdt(time_string)
    expected_result = datetime.datetime(2022, 3, 28, 19, 51)
    assert date_out == expected_result
