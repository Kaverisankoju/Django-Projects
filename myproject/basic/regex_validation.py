import re
def validate(username,email,password):
    username_regex = r'^[A-Za-z0-9_]{6,15}$'
    # email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2,}$'  (or),
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    password_regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'
    
    return {
        "username":"Valid" if re.match(username_regex,username) else "Invalid",
        "email":"Valid" if re.match(email_regex,email) else "Invalid",
        "password":"Valid" if re.match(password_regex,password) else "Invalid"
    }
    
print(validate("user_123","test@gmail.com","Pass@123"))
    