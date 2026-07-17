import csv
import os

from video import Video

def load_data():
    videos = []

    csv_path = os.path.join(
        os.path.dirname(__file__),
        "data",
        "youtube_trending_videos.csv"
    )

    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            videos.append(Video(row))

    print("Data loaded successfully.")
    print(f"{len(videos)} records loaded.")

    return videos