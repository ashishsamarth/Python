# Import datetime package
from datetime import datetime, timedelta, timezone, date


# Class definitions should use CamelCase convention based on pep-8 guidelines
class CustomDatetime:

    # Initialize the class
    # No argument needed
    def __init__(self):
        # Following line returns: - date format as 03-27-2022
        self.date_today_mm_dd_yyyy = datetime.now().strftime("%m-%d-%Y")
        # Following line returns: - date format as 2022-03-27
        self.date_today_yyyy_mm_dd = datetime.today().date()
        # Following line returns: - date format as 27-Mar-2022
        self.date_today_dd_mon_yyyy = datetime.now().strftime("%d-%b-%Y")
        # Following line returns: - date format as 27-March-2022
        self.date_today_dd_month_yyyy = datetime.now().strftime("%d-%B-%Y")
        # Following line returns: - date format as un-padded integer month
        self.date_today_m = datetime.today().month
        # Following line returns: - date format as padded integer month
        self.date_today_mm = datetime.now().strftime("%m")
        # Following line returns: - date format as string date today
        self.date_today_dd = datetime.now().strftime("%d")
        # Following line returns: - date format as integer year
        self.date_today_yyyy = datetime.today().year
        # Following line returns: - date format as string year
        self.date_today_yy = datetime.now().strftime("%y")
        # Following line returns: - 2022-03-27 22:57:33.730863 <class 'datetime.datetime'>
        self.today = datetime.today()
        # Following line returns: - mm-dd-yyyy as string
        self.utc_today_mm_dd_yyyy = datetime.utcnow().strftime("%m-%d-%Y")
        # Following line returns: - hh:mm:ss as string
        self.utc_time_fmt_24 = datetime.utcnow().strftime("%X")
        # Following line returns: - Current hour:minute:second as string
        self.time_fmt_12 = datetime.now().strftime("%I:%-M:%-S %p")
        # Following line returns: - Current hour:minute:second as string
        self.time_fmt_24 = datetime.now().strftime("%X")
        # Following line returns: - Current hour as string
        self.time_hr_fmt_12 = datetime.now().strftime("%I %p")
        # Following line returns: - Current hour as string
        self.time_hr_fmt_24 = datetime.now().strftime("%-H")
        # Following line returns: - Current day number of the year as string
        self.num_day_of_yr = datetime.now().strftime("%-j")
        # Following line returns: - date format as Sun Mar 27 22:52:59 2022 of class string
        self.local_time = datetime.now().strftime("%c")
        # Following line returns: - current day as string
        self.day = datetime.now().strftime("%A")

    # Method to convert integers to date
    # Arguments to this method are: - month (integer) and date (integer)
    # year is already fetch from the __init__ method
    def ref_date_curr_year(self, _mm, _dd):
        # Returns type: - datetime.date
        return date(self.date_today_yyyy, _mm, _dd)

    # Method to convert integers to date
    # Arguments to this method are: - year (integer), month (integer) and date (integer)
    @staticmethod
    def ref_date(_yyyy, _mm, _dd):
        # Returns type: - datetime.date
        return date(_yyyy, _mm, _dd)