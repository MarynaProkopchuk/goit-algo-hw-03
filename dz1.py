from datetime import datetime

def get_days_from_today(date = input("Write the date ")):
    try:
        date = datetime.strptime(date, "%Y-%m-%d").toordinal()
        current_date = datetime.today().toordinal()
        if date <= current_date: 
           return current_date - date
        else:
            return (current_date - date)*(-1) 
    except ValueError:
        print(f"Please write {date} in YYYY-MM-DD format")
print(get_days_from_today())