# Build the Docker image with tag 'pocket_repo'
docker build -t pocket_repo .

# Run the container, removing it after exit
docker run --rm pocket_repo
