class User:
    def __init__(self, userName, password, fullName):
        self.userName = userName
        self.password = password
        self.fullName = fullName
        self.followers = []
        self.following = []
        self.followRequestsSent = []
        self.followRequestsReceived = []
        self.posts = []

    def handleSendFollowRequests(self):
        otherUserName = input("Enter user-name to send follow request: ")
        if otherUserName not in dataStore:
            print("User doesn't exist")
            return 

        if otherUserName in self.following:
            print("Already you are following this user")
            return

        if otherUserName in self.followRequestsSent:
            print("Follow request already sent")
            return

        self.followRequestsSent.append(otherUserName)
        otherUserObj = dataStore[otherUserName]
        otherUserObj.followRequestsReceived.append(self.userName)
        print("Follow request sent successfully")

    def handleAcceptFollowRequests(self):
        if not self.followRequestsReceived:
            print("No follow requests received")
            return

        for userName in self.followRequestsReceived:
            print(f"Do you want to accept request from: {userName}? (y/n)")
            option = input().strip().lower()

            if option == 'y':
                self.followers.append(userName)
                dataStore[userName].following.append(self.userName)  # Add to the other user's following list
                print("Accepted the request successfully")
            else:
                print("Deleted the follow request successfully")

        self.followRequestsReceived = []  # Clear follow requests

    def printAllFollowersList(self):
        if not self.followers:
            print("No followers")
        else:
            print("Your followers:")
            for userName in self.followers:
                print(userName)

    def printAllFollowingList(self):
        if not self.following:
            print("You are not following anyone")
        else:
            print("You are following:")
            for userName in self.following:
                print(userName)

dataStore = {}

def displayAndHandleMainMenu(userName):
    userObj = dataStore[userName]

    while True:
        print("\n-----------------------------------------------------")
        print("1 - Send Follow Request")
        print("2 - Accept Follow Request")
        print("3 - Print Followers")
        print("4 - Print Following List")
        print("5 - Logout")
        option = input("Choose an option: ").strip()
        print("-----------------------------------------------------")

        if option == "1":
            userObj.handleSendFollowRequests()
        elif option == "2":
            userObj.handleAcceptFollowRequests()
        elif option == "3":
            userObj.printAllFollowersList()
        elif option == "4":
            userObj.printAllFollowingList()
        elif option == "5":
            print("Logged out successfully\n")
            break
        else:
            print("Invalid option! Please choose a valid option.")

def handleLogin():
    print("\nEnter your login details")
    userName = input("Enter your user-name: ").strip()
    password = input("Enter your password: ").strip()

    if userName not in dataStore:
        print("User not found! Please sign up first.")
        return
    
    userObj = dataStore[userName]
    if password != userObj.password:
        print("Incorrect password! Try again.")
        return
    
    print("Logged in successfully!")
    displayAndHandleMainMenu(userName)

def handleSignup():
    print("\nEnter your details to create an account")
    fullName = input("Enter your full name: ").strip()
    userName = input("Enter your user-name: ").strip()
    password = input("Enter your password: ").strip()

    if userName in dataStore:
        print("User-name already exists! Try a different one.")
        return
    
    newUser = User(userName, password, fullName)
    dataStore[userName] = newUser
    print("Account created successfully!")

while True:
    print("\n-----------------------------------------------------")
    print("1 - Login")
    print("2 - Signup")
    print("3 - Exit")
    option = input("Choose an option: ").strip()
    print("-----------------------------------------------------")

    if option == "1": 
        handleLogin()
    elif option == "2":
        handleSignup()
    elif option == "3":
        print("Thanks for using Instagram!")
        break
    else:
        print("Invalid option! Please choose a valid one.")
