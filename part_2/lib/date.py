from datetime import datetime

class DateConvertor:
    def __str__(self,date_value):
        self.date_value = date_value

    def convert_to_date(self):
        date0 = str(self.date_value)
        date1 = datetime.strptime(date0, "%d%m%y")
        return date1.date()
