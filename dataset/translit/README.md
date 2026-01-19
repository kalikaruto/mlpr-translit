# How to use translit/

## Build the image

```bash
## install docker and build the image using
docker build -t translit:dev .

# this will download all the tools and python libraries
```

## Run the image

```bash
## run the image in detached mode
docker run -d --rm \
    -p 8000:8000 \
    -v $(pwd)/app:/app \
    translit:dev
```

`Note:` run the above cmd from the ../translit/app/

```bash
## check if docker is running
docker ps -a

## this will output with columns
# CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                                         NAMES

## not the NAMES to later stop the container
```

## Do data generation

`Note:` ../data/english/SOME_FILE_WITH_TXT should be there. The file should have sentences per line.

```bash
## run the python script from ../translit/../ that is the parent of translit
python batch_transliterate.py
```

## Stop the container

```bash
docker stop NAME

## name from the NAMES from the output of docker ps -a
```
