import string
import random
from datetime import date, datetime


today = date.today()
now = datetime.now()

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    acc = input("Enter Name of Plateform For which you need Password : ")
    plen = int(input("Enter the length of the password : "))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    password = (''.join(s[0:plen]))
    print("Your Password is :")
    print(password)
    d2 = today.strftime("%B %d, %Y")
    f = open("password.txt", "a")
    f.write(f"Password generated for {acc} at {now} is {password}\n")
    f.close()
