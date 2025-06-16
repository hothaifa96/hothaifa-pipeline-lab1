#!/bin/bash

set -e

MOVIE_NAME="The Matrix"

# Add a new movie
echo "Adding a new movie..."
curl -s -X POST http://localhost/movie \
  -H "Content-Type: application/json" \
  -d "{\"name\": \"${MOVIE_NAME}\", \"length\": 136, \"genre\": \"sci-fi\"}" > /dev/null

sleep 1

# Get all movies
echo "Fetching all movies..."
ALL_MOVIES=$(curl -s http://localhost/movie)

# Check if movie was added
echo "$ALL_MOVIES" | grep -q "$MOVIE_NAME"

if [ $? -eq 0 ]; then
  echo "✅ Movie '${MOVIE_NAME}' was successfully added."
else
  echo "❌ Movie '${MOVIE_NAME}' not found in the list. Test failed!"
  exit 1
fi
