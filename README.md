# Auto-Build-Images-Anywhere

![GitHub contributors](https://img.shields.io/github/contributors/Matt-Gleich/Auto-Build-Images-Anywhere)

🐳 Easily build an image when pushed to master on anything that runs docker

## Github Actions

| Action                                                                                                                                                                                      | Action Description                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| [![Actions Status](https://github.com/Matt-Gleich/Auto-Build-Images-Anywhere/workflows/Python-Versions/badge.svg)](https://github.com/Matt-Gleich/Auto-Build-Images-Anywhere/actions) | Testing for Python 3.6, 3.7, and 3.7-dev |
| [![Actions Status](https://github.com/Matt-Gleich/Auto-Build-Images-Anywhere/workflows/Python-Cron/badge.svg)](https://github.com/Matt-Gleich/Auto-Build-Images-Anywhere/actions)     | Cron job for the Python-Versions action  |

## Setup

There are a few things that you need to have installed before you use this program:

1. Python 3
2. Docker (Make sure your logged in so you can push to docker hub)
3. Pip
4. Git

You then can clone this repo, `cd` into it, and run the following command:

1. `pip3 install -r requirements.txt`

Then make sure that you have the config.yml file in the img-build-configs folder located at root. If you need to know how to write the config.yml file, look at the second down below:

## Config File

In order to outline what repos you want the img-build program to build and some other general configuration, you need to make the config file. The file should be called `config.yml` and should have the general outline:

```yml
docker:
  userName: "mattgleich"
testTime: 20
repos:
  Scrape-Calendar-Data:
    cloneURL: "https://github.com/goffstown-sports-app/Scrape-Calendar-Data.git"
    imageName: "scrape-calendar-data"
    imageTag: "arm32v7"
  Server-Monitor:
    cloneURL: "https://github.com/goffstown-sports-app/Server-Monitor.git"
    imageName: "server-monitor"
    imageTag: "arm32v7"
```

testTime stands for the amount of time between cycles in seconds.

## How it works

This application begins by cloning all of the repositories. It then starts the first cycle. A cycle works by running the `git pull` command for each repo. If the output of `git pull` command shows that the command did in fact pull changes, then the image will be built and pushed up to docker hub. Once it has done this for each repo, the cycle is done and the next cycle will start based off of the time set for the `testTime` key.
