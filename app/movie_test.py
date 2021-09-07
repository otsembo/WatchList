import unittest
from models import movie

#Movie object
Movie = movie.Movie

class MovieTest(unittest.TestCase):
    '''
    Test class to check behavior of class
    '''

    def setUp(self):
        '''
        Run before every test
        '''
        self.new_movie = Movie(5243, 'Face Off', 'Thrilling action movie', 'https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5, 129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie, Movie))


if __name__ == '__main__':
    unittest.main()