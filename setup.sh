# creating a directory on the server
mkdir -p ~/.streamlit/

# establishing connection with the server
echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml # creating a configuration file
