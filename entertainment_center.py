__author__ = 'artemstafeev'
import media
import fresh_tomatoes
#initialize movie instances
toy_story=media.Movie("Toy Story","A story of a boy and his toys that has come to life","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar=media.Movie("Avatar","Avatar story","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=qlRriWu1zOI")
hunger=media.Movie("Hunger Games","The Hunger Games universe is a dystopia set in Panem, a country consisting of the wealthy Capitol and twelve districts in varying states of poverty.","https://upload.wikimedia.org/wikipedia/en/0/09/Catching_fire.JPG","https://www.youtube.com/watch?v=KmYNkasYthg")
spider=media.Movie("Spiderman","Fictional character and superhero appearing in American comic books published by Marvel Comics existing in its shared universe","https://upload.wikimedia.org/wikipedia/en/0/0c/Spiderman50.jpg","https://www.youtube.com/watch?v=O7zvehDxttM")
terminator=media.Movie("Terminator","A cyborg assassin sent back in time from the year 2029 to 1984 to kill Sarah Connor","https://upload.wikimedia.org/wikipedia/en/8/85/Terminator2poster.jpg","https://www.youtube.com/watch?v=rGSxss7gWak")
hobbit=media.Movie("Hobbit","Hobbit story","https://upload.wikimedia.org/wikipedia/en/b/b3/The_Hobbit-_An_Unexpected_Journey.jpeg","https://www.youtube.com/watch?v=iVAgTiBrrDA")
#add movies to array
movies=[toy_story,avatar,hunger,spider,terminator,hobbit]
#display movie on the webpage
fresh_tomatoes.open_movies_page(movies)