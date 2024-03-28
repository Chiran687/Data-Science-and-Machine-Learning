import sqlite3, inquirer, base64, colorama
import regex as re


database = sqlite3.connect("DB_Main.db")
cursor = database.cursor()
colorama.init()

print("██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗")
print("██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝")
print("██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  ")
print("██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  ")
print("╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗")
print(" ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝", "\n")
                                                                                                                       

class UserManagement:
    def __init__(self):
        pass
    
    #Function to create user
    def register_user():
        username = input("Please enter username: ")
        while True:
            #Check if Username exixts
            cursor.execute("SELECT username FROM users WHERE username=?", (username,))
            existing_username = cursor.fetchone()
            
            if existing_username: 
                print("Username already Exists.")
                username = input("Please enter username: ")
            else:
                password = str(input("Please provide password: "))
                #Using regex to validate password strength
                if re.match(
                    r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$",
                    password,
                ):  
                    #Encrypting Password Using Base64
                    encrpted_password = base64.b64encode(password.encode())
                    UserManagement.insert(username.strip(), encrpted_password)
                    break
                
                else:
                    print(
                        "Password requirement not met.\n Special Character.\n Numbers.\n Lower case and upper case. "
                    )
                    password = str(input("Please provide password: "))
                    
    #Function to insert Username in Database.        
    def insert(username, encrypted_password):
        try:
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)"
            )
            database.commit()
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, encrypted_password),
            )
            database.commit()
            print(f"{username} added successfully.")
        except sqlite3.Error as e:
            print(e)
            
    #Function to login user
    def login_user():
        while True:
            username = str(input("Please enter your username:- "))
            password = str(input("Please enter your password:- "))
            encrypted_password = base64.b64encode(password.encode())
            cursor.execute(
                "SELECT * FROM users WHERE username=? AND password=?",
                (username, encrypted_password),
            )
            user = cursor.fetchone()
            
            if user:
                print(f"Login successful for {username}.")
                UserManagement.home()
                break
            else:
                print("Login failed. Incorrect username or password.")
                
    #Home function for logged in user.
    def home():
        while True:
            questions = [
                inquirer.List(
                    "size",
                    message="Please Select the operation?",
                    choices=[
                        "List all Users.",
                        "Add new user",
                        "Delete a User",
                        "Update Password",
                        "Exit.",
                    ],
                ),
            ]
            
            answers = inquirer.prompt(questions)
            if answers["size"] == "List all Users.":
                cursor.execute(
                "SELECT * FROM users")
                data = cursor.fetchall()
                print(data)
                
            elif answers["size"] == "Add new user":
                UserManagement.register_user()
                
            elif answers["size"] == "Delete a User":
                try:
                    uname = str(input(f"Please type the username to delete, {colorama.Fore.YELLOW  + "username is case sensitive" + colorama.Fore.RESET}" ))
                    cursor.execute(
                    f"DELETE  FROM users WHERE username={uname}"
                    )
                    database.commit()
                    print(f"{uname} Deleted")
                except sqlite3.Error as e:
                    print(e)
            elif answers["size"] == "Update Password":
                UserManagement.update()      
            elif answers["size"] == "Exit.":
                cursor.close()
                print("Bye.......")
                exit()
    #update password            
    def update():
        while True:
            username = str(input("Please provide username whose password to change:- "))
            updated_password = str(input("Please provide new password:- "))
        
            if re.match(
                        r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$",
                        updated_password,
                    ):  
                        #Encrypting Password Using Base64
                        encrypted_password = base64.b64encode(updated_password.encode())
                        cursor.execute("UPDATE users SET password=? WHERE username=?", (encrypted_password, username))
                        database.commit()
                        print(f"Password reset successful for {username}.")
                        break
                    
            else:
                print(
                    "Password requirement not met.\n Special Character.\n Numbers.\n Lower case and upper case. "
                )
                
            updated_password = str(input("Please provide new password:- "))
            encrypted_password = base64.b64encode(updated_password.encode())
        
#Main startup Function
def main():
    while True:
        questions = [
        inquirer.List('size',
                        message="Do you want to Login or Register",
                        choices=['Login', 'Register']
                    ),
                    ]
        answers = inquirer.prompt(questions)
        if answers["size"] == "Login":
            UserManagement.login_user()
        else:
            UserManagement.register_user()

if __name__ == "__main__":
    main()
