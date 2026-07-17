from charts import category_pie_chart, views_histogram
from data_loader import load_data
from processor import (
    total_videos,
    total_channels,
    category_summary,
    search_video,
    top_ten_videos
)

videos = []

while True:
    print("\n--------------------------------")
    print("YouTube Trending Videos")
    print("--------------------------------")
    print("1. Load Data")
    print("2. Process Data")
    print("3. Visualise Data")
    print("4. Export Data")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        videos = load_data()

    elif choice == "2":
        if not videos:
            print("Please load the data first.")
            continue

        print("\nProcessing Menu")
        print("1. Total Videos")
        print("2. Total Channels")
        print("3. Category Summary")
        print("4. Search Video")
        print("5. Top 10 Videos")

        process = input("Choose an option: ")

        if process == "1":
            total_videos(videos)

        elif process == "2":
            total_channels(videos)

        elif process == "3":
            category_summary(videos)

        elif process == "4":
            search_video(videos)

        elif process == "5":
            top_ten_videos(videos)

        else:
            print("Invalid processing option.")


    elif choice == "3":

        if not videos:
            print("Please load the data first.")

            continue

        print("\nVisualisation Menu")

        print("1. Pie Chart")

        print("2. Views Histogram")

        visual = input("Choose an option: ")

        if visual == "1":

            category_pie_chart(videos)


        elif visual == "2":

            views_histogram(videos)


        else:

            print("Invalid option.")

    elif choice == "5":
        print("Goodbye!")
        print("Thank you for using the program.")
        break

    else:
        print("This option is not ready yet.")

