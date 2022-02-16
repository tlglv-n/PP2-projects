movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]


def single_movie(s, movies):
    for i in range(len(movies)):
        if movies[i]["name"] == s and float(movies[i]["imdb"]) > 5.5:
            return True
    return False

def sublist(s, movies):
    list_movies = []
    for i in range(len(movies)):
        if float(movies[i]["imdb"]) > 5.5:
            list_movies.append(movies[i]["name"])
    return list_movies

def category(s2, movies):
    list_categories = []
    for i in range(len(movies)):
        if movies[i]["category"] == s2:
            list_categories.append(movies[i]["name"])
    return list_categories

def average(s3, movies):
    aver_num = 0
    denominator_num = 1
    for i in range(len(movies)):
        if movies[i]["name"] in s3:
            aver_num += movies[i]["imdb"]
            denominator_num += 1
    return aver_num / (denominator_num - 1)

def categories_average(s4, movies):
    aver_num = 0
    denominator_num = 1
    for i in range(len(movies)):
        if movies[i]["category"] == s4:
            aver_num += movies[i]["imdb"]
            denominator_num += 1
    return aver_num / (denominator_num - 1)


s = input()
s2 = input()
s3 = input()
s4 = input()
print(single_movie(s, movies))
print(*sublist(s, movies), sep=", ")
print(*category(s2, movies), sep=", ")
print(average(s3, movies))
print(categories_average(s4, movies))
