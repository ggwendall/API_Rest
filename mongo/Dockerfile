# official MongoDB 5.0 image as the base image
FROM mongo:5.0

# Define build-time variables
ARG DATABASE_URI
ARG USERNAME
ARG PASSWORD

# Set environment variables
ENV DATABASE_URI ${DATABASE_URI}
ENV USERNAME ${USERNAME}
ENV PASSWORD ${PASSWORD}

# Copy the .json file from the local file system to the Docker image
COPY CO2_emission_by_countries.json /CO2_emission_by_countries.json

# Run the mongoimport command
CMD mongoimport --jsonArray --db=environment --collection=worldcarbon --file=CO2_emission_by_countries.json -u root -p pass12345 --host=mongo --port=27017 --authenticationDatabase admin