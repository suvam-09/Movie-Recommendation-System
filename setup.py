from distutils.core import setup
import os
from setuptools import find_packages

# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(
    # Name of the package
    name='Movie-Recommendation-System',
    # Packages to include into the distribution
    packages=find_packages('.'),
    # Start with a small number and increase it with
    # every change you make https://semver.org
    version='1.0.0',
    # Chose a license from here: https: //
    # help.github.com / articles / licensing - a -
    # repository. For example: MIT
    license='',
    # Short description of your library
    description='TMDB Movie Recommendation SYstem using Machine Learning',
    # Long description of your library
    long_description=long_description,
    long_description_content_type='Designing a streamlit web application that can recommend various kinds of similar movies based on users\' interest. Recommendation systems work in a way wherein the users are requested to type/select a movie based on their interest and the recommender system would help suggest back a list of movies similar to the one selected by the user.',
    # Your name
    author='Suvam Kumar',
    # Your email
    author_email='suvam.kumar@yahoo.com',
    # Either the link to your github or to your website
    url='https://blink-movie-recommender.herokuapp.com/',
    # Link from which the project can be downloaded
        download_url='https://github.com/suvam-09/Movie-Recommendation-System',
        # List of keywords
        keywords=[],
        # List of packages to install with this one
        install_requires=['streamlit', 'requests', 'pickleshare'],
        # https://pypi.org/classifiers/
        classifiers=[]
)
