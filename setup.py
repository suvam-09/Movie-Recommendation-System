from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# edit below variables as per the requirements -
REPO_NAME = "Movie-Recommendation-System"
AUTHOR_USER_NAME = "suvam-09"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="Movie Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="suvam.kumar@yahoo.com",
    packages=[SRC_REPO],
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
