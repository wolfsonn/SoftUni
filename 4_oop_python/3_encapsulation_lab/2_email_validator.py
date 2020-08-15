class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __validate_name(self, name):
        if len(name) >= self.min_length:
            return True
        else:
            return False

    def __validate_mail(self, mail):
        if mail in self.mails:
            return True
        else:
            return False

    def __validate_domain(self, domain):
        if domain in self.domains:
            return True
        else:
            return False

    def validate(self, email):
        m = self.__validate_mail(email[email.find('@') + 1:email.find('.')])
        n = self.__validate_name(email[0:email.find('@')])
        d = self.__validate_domain(email[email.find('.') + 1:])
        if m and n and d:
            return True
        else:
            return False


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
