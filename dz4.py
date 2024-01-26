from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.28"},
    {"name": "Maria Tramp", "birthday": "1988.01.30"},
    {"name": "Jon Snow", "birthday": "1965.02.01"}
]

def get_upcoming_birthdays(users=None):
    today=datetime.today().date()
    birthday = []
    for user in users:
        birth_date = user["birthday"]
        birth_date = str(today.year)+birth_date[4:]
        birth_date = datetime.strptime(birth_date, "%Y.%m.%d").date()
        week_day = birth_date.weekday()
        days_difference = (birth_date-today).days
        if birth_date < today:
            birth_date = birth_date + timedelta(days=366)
        if 0<days_difference<7:
            if week_day<5:
                birthday.append({'name': user['name'], 'birthday': birth_date.strftime("%Y.%m.%d")})
            elif week_day==5:
                birth_date=(birth_date+timedelta(days=2))
                birthday.append({'name': user['name'], 'birthday': birth_date.strftime("%Y.%m.%d")})
            else:
                birth_date=(birth_date+timedelta(days=1))
                birthday.append({'name': user['name'], 'birthday': birth_date.strftime("%Y.%m.%d")})
    return birthday

print(get_upcoming_birthdays(users))
        
