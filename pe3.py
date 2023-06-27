def encode(input_text, shift):
    alphabet_list = list("abcdefghijklmnopqrstuvwxyz")

    encoded_text = ""

    for char in input_text:
        if char.isalpha():
            index = alphabet_list.index(char.lower())
            encoded_index = (index + shift) % 26
            encoded_char = alphabet_list[encoded_index]
            encoded_text += encoded_char
        else:
            encoded_text += char

    return alphabet_list, encoded_text

print(encode("a", 3))
print(encode("abc", 4))
print(encode("xyz", 3))
print(encode("j!K, 2?", 3))


def decode(input_text, shift):
    alphabet_list = list("abcdefghijklmnopqrstuvwxyz")

    decoded_text = ""

    for char in input_text:
        if char.isalpha():
            index = alphabet_list.index(char.lower())
            decoded_index = (index - shift) % 26
            decoded_char = alphabet_list[decoded_index]
            decoded_text += decoded_char
        else:
            decoded_text += char
            
    return decoded_text

print(decode("d", 3))
print(decode("efg", 4))
print(decode("abc", 3))
print(decode("m!n, 2?", 3))


import datetime

class BankAccount:
    def __init__(self, name="Clocks", ID="123", creation_date=datetime.date.today(), balance=0):
        if creation_date > datetime.date.today():
            raise Exception("Creation date cannot be in the future.")
        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        pass
    
    def view_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        six_months_ago = self.creation_date + datetime.timedelta(days=6 * 30)
        if datetime.date.today() >= six_months_ago:
            if self.balance >= amount:
                self.balance -= amount
            else:
                raise Exception("Not enough balance.")
        else:
            raise Exception("Cannot withdraw before 6 months.")


class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            if self.balance < 0:
                self.balance -= 30
        else:
            raise Exception("Not enough balance.")
