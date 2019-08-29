class Patient():

    def __init__(self, first, last, social, birth, account, address):
        self.__first_name = first
        self.__last_name = last
        self.__social = social
        self.__birth = birth
        self.__account = account
        self.address = address


    @property # The getter
    def social(self):
        try:
            return self.__social # Note there are 2 underscores here
        except AttributeError:
            return "555-55-5555"
    
    @property
    def birth(self):
        try:
            return self.__birth # Note there are 2 underscores here
        except AttributeError:
            return "09-01-1989"

    @property
    def account(self):
        try:
            return self.__account # Note there are 2 underscores here
        except AttributeError:
            return "#123456"

    @property # The getter
    def full_name(self):
        try:
            return (f"{self.__first_name} {self.__last_name}") # Note there are 2 underscores here
        except AttributeError:
            return ""

    @property # The getter
    def address(self):
        try:
            return self.__address # Note there are 2 underscores here
        except AttributeError:
            return ""

    @address.setter # The setter
    def address(self, new_address):
        if type(new_address) is str:
            self.__address = new_address
        else:
            raise TypeError('Please provide a string for the address')

    

shane = Patient("Shane", "Miller", "555-123-4567", "09-01-1989", "#123456789", "123 Main Street.")
print(f"The patient, {shane.full_name}, lives at {shane.address}.")
print(f"* DOB: {shane.birth}")
print(f"* SS: {shane.social}")
print(f"* Account {shane.account}")

 



              