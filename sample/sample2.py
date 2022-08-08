#import calendar, math
from calendar import TextCalendar

# 日曜スタートでTextCalendarのインスタンスを生成
cal = TextCalendar(6)
cal.prmonth(2022, 1, w=5)