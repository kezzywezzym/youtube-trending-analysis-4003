import csv

def load_data():
    data = []

    import os

    csv_path = os.path.join(os.path.dirname(__file__), "data", "youtube_trending_videos.csv")

    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            data.append(row)

    print("Data loaded successfully.")
    print(f"{len(data)} records loaded.")

    return data