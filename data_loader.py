import csv

def load_data():
    data = []

    with open("data/youtube_trending_videos.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            data.append(row)

    print("Data loaded successfully.")
    print(f"{len(data)} records loaded.")

    return data