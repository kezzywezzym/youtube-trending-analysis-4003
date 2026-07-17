from processor import total_videos
from data_loader import load_data



def display_menu():

    print("\n--------------------------------")

    print("YouTube Trending Videos")

    print("--------------------------------")

    print("1. Load Data")

    print("2. Process Data")

    print("3. Visualise Data")

    print("4. Export Data")

    print("5. Exit")




videos = []


while True:

    display_menu()

    choice = input("Enter your choice: ")


    if choice == "1":

        videos = load_data()

    elif choice == "2":

        print("\nProcessing Menu")
        print("1. Total Videos")
        print("2. Back")

        process_choice = input("Choose an option: ")

        if process_choice == "1":
            total_videos(videos)

    elif choice == "5":

        print("Goodbye!")

        print("Thank you for using the program.")

        break

    else:

        print("This option is not ready yet.")