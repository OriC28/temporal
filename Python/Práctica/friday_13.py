import datetime as dt

def has_friday_13(month, year):
	date = dt.datetime(year, month, 13)
	result: bool = True if date.strftime("%A") == 'Friday' else False
	return result



print(has_friday_13(8, 2024))