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
        labels=categories.keys(),
        autopct="%1.1f%%"
    )

    plt.title("Distribution of YouTube Videos by Category")

    plt.show()
