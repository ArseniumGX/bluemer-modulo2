class Contato:
    def __init__(self):
        self.__name = str()
        self.__email = str()
        self.__message = str()

    def __str__(self):
        return f'''{self.name}\n{self.email}\n{self.message}'''

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def message(self):
        return self.__message
    @message.setter
    def message(self, value):
        self.__message = value
