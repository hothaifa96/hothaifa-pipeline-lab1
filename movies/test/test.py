import requests

MOVIE_NAME = "The Matrix"
movie_data = {
    "name": MOVIE_NAME,
    "length": 136,
    "genre": "sci-fi"
}

# POST: Add the movie
print("Adding a new movie...")
res_post = requests.post("http://localhost/movie", json=movie_data)
if res_post.status_code != 200:
    raise Exception(f"Failed to add movie: {res_post.text}")

# GET: Retrieve all movies
print("Fetching all movies...")
res_get = requests.get("http://localhost/movie")
if res_get.status_code != 200:
    raise Exception(f"Failed to get movies: {res_get.text}")

movies = res_get.json()

# Check if the new movie is in the list
if any(movie.get("name") == MOVIE_NAME for movie in movies):
    print(f"✅ Movie '{MOVIE_NAME}' was successfully added.")
else:
    raise Exception(f"❌ Movie '{MOVIE_NAME}' not found in the movie list. Test failed!")
