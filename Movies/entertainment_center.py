
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",)
avatar = media.Movie("Avatar",
                        "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                        "http://www.foxmovies.com/movies/avatar/download-poster/251",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY",)
matrix = media.Movie("The Matrix",
                        "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                        "http://www.impawards.com/1999/posters/matrix_ver1.jpg",
                        "https://www.youtube.com/watch?v=vKQi3bBA1y8",)

print(toy_story.storyline)
print(avatar.storyline)
matrix.show_trailer()
#avatar.show_trailer()



