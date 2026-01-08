Docker uses a layer cache to speed up builds. Each instruction in a Dockerfile creates a new layer. If you haven’t changed the instruction and its previous layers, Docker will reuse the cached layer.


To see the layers of an image:

docker history my-nginx-image:v2