import string
import random
from datetime import date, datetime


today = date.today()
now = datetime.now()

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    # print(s1)
    s2 = string.ascii_uppercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)
    plen = int(input("Enter the length of the password\n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    random.shuffle(s)
    password = (''.join(s[0:plen]))
    print("Your Password is :")
    print(password)

    d2 = today.strftime("%B %d, %Y")
    

    f = open("password.txt", "a")
    f.write(f"New Password generated at {now} is {password}\n")
    f.close()
