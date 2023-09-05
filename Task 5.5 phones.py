def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    new_phones = []
    for phone in list_phones:
        new_phones.append(sanitize_phone_number(phone))

    dict_pref = {
        'JP': '81',
        'SG': '65',
        'TW': '886',
        'UA': '380',
        'other': ''
    }

    dict = {}
    list_prefix = ['380', '81', '886', '65']
    phones = [[], [], [], []]

    for phone in new_phones:
        print(phone)
        count = 0
        j = 0
        for i, k in dict_pref.items():
            #print(f'{i} {k}')

            if dict_pref.get('c', -1)

            if len(k) == 2:
                if ((phone[:2].find(k) != -1) and (count < 1)):
                    print(f'{i} {k}')
                    if 
                    dict.update({i: [phone]})
                    count += 1

            if len(k) == 3:
                if ((phone[:3].find(k) != -1) and (count < 1)):
                    print(f'{i} {k}')
                    dict.update({i: [phone]})
                    count += 1

    return dict

list1 = ['380998759405', '818765347', '8867658976', '657658976']
list2 = ['0658759411', '818765347', '818765344', '8867658976', '657658976']
print(get_phone_numbers_for_countries(list2))
        
        
            
        
            
        
            
        
            
        
            
    