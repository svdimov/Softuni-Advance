class Profile:
    def __init__(self, username: str, password: str):
        self.password = password
        self.username = username

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if  len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_len_word = len(value) >= 8
        contain_upper_letter = any([l for l in value if l.isupper()])
        digit = any([d for d in value if d.isdigit()])
        if not is_len_word or not contain_upper_letter or not digit:
            raise ValueError("The password must be"
                             " 8 or more characters with at least 1 digit "
                             "and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.__password)}'



correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)