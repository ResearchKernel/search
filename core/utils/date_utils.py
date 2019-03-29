import datetime


def convert_date_to_es_format(date):
    try:
        datetime.datetime.strptime(date, '%d/%m/%Y')
    except ValueError:
        raise ValueError("Incorrect data format, should be DD-MM-YYYY")

    date_list = date.split('/')
    new_date = date_list[2] + '-' + date_list[1] + '-' + date_list[0]

    return new_date


def get_today_date():
    return datetime.datetime.today().strftime('%Y-%m-%d')