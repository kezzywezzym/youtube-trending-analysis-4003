from data_loader import load_data


def display_menu():
    print("--------------------------------------------------")
    print("YouTube Trending Videos")
    print("--------------------------------------------------")
    print()
    print("1. Load Data")
    print("2. Process Data")
    print("3. Visualise Data")
    print("4. Export Data")
    print("5. Exit")


display_menu()

def main():

    videos = None

    display_menu()


    choice = input("Enter your choice: ")

    if choice == "1":

        videos = load_data()


    elif choice == "5":

        print("Goodbye.")


    else:

        print("This option is not ready yet.")

main()