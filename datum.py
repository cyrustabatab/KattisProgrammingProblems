import datetime as dt



def datum():

    year = 2009


    day,month = map(int,input().split())

    

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    date = dt.datetime(day=day,month=month,year=year)


    print(days[date.weekday()])




datum()














