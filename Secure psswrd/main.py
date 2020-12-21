SECURE=(('s','$'),('and','&'),('a','@'),('o','0'),('i','1'),('I','|'))

def securePsswrd(password):
    for i in SECURE:
        password= password.replace(a,b)

    return password





if __name__=="__main__":
    password =input("Enter your Password")
    password=securePsswrd(password)
    print(f"Your Secure Password is {password}")