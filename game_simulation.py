import time 

def display_intro():
    print("Welcome to the text adventure game!")
    print("You can yourself in a mysterious land full of challenges and decisions.")
    
def get_player_choice():
    print("\nChoose your action:")
    print("1. Go left")
    print("2. Go right")
    print("3. Stay put")
    return input("Enter the number of your choice: ")

def provide_feedback(choice):
    if choice == "1":
        print("\nYou choose to go left. You encounter a friend creature.")
    elif choice == "2":
        print("\nYou choose to go right. You discover a hidden treasure.")
    elif choice == "3":
        print("\nYou choose to stay put. Nothing eventful happens. ")
        
def update_progress():
    print("\nUpdating your progress...")
    time.sleep(1)
    print("You have made some progress in the game.")
    
def display_conclusion():
    print("\nCongratulations! You've reached the end of the adventure.")
    print("Here are the outcomes based on your choices: ")
    

def main():
    display_intro()
    
    for _ in range(3):
        choice = get_player_choice()
        provide_feedback(choice)
        update_progress()
        
    display_conclusion()
    
    
if __name__ == "__main__":
    main()