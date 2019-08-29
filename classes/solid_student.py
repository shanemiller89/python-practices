class Student():

    def __str__(self):
        return f"{self.full_name} is {self.age} and is in cohort {self.cohort}"    

    @property # The getter
    def first_name(self):
        try:
            return self.__first_name # Note there are 2 underscores here
        except AttributeError:
            return ""

    @first_name.setter # The setter
    def first_name(self, new_name):
        if type(new_name) is str:
            self.__first_name = new_name
        else:
            raise TypeError('Please provide a string for the first name')

    @property # The getter
    def last_name(self):
        try:
            return self.__last_name # Note there are 2 underscores here
        except AttributeError:
            return ""

    @last_name.setter # The setter
    def last_name(self, new_name):
        if type(new_name) is str:
            self.__last_name = new_name
        else:
            raise TypeError('Please provide a string for the last name')

    @property # The getter
    def age(self):
        try:
            return self.__age # Note there are 2 underscores here
        except AttributeError:
            return 0

    @age.setter # The setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError('Please provide a number for the age')

    @property # The getter
    def cohort(self):
        try:
            return self.__cohort # Note there are 2 underscores here
        except AttributeError:
            return 0

    @cohort.setter # The setter
    def cohort(self, new_cohort):
        if type(new_cohort) is int:
            self.__cohort = new_cohort
        else:
            raise TypeError('Please provide a number for the cohort')
            
    @property # The getter
    def full_name(self):
        try:
            return (f"{self.first_name} {self.last_name}") # Note there are 2 underscores here
        except AttributeError:
            return ""



shane = Student()
shane.first_name = "Shane"
shane.last_name = "Miller"
shane.age = 30
shane.cohort = 33

print(shane)