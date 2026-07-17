def total_videos(videos):
    print(f"\nTotal Videos: {len(videos)}")


def total_channels(videos):
    channels = set()

    for video in videos:
        channels.add(video.channel)

    print(f"\nTotal Channels: {len(channels)}")