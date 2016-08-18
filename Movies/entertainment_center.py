
import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",)
avatar = media.Movie("Avatar",
                        "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn "
                        "between following his orders and protecting the world he feels is his home.",
                        "http://www.foxmovies.com/movies/avatar/download-poster/251",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY",)
matrix = media.Movie("The Matrix",
                        "A computer hacker learns from mysterious rebels about the true nature of his "
                        "reality and his role in the war against its controllers.",
                        "http://www.impawards.com/1999/posters/matrix_ver1.jpg",
                        "https://www.youtube.com/watch?v=vKQi3bBA1y8",)

lotr = media.Movie("Lord of the Rings",
                  "The future of civilization rests in the fate of the One Ring",
                  "https://www.movieposter.com/posters/archive/main/7/MPW-3576",
                  "https://www.youtube.com/watch?v=Pki6jbSbXIY")

about_time = media.Movie("About Time",
                         "At the age of 21, Tim discovers he can travel in time and change what happens and "
                         "has happened in his own life. His decision to make his world a better place by getting a girlfriend "
                         "turns out not to be as easy as you might think.",
                         "http://www.impawards.com/intl/uk/2013/posters/about_time.jpg",
                         "https://www.youtube.com/watch?v=T7A810duHvw")

stargate = media.Movie("Stargate",
                       "An interstellar teleportation device, found in Egypt, leads to a planet with humans resembling "
                       "ancient Egyptians who worship the god Ra.",
                       "http://media.theiapolis.com/d4/h1AK/i1O4J/k4/l1OIT/wW8/stargate-film-poster.jpg",
                       "https://www.youtube.com/watch?v=_mucMCddPy0")

#print(toy_story.storyline)
#print(toy_story.title)
#print(avatar.storyline)
#matrix.show_trailer()
#avatar.show_trailer()

#print(media.Movie.valid_ratings)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)

movies = [toy_story, avatar, matrix, lotr, about_time, stargate]
fresh_tomatoes.open_movies_page(movies)



