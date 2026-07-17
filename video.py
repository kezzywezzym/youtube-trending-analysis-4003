class Video:
    def __init__(self, row):
        self.video_id = row["video_id"]
        self.title = row["title"]
        self.channel = row["channel_title"]
        self.category = row["category_id"]
        self.tags = row["tags"]
        self.views = int(row["views"])
        self.likes = int(row["likes"])
        self.dislikes = int(row["dislikes"])
        self.comments = int(row["comment_count"])
        self.publish_time = row["publish_time"]
        self.trending_date = row["trending_date"]

    def summary(self):
        return (
            f"{self.title} by {self.channel}\n"
            f"Views: {self.views:,} | Likes: {self.likes:,} | "
            f"Comments: {self.comments:,}"
        )