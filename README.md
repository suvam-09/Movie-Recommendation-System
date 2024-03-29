# Recommendation System

Recommendation systems are becoming increasingly important in today’s extremely busy world. People are always short on time with the myriad tasks they need to accomplish in the limited time span. It is a subclass of information filtering systems that seek to predict the rating or the preference a user might give to an item. In simple words, it is an algorithm that suggests relevant items to users. Therefore, the recommendation systems are important as they help them make the right choices without having to expend their cognitive resources.

Example:
- In the case of Netflix -> which movie to watch
- In the case of e-commerce websites/apps -> which product to buy
- In the case of e-reader apps (eg: Kindle) -> which book to read, and much more

The purpose of a recommendation system is basically to search for content that would be interesting to an individual. Moreover, it involves a number of factors to create personalised lists of useful and interesting content specific to each user. Recommendation systems are AI based algorithms that skim through all possible options and create a customized list of items that are interesting and relevant to an individual. These results are based on their profile, search/browsing history, what other people with similar traits/demographics are interested in, and how likely it is for the user to seek interest in similar content. This is achieved through predictive modeling and heuristics with the data available.

##  Types of Recommendation System:

#### (i). Content Based:
Content-based systems are the ones which use characteristic information and takes item attriubutes into consideration, for example, Twitter, Youtube, etc. Basically for a content based recommender system, the customized list of recommendations is prepared using '*tags*'. Tracking which song is a user listening to, genre of songs that a user most frequently listens to, and much more. Based on these details, features are embedded into one unit and some valuable keywords are extracted to form what we call as '*tags*'. These systems make recommendations using users' item and profile features. They hypothesize that if a user was interested in an item in the past, they might seek similar interest in some related content in the future.

#### (ii). Collaborative Filtering Based:
Collaborative filtering systems are the ones which are based on user-item interactions. The alogrithm clusters the users based on their similarity scores & interests. Collaborative filtering systems are based on the assumption that if a user likes item A and another user likes the same item A as well as another item B then the first user could also be interested in the second item (i.e. *item B*). In this way the recommender system can considering recommending item B to the user A. For example, when we shop on Amazon it recommends new products saying “*Customers who bought this also bought*”. There are two types under collaborative-based recommendation systems:
- **User-Based Collaborative Filtering**: Rating of the item is done using the rating of neighbouring users. It is based on the notion of users’ similarity.
- **Item-Based Collaborative Filtering**: Rating of the item is predicted using the user’s own rating on neighbouring items. It is based on the notion of item similarity.

#### (iii) Hybrid Systems:
Hybrid systems are the ones which combine both types of information with the aim of avoiding problems that are generated when working with just one kind of these recommendation systems.

## Project Overview:
The project highlights a streamlit web application that can recommend various kinds of similar movies based on an users' interest. It is basically a content-based recommendation system using machine learning wherein the recommender model is feeding back atmost atmost 6 recommended movies based on users' chocie. Users will be requested to type/select a movie based on their interest and the recommender system would help suggest back a list of movies similar to the one selected by the user. The final deployment of the web application has been implemented on Heroku.

We have used the dataset from [TMDB](https://www.themoviedb.org/about). The Movie Database (TMDB) is a community built movie and TV database. The platform consists of around 5000 movies and associated details. The dataset is available on [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).

** **Click [here](https://suvam-09-movie-recommendation-system-app-lbu1kg.streamlit.app/) to run the application live on server**

#### -> Sample Screenshot:
<img src = ".\cover_image\screenshot.jpg">

#### -> (cosine similarity): Concept Used for Comparing Similarity Scores between Movies
- Cosine Similarity is a metric that allows us to measure the similarity between two/multiple entities
- In order to demonstrate cosine similarity function we need vectors arranged as a numpy array
- Once we have vectors, we can call *cosine_similarity()* function by passing both vectors
- This will calculate the cosine similarity between these two vectors
- The value/similarity score ranges between [0,1] -- *if it is 0 then both vectors are completely different (i.e. no similarity) while if the value is 1, the vectors are strongly correlated with each other (i.e. completely similar)*

#### -> Sample Understanding of How the Model Should Work:
- Based on user's request a movie is provided as an input to the function
- Now we need to fetch the index value for this movie and store it under a variable
- Based on the index value, we then need to check for the similarity scores for this movie against other movies
- Once the similarity array for that particular movie has been identified, we need to sort the distances in decreasing order
- Meanwhile while sorting the distances we also need to hold the index position for our requested movie so that the sorted values don't mismatch
> *for example:*
- for '*Avatar*' --> cosine distance = 1 against *itself*
- for '*Avatar*' --> cosine distance = 0.08226127 against *movie_2*
- for '*Avatar*' --> cosine distance = 0.0860309 against *movie_3*
- so while sorting results will follow up as: [1, 0.0860309, 0.08226127]
- however, we have our movies in the sequence: [*movie_1*, *movie_2*, *movie_3*]
- but the correct sequence should be: [*movie_1*, *movie_3*, *movie_2*] (based on distance)

So we need to ensure that the index position is not lost while sorting the distance values and for this we would be using the *enumerate()* functionality and transform it into a list.

#### -> Deploying the Web Application:
We need 4 files as stated below with regards to the final step of deploying our application over Heroku:
- *procfile* - this file houses the command required for running our streamlit application over Heroku's server
- *setup.sh* - this is a batch file consisting of OS related commands specific to the directory
- *.gitignore* - this file consists of the names of files and folders that we want to ignore from uploading over the server
- *requirements.txt* -  this file consists of a list of libraries that are required for the project to run on the server

## Disclaimer:
- The *similarity_check.pkl* file that houses the distance between movies (vectors) arranged in an array, has a file size greater than 100 MB. I have used the LFS Git Extension for versioning this large file. However, as Heroku doesn't support for LFS objects, the app deployment process failed multiple times during the initial stage. 
> *So in that case, consider using config vars option available under Heroku server. Heroku lets us externalise configuration i.e., storing data such as encryption keys or external resource addresses in config vars, and later at runtime, these config vars are exposed as environment variables to the application. We need to create a key-value pair under the Heroku server and have it configured as environment variable to the application using a PAT (personal access token) generated inside our GitHub account. This will enable uploading the LFS objects on the server and the deployment will be executed successfully.*

- With regards to the *requirements.txt* file, initially I had run the *pip freeze* -> *requirements.txt* code under the terminal which listed out all the libraries that would be used in running the app on the server under a file named *requirements.txt*. However, while pushing the changes to the server, there was some error wherein the libraries failed to upload on the server owing to the requirement for a different version of Python for few of these libraries, other than the one being used in this project.
> *So in that case, consider modifying 'requirements.txt' file by removing all the libraries and mentioning only those libraries that have been imported under the 'app.py' file (without mentioning the respective versions). With this, Heroku automatically decides which version is required for the installation of all the libraries over the server.*
