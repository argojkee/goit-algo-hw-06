from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
           self.value = value

class Phone(Field):
    def __init__(self, value):
        try:
            assert len(value) >= 9, f"{value} can't be less than 10 symbols"
            self.value = value
        except AssertionError as e:
            print(e)

    def edit_value(self, value):
        try:
            assert len(value) >= 9, f"{value} can't be less than 10 symbols"
            self.value = value
        except AssertionError as e:
            print(e)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, value):
         self.phones.append(Phone(value))

    def edit_phone(self, old_phone, new_phone):
        try:
            phone = self.find_phone(old_phone)
            phone.edit_value(new_phone)
        except ValueError:
            print('Bad number')
    
    def find_phone(self, value):
        try:
            phone = [phone for phone in self.phones if phone.value == value]
            return phone[0]
        except (IndexError):
            print('Bad number')
    def remove_phone(self, value):
        try:
            phone = self.find_phone(value)
            self.phones.remove(phone)
        except ValueError:
            print('Bad number')
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        try:
            del self.data[name]
        except KeyError:
            print('Bad name')

    def find(self, name):
        try:
           return self.data[name]
        except (KeyError, IndexError):
            return None



