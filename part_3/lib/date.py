from datetime import datetime

class DateConvertor:
    def __init__(self,date_char):
        self.date_char = date_char

    def convert_to_date(self):
        date = self.date_char[34:36] + "20" + self.date_char[39:40]
        return datetime.strptime(date, "%d%m%Y")
