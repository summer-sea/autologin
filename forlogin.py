import findpageid

if __name__ == "__main__":
    pw ="123"
    for num in range(0,10):
        print(num)
        num = str(num)
        name= 'xiaoming'
        user =name+num
        print(user)
        findpageid.login(user, pw)