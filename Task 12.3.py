import csv


def write_contacts_to_file(filename, contacts):
    print(contacts)
    with open(filename, 'w', newline='') as fh:
        field_names = [str(i) for i in contacts[0].keys()]
        writer = csv.DictWriter(fh, fieldnames=field_names)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)


def read_contacts_from_file(filename):
    contacts = []
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            favorite = row['favorite'] == 'True'
            contact = {
                "name": row['name'],
                "email": row['email'],
                "phone": row['phone'],
                "favorite": favorite
            }
            contacts.append(contact)

    return contacts


contacts = [{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False},
            {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False}]
filename = 'file.dat'
write_contacts_to_file(filename, contacts)
print(read_contacts_from_file(filename))   