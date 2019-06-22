# Functions::::

# Diet Feed :::
def feed_diet():
    print("Harry (1).\nRohan (2).\nHammad (3).")
    dt_cl = int(input("Whome diet you want to feed : "))
    if dt_cl == 1:
        with open("harry_dt.txt", 'a') as f:
            fd = input("What you want to feed : ")
            f.write(f"\n[{getdate()}] : {fd}")
            print(f"{fd} : Feeded Successfully.")
    elif dt_cl==2:
        with open("rohan_dt.txt", 'a') as f:
            fd = input("What you want to feed : ")
            f.write(f"\n[{getdate()}] : {fd}")
            print(f"{fd} : Feeded Successfully.")
    elif dt_cl == 3:
        with open("hammad_dt.txt", 'a') as f:
            fd = input("What you want to feed : ")
            f.write(f"\n[{getdate()}] : {fd}")
            print(f"{fd} : Feeded Successfully.")
    else:
        print("Wrong input.")

# Exercise Feed :::
def feed_exrs():
    print("Harry (1).\nRohan (2).\nHammad (3).")
    dt_cl = int(input("Whome Exercise you want to feed : "))
    if dt_cl == 1:
        with open("harry_ex.txt", 'a') as f:
            fd = input("What you want to feed : ")
            f.write(f"\n[{getdate()}] : {fd}")
            print(f"{fd} : Feeded Successfully.")
    elif dt_cl == 2:
        with open("rohan_ex.txt", 'a') as f:
            fd = input("What you want to feed : ")
            f.write(f"\n[{getdate()}] : {fd}")
            print(f"{fd} : Feeded Successfully.")
    elif dt_cl == 3:
        with open("hammad_ex.txt", 'a') as f:
            fd = input("What you want to feed : ")
            f.write(f"\n[{getdate()}] : {fd}")
            print(f"{fd} : Feeded Successfully.")
    else:
        print("Wrong input.")

# Show Diet :::
def show_diet():
    print("Harry (1).\nRohan (2).\nHammad (3).")
    dt_cl = int(input("Whome Diet you want to see : "))
    if dt_cl==1:
        with open('harry_dt.txt','rt') as f:
            print(f.read())
    elif dt_cl==2:
        with open('rohan_dt.txt', 'rt') as f:
            print(f.read())
    elif dt_cl==3:
        with open('hammad_dt.txt', 'rt') as f:
            print(f.read())
    else:
        print("Wrong input.")


# Show Exercise :::
def show_ex():
    print("Harry (1).\nRohan (2).\nHammad (3).")
    dt_cl = int(input("Whome Exercise you want to see : "))
    if dt_cl == 1:
        with open('harry_ex.txt', 'rt') as f:
            print(f.read())
    elif dt_cl == 2:
        with open('rohan_ex.txt', 'rt') as f:
            print(f.read())
    elif dt_cl == 3:
        with open('hammad_ex.txt', 'rt') as f:
            print(f.read())
    else:
        print("Wrong input.")

# Returns Time :::
def getdate():
    import datetime
    return datetime.datetime.now()

# Main program::::
print("Helth management program : ")
lc_rt=int(input("What do you want (Enter 1 to lock or 2 to Retrive) : "))
if lc_rt==1:
    dt_ex=int(input('What do you want to lock (Enter 1 for diet or 2 for Exercise) : '))
    if dt_ex==1:
        feed_diet()
    elif dt_ex==2:
        feed_exrs()
    else:
        print("Wrong input.")

elif lc_rt==2:
    dt_ex_rt=int(input("What do you want to retrive (Enter 1 for diet or 2 for Exercise) : "))
    if dt_ex_rt==1:
        show_diet()
    elif dt_ex_rt==2:
        show_ex()
    else:
        print("Wrong input.")
else:
    print("Please try again enter 1 or 2 only : ")

