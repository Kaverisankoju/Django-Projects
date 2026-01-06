# # example pancard number validation
import re
# pattern = 'ABCDE1234F'
# # syntax = re.match(parttern,input)
# x = re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$',pattern)
# print(x)

# # match => checks only first of characters 
# ip = 'IND123'
# ip1= '123IND'
# x = re.match(r'IND',ip)
# y = re.match(r'IND',ip1)
# print(x)
# print(y)



# # search method is check for entire string ,if it finds in any where of string then (T)
# ip2 = 'python language is very easy'
# z = re.search(r'is',ip2)
# print(z)


# # phone number validation
# ip3 = '+919746268494'
# k = re.match(r'^\+91[6-9]\d{9}$',ip3)

# if k:
#     print('valid indian phone number ')
# else:
#     print('invalid indian phone number')


# phone number validation another way 
phone_pattern = r"^[6-9]{1}[0-9]{9}$"
ip = '5309313501'
b = re.match(phone_pattern,ip)
print(b)

# user name parttern 
username_pattern = r"^[A-Za-z0-9_]{8,15}$"
ip1 = 'userName99'
c = re.match(username_pattern,ip1)
print(c)

# password validation
password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[A-Za-z0-9@._]{9,12}"
password = 'India*123'
d = re.match(password_pattern,password)
print(d)