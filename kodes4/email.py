class InvalidEmail(Exception):
    def email_validation(email):
        if '@' not in email:
            raise Invalid_Email_Error(f"this mail{email} is invalid")
        return True

try:
    email_validation("user@gmail.com")
except Exception as e:
    print(e)