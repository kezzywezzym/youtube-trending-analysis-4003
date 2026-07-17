def total_videos(videos):
    print(f"\nTotal Videos: {len(videos)}")


def total_channels(videos):
    channels = set()

    for video in videos:
        channels.add(video.channel)

    print(f"\nTotal Channels: {len(channels)}")


def category_summary(videos):
    categories = {}

    for video in videos:
        category = video.category

        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1

    print("\nVideos by Category")

    for category, total in categories.items():
        print(f"Category {category}: {total}")


def search_video(videos):
    search = input("Enter a video title: ").lower()

    for video in videos:
        if search in video.title.lower():
            print("\nTitle:", video.title)
            print("Channel:", video.channel)
            print("Views:", video.views)
            print("Likes:", video.likes)
            print("Comments:", video.comments)
            return

    print("Video not found.")

def top_ten_videos(videos):
    top_videos = sorted(
        videos,
        key=lambda video: video.views,
        reverse=True
    )

    print("\nTop 10 Videos by Views")

    for number, video in enumerate(top_videos[:10], start=1):
        print(f"{number}. {video.title}")
        print(f"   Views: {video.views:,}")