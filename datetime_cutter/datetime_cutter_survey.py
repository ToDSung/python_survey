from datetime import datetime, timedelta
start_date = '2011-05-18'
end_date = '2015-12-31'

def cut_datetime(start_date, end_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    for n in range(int ((end_date - start_date).days)):
        if n % 365 == 0: 
            yield start_date + timedelta(n)
    else:
        yield end_date
# for i in cut_datetime(start_date, end_date):
#     print(i)

a = [datetime.strftime(i, '%Y-%m-%d') for i in cut_datetime(start_date, end_date)]
print(a)