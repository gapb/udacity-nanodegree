# coding: utf-8
"""This module contains the code to load the movie data for the entertainment
center (stored as string literals), and call fresh_tomatoes.open_movies() to
convert the data into a web page. Future versions of this program may store the
movie information in an external file, which this program would parse before
feeding to fresh_tomatoes.py

"""

import media, fresh_tomatoes

__author__ = 'gilbertpodell-blume'


def main():

    # Step 1: declare the required Movie objects
    fury_road = media.Movie("Mad Max: Fury Road", "[find or write a good"
                                                  "synopsis]",
                            "https://upload.wikimedia.org/wikipedia/en/2/23/"
                            "Max_Mad_Fury_Road_Newest_Poster.jpg",
                            "https://www.youtube.com/watch?v=cdLl1GVjOrc")

    the_lives_of_others = media.Movie("The Lives of Others",
                                      "[find or write a good synopsis]",
                                      "https://upload.wikimedia.org/wikipedia/"
                                      "en/9/9f/Leben_der_anderen.jpg",
                                      "https://www.youtube.com/watch?v=n3_iLOp6"
                                      "IhM")

    yojimbo = media.Movie("Yojimbo", "[find or write a good synopsis]",
                          "https://upload.wikimedia.org/wikipedia/en/8/8b/"
                          "Yojimbo_%28movie_poster%29.jpg",
                          "https://www.youtube.com/watch?v=y_1iT_GmHTE")

    castle_in_the_sky = media.Movie("Castle in the Sky",
                                    "[find or write a good synopsis]",
                                    "https://upload.wikimedia.org/wikipedia/en/"
                                    "4/40/Castle_in_the_Sky_%28Movie_Poster%29."
                                    "jpg",
                                    "https://www.youtube.com/watch?v=8ykEy-yPBF"
                                    "c")

    micmacs = media.Movie("Micmacs", "[find or write a good synopsis]",
                          "https://upload.wikimedia.org/wikipedia/en/7/75/"
                          "Micmacs_à_tire-larigot.jpg",
                          "https://www.youtube.com/watch?v=TjKW0tG7I8s")

    labyrinth = media.Movie("Labyrinth", "[find or write a good synopsis]",
                            "https://upload.wikimedia.org/wikipedia/en/6/6b/"
                            "Labyrinth_ver2.jpg",
                            "https://www.youtube.com/watch?v=XRcOZZDvMv4")

    # Step 2: compile the Movie objects into a list of movies
    movies = {fury_road, the_lives_of_others, yojimbo, castle_in_the_sky,
              micmacs, labyrinth}

    # Step 3: pass the list of movies to fresh_tomatoes.open_movies_page(movies)
    fresh_tomatoes.open_movies_page(movies)

if __name__ == "__main__":
    main()
