import matplotlib.pyplot as plt


def category_pie_chart(videos):
    categories = {}

    for video in videos:
        categories[video.category] = categories.get(video.category, 0) + 1

    plt.figure()
    plt.pie(
        categories.values(),
        labels=categories.keys(),
        autopct="%1.1f%%"
    )

    plt.title("Videos by Category")
    plt.show()