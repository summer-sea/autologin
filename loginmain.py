import findpageid
#if __name__ == "__main__":

    #from pyvirtualdisplay import Display

    #display = Display(visible=1, size=(1366, 768))
    #display.start()
    user1 = "李四"
    pw = "123"
    findpageid.login(user1, pw)

    user2 ="xiaoming0"
    findpageid.login(user2, pw)
    user3="xiaoming1"
    findpageid.login(user3, pw)


    #display.stop()