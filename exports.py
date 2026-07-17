import json
import os


def export_video(videos):
    search = input("Enter a video title: ").lower()

    for video in videos:
        if search in video.title.lower():

            data = {
                "video_id": video.video_id,
                "title": video.title,
                "channel": video.channel,
                "category": video.category,
                "views": video.views,
                "likes": video.likes,
                "dislikes": video.dislikes,
                "comments": video.comments
            }

            file_path = os.path.join("exports", "selected_video.json")

            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

            print("Video exported successfully.")
            return

    print("Video not found.")