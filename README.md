# Overview:
This is a streamlit web application that can recommend various kinds of similar movies based on an users' interest. Users will be requested to type/select a movie based on their interest and the recommender system would help suggest back a list of movies similar to the one selected by the user. Here in this project, we will be implementing a content-based recommendation system and would be sharing atmost 6 recommended movies based on users' choice.

We are using the dataset from TMDB (https://www.themoviedb.org/about). The Movie Database (TMDB) is a community built movie and TV database. The platform consists of around 5000 movies and associated details. The dataset is available on Kaggle - https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata.

## Sample Screenshot:
<img src = ".\cover_image\screenshot.jpg">

## Concept used to build the similarity_check.pkl file: cosine_similarity
- Cosine Similarity is a metric that allows us to measure the similarity between two/multiple entities
- In order to demonstrate cosine similarity function we need vectors arranged as a numpy array
- Once we have vectors, we can call *cosine_similarity()* function by passing both vectors
- This will calculate the cosine similarity between these two vectors
- The value/similarity score ranges between [0,1] -- *if it is 0 then both vectors are completely different (i.e. no similarity) while if the value is 1, the vectors are strongly correlated with each other (i.e. completely similar)*

## Sample understanding of how the model should work:
- Based on user's request a movie is provided as an input to the function
- Now we need to fetch the index value for this movie and store it under a variable
- Based on the index value, we then need to check for the similarity scores for this movie against other movies
- Once the similarity array for that particular movie has been identified, we need to sort the distances in decreasing order
- Meanwhile while sorting the distances we also need to hold the index position for our requested movie so that the sorted values don't mismatch
> *for example:*
- for 'Avatar' --> cosine distance = 1 against itself
- for 'Avatar' --> cosine distance = 0.08226127 against movie_2
- for 'Avatar' --> cosine distance = 0.0860309 against movie_3
- so while sorting results will follow up as: [1, 0.0860309, 0.08226127]
- however, we have our movies in the sequence: [movie_1, movie_2, movie_3]
- but the correct sequence should be: [movie_1, movie_3, movie_2] (based on distance)

So we need to ensure that the index position is not lost while sorting the distance values and for this we would be using the *enumerate()* functionality and transform it into a list.

## Deploying application on Heroku:
With regards to the final step of deploying our application over the Heroku server, we need 4 files as stated below:
- *procfile* - this file houses the command required for running our streamlit application over Heroku's server
- *setup.sh* - this is a batch file consisting of OS related commands specific to the directory
- *.gitignore* - this file consists of the names of files and folders that we want to ignore from uploading over the server
- *requirements.txt* -  this file consists of a list of libraries that are required for the project to run on the server
