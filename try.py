import random

class MovieRecommendationSystem:
    def __init__(self):
        self.movies = []

    def add_movie(self, title, genre, industry, language):
        rating = round(random.uniform(0, 10), 1)  # Assign a random rating between 0 and 10
        movie = {
            'title': title,
            'genre': genre,
            'industry': industry,
            'language': language,
            'rating': rating
        }
        self.movies.append(movie)
        print(f"Movie '{title}' added with rating {rating}.")

    def search_movie_by_title(self, title):
        results = [movie for movie in self.movies if movie['title'].lower() == title.lower()]
        return results

    def search_movie_by_genre(self, genre):
        results = [movie for movie in self.movies if movie['genre'].lower() == genre.lower()]
        return results

    def search_movie_by_industry(self, industry):
        results = [movie for movie in self.movies if movie['industry'].lower() == industry.lower()]
        return results

    def delete_movie(self, title):
        self.movies = [movie for movie in self.movies if movie['title'].lower() != title.lower()]
        print(f"Movie '{title}' deleted if it existed.")

    def display_movies(self, count=10):
        return self.movies[:count]

    def display_movies_by_rating(self):
        sorted_movies = sorted(self.movies, key=lambda x: x['rating'], reverse=True)
        return sorted_movies

# Command-line interface
def main():
    movie_system = MovieRecommendationSystem()
    
    while True:
        print("\nOptions:")
        print("1. Add Movie")
        print("2. Search Movie by Title")
        print("3. Search Movie by Genre")
        print("4. Search Movie by Industry")
        print("5. Delete Movie")
        print("6. Display up to 10 Movies")
        print("7. Display Movies by Rating")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter movie title: ")
            genre = input("Enter movie genre: ")
            industry = input("Enter movie industry: ")
            language = input("Enter movie language: ")
            movie_system.add_movie(title, genre, industry, language)
        elif choice == '2':
            title = input("Enter movie title to search: ")
            results = movie_system.search_movie_by_title(title)
            if results:
                for movie in results:
                    print(movie)
            else:
                print("No movie found with that title.")
        elif choice == '3':
            genre = input("Enter movie genre to search: ")
            results = movie_system.search_movie_by_genre(genre)
            if results:
                for movie in results:
                    print(movie)
            else:
                print("No movie found with that genre.")
        elif choice == '4':
            industry = input("Enter movie industry to search: ")
            results = movie_system.search_movie_by_industry(industry)
            if results:
                for movie in results:
                    print(movie)
            else:
                print("No movie found in that industry.")
        elif choice == '5':
            title = input("Enter movie title to delete: ")
            movie_system.delete_movie(title)
        elif choice == '6':
            movies = movie_system.display_movies()
            for movie in movies:
                print(movie)
        elif choice == '7':
            sorted_movies = movie_system.display_movies_by_rating()
            for movie in sorted_movies:
                print(movie)
        elif choice == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

