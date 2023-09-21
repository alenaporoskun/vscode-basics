from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання

    users2 = {}
    names_monday, names_tuesday, names_wednesday, names_thursday, names_friday  = [], [], [], [], []
    count_people = 0
    for user in users:

        print(user)
        name = user['name']
        name = name.split()[0]
        print('name ', name)


        today = date.today()
        print('today', today)
        #print('today.strftime("%w")', today.strftime('%w'))

        new_day = today + timedelta(days=(7))
        print('new_day', new_day)

        new_day_week = new_day.strftime('%A')
        print('today_day_week ', new_day_week)

        birthday = user['birthday']
        if birthday.year <= today.year:
            birthday = birthday.replace(year = today.year)
            
        print('birthday ', birthday)
        birthday_day_week = birthday.strftime('%A')
        print('birthday_day_week ', birthday_day_week)


        delta = birthday - today
        delta2 = new_day
        delta2 = delta2 
        print('delta ', delta)
        print('delta2 ', delta2)
        if delta.days >= 0:
            if birthday_day_week == 'Monday' or birthday_day_week in ('Saturday', 'Sunday'):
                names_monday.append(name)

            if birthday_day_week == 'Tuesday':
                names_tuesday.append(name)

            if birthday_day_week == 'Wednesday':
                names_wednesday.append(name)

            if birthday_day_week == 'Thursday':
                names_thursday.append(name)

            if birthday_day_week == 'Friday':
                names_friday.append(name)


    users2['Monday']     = names_monday
    users2['Tuesday']    = names_tuesday
    users2['Wednesday']  = names_wednesday
    users2['Thursday']   = names_thursday
    users2['Friday']     = names_friday


    for key, value in users2.items():
        if len(value) != 0:
            count_people += 1
    print(users2)

    if count_people == 0:
        return {}
    
    #print('-'*10)

    return users2 # users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
        
