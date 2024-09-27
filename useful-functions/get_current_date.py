# Import the datetime module
from datetime import datetime
# Method to get the current date
def get_current_date():
    fmt = "%m/%d/%Y"
    return datetime.today().strftime(format=fmt)