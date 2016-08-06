import fresh_tomatoes
import media

X_Men = media.Movie("X-men","Story of mutants","http://cdn1-www.comingsoon.net/assets/uploads/2016/05/xmenapocalypseimax-1.jpg","https://www.youtube.com/watch?v=PfBVIHgQbYk")

Hunger_games = media.Movie("Hunger games","story of fighter","http://cdn.collider.com/wp-content/uploads/the-hunger-games-catching-fire-poster-final.jpg","https://www.youtube.com/watch?v=EAzGXqJSDJ8")

Avatar = media.Movie("Avatar","A marine on a alien planet","http://imgs.abduzeedo.com/files/articles/Avatar/4154691413_a695e033a8_o.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")

Iron_man = media.Movie("Iron Man","Story of a Superhero","http://cdn.collider.com/wp-content/uploads/iron-man-poster.jpg","https://www.youtube.com/watch?v=8hYlB38asDY")

Avengers = media.Movie("Avengers","Story of Superheroes saving their Country","https://s-media-cache-ak0.pinimg.com/236x/2d/17/7f/2d177f86134cce044cfea0e150dbdf44.jpg","https://www.youtube.com/watch?v=eOrNdBpGMv8")


movies=[X_Men,Hunger_games,Avatar,Iron_man,Avengers]
fresh_tomatoes.open_movies_page(movies)
