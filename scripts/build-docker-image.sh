#!/usr/bin/bash

# Reduces the size of the image by using the dslim/slim image
# https://github.com/slimtoolkit/slim

set -e

image_name="flask-htmx-app"

docker build -t $image_name .
docker run -it --rm -v /var/run/docker.sock:/var/run/docker.sock dslim/slim build $image_name
docker images | grep "${image_name}.slim"
