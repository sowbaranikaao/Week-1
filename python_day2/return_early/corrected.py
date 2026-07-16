def login(user):
    if not user:
        print("Empty")
        return
    if user!="admin":
            print("Guest")
            return
    if len(user)<=3:
            print("Invalid")
            return
    print("Welcome")
login("admin")