def login(user):

    if user:

        if user=="admin":

            if len(user)>3:

                print("Welcome")

            else:

                print("Invalid")

        else:

            print("Guest")

    else:

        print("Empty")