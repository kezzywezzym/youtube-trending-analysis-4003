import matplotlib.pyplot as plt


def category_pie_chart(videos):

    category_names = {
        "1": "Film & Animation",
        "2": "Autos & Vehicles",
        "10": "Music",
        "15": "Pets & Animals",
        "17": "Sports",
        "19": "Travel & Events",
        "20": "Gaming",
        "22": "People & Blogs",
        "23": "Comedy",
        "24": "Entertainment",
        "25": "News & Politics",
        "26": "How-to & Style",
        "27": "Education",
        "28": "Science & Technology",
        "29": "Nonprofits & Activism",
        "43": "Shows"
    }

    categories = {}

    for video in videos:
        category = category_names.get(video.category, video.category)

        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1

    plt.figure(figsize=(8, 8))

    plt.pie(
        categories.values(),
        autopct="%1.1f%%",
        startangle=90
    )

    plt.legend(
        categories.keys(),
        title="Categories",
        loc="center left",
        bbox_to_anchor=(1, 0.5)
    )

    plt.title("Distribution of YouTube Videos by Category")
    plt.show()


def views_histogram(videos):

    views = []

    for video in videos:
        views.append(video.views)

    plt.figure(figsize=(8, 5))

    plt.hist(views, bins=15)

    plt.title("Distribution of Video Views")
    plt.xlabel("Views")
    plt.ylabel("Number of Videos")

    plt.show()


def likes_histogram(videos):

    likes = []

    for video in videos:
        likes.append(video.likes)

    plt.figure(figsize=(8, 5))

    plt.hist(likes, bins=15)

    plt.title("Distribution of Video Likes")
    plt.xlabel("Likes")
    plt.ylabel("Number of Videos")

    plt.show()


def comments_histogram(videos):

    comments = []

    for video in videos:
        comments.append(video.comments)

    plt.figure(figsize=(8, 5))

    plt.hist(comments, bins=15)

    plt.title("Distribution of Video Comments")
    plt.xlabel("Comments")
    plt.ylabel("Number of Videos")

    plt.show()

