import streamlit as st
import pickle
import requests

# in Python the base64 module is used to encode and decode data
# at first the strings are converted into byte-like objects and then encoded using the base64 module
import base64

# unpickle the 'movie_list.pkl' file to and pass on the values for movie titles
movie_list = pickle.load(open('./movie_list.pkl', 'rb'))
movies_list = movie_list['title'].values
similarity = pickle.load(open('./similarity_check.pkl', 'rb'))


st.title('Movie Recommender System')

# ----------------------------------------------------------------------------------------------------------------------------
# setting up the cover page for our application


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
    # we use the base64.b64encode() function to encode these base64 bytes
    # now to get a string out of these bytes we use Python's decode() method


def add_bag_from_url(png_file):
    bin_str = get_base64(png_file)
    bg_img = '''
    <style>.stApp{
    background-image: url("data:image/png;base64,%s");
    background-attachment: fixed;
    background-size: cover
    }
    </style>
    ''' % bin_str
    st.markdown(bg_img, unsafe_allow_html=True)
    # background-size: cover --> meaning the background image will cover the entire element
    # background-attachment: fixed --> meaning entire element is always covered with no stretching (the image will retain its original proportion)
    # unsafe_allow_html=False --> to ensure the HTML tags in the body are neither escaped not treated as mere text


add_bag_from_url('./cover_image/image_1.jpg')

# ----------------------------------------------------------------------------------------------------------------------------
# defining helper function to fetch posters for the recommended movies


def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(
        movie_id)
    data = requests.get(url, verify=False)
    # adding parameter [verify= False] to avoid error related to verification of SSL certificates: SSLError HTTPSConnectionPool
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# ----------------------------------------------------------------------------------------------------------------------------
# now we need to define a helper function that would request a movie from the user
# and would fetch for top 5 similar movies and share them back to the user as recommendation

# Steps to be followed under the helper function:
# based on users request a movie is provided as an input to the function
# now we need to fetch the index value for this movie and store it under a variable
# based on the index value we then need to check for the similarity scores for this movie against other movies
# once the similarity array for that particular movie has been identified -- it then needs to sort the distances in decreasing order


def recommend(movie):
    movie_index = movie_list[movie_list['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_rec = sorted(list(enumerate(distance)),
                        reverse=True, key=lambda x: x[1])[1:7]

    movie_names = []
    movie_posters = []
    for i in movies_rec:
        movie_id = movie_list.iloc[i[0]].movie_id
        movie_names.append(movie_list.iloc[i[0]].title)
        # fetch movie poster using API
        movie_posters.append(fetch_poster(movie_id))

    return movie_names, movie_posters


# ----------------------------------------------------------------------------------------------------------------------------
# selectbox to access the inout provided by the user
user_input = st.selectbox(
    'Type or select a movie from the dropdown:', movies_list)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(user_input)

    col1, col2, col3 = st.columns([5, 5, 5], gap='large')
    with col1:
        st.image(recommended_movie_posters[0], width=200)
        st.caption(recommended_movie_names[0])
    with col2:
        st.image(recommended_movie_posters[1], width=200)
        st.caption(recommended_movie_names[1])
    with col3:
        st.image(recommended_movie_posters[2], width=200)
        st.caption(recommended_movie_names[2])

    col4, col5, col6 = st.columns([5, 5, 5], gap='large')
    with col4:
        st.image(recommended_movie_posters[3], width=200)
        st.caption(recommended_movie_names[3])
    with col5:
        st.image(recommended_movie_posters[4], width=200)
        st.caption(recommended_movie_names[4])
    with col6:
        st.image(recommended_movie_posters[5], width=200)
        st.caption(recommended_movie_names[5])
