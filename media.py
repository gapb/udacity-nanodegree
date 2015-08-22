"""This module contains classes (well, one class) for managing information about
movies for the benefit of the Movie Trailer Website.
It was modeled almost verbatim after the Movie class detailed in Lesson 03a of
Udacity's Programming Foundations with Python course.

"""

__author__ = 'gilbertpodell-blume'


class Movie:
    """A class containing information about a Movie.

    Attributes:
        title: a string indicating the movie's title
        storyline: a string containing a summary of the movie's plot.
        poster_image_url: a string containing the URL of an image of a movie
        poster
        trailer_youtube_url: a string containing the URL of a trailer for the
        movie on Youtube

    """

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def __str__(self):
        return "Title: " + self.title + "\nStoryline: " + self.storyline\
               + "\nPoster URL: " + self.poster_image_url + "\nTrailer URL: "\
               + self.trailer_youtube_url

    # There would be a show_trailer() method here if this were the
    # implementation from the Programming Foundations with Python course, but as
    # it would be redundant I've chosen to omit it for the time being.

