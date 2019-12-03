import git_interactions
import file_utils
from printing_utils import print_with_time
import docker
from time import sleep
import os
from subprocess import call
import subprocess


print_with_time("🐳  Getting Docker Client", 0, "yellow")
docker_client = docker.from_env()
print_with_time("✅  Successfully got the Docker Client", 1, "green")
configuration_file = file_utils.safe_file_read("config/config.yml", "yml")
repos = []  # Path of each repo
print_with_time("📩  Cloning all repos", 0, "white")
call(["rm", "-rf", "repos"])
for repoName in configuration_file["repos"]:
    print_with_time("☁️  Cloning " + repoName, 1, "yellow")
    git_interactions.clone_repo(
        configuration_file["repos"][repoName]["cloneURL"])
    print_with_time("✅  Successfully Cloned " + repoName, 2, "green")
    repos.append(repoName)
docker_username = configuration_file["docker"]["userName"]
cycle_instance = 0
while True:
    print_with_time("♻️  Starting cycle " +
                    str(cycle_instance), 0, "white")
    built_images = []
    for repo in repos:
        os.chdir("./repos/" + repo)
        gitPull = os.popen('git pull').read()
        if gitPull != "Already up to date.\n":
            print_with_time("📭  " + repo + " updated", 1, "blue")
            print_with_time("✅  Successfully pulled " +
                            repo + " repo", 2, "green")
            imageName = configuration_file["repos"][repo]["imageName"]
            imageTag = configuration_file["repos"][repo]["imageTag"]
            print_with_time("🐳  Building image for " + docker_username +
                            "/" + imageName + ":" + imageTag, 2, "yellow")
            try:
                Dockerfile = configuration_file["repos"][repo]["file"]
                call(["docker", "build", "-f", Dockerfile, "-t", docker_username +
                      "/" + imageName + ":" + imageTag, "."], stdout=subprocess.PIPE)
            except KeyError:
                call(["docker", "build", "-t", docker_username +
                    "/" + imageName + ":" + imageTag, "."], stdout=subprocess.PIPE)
            print_with_time("✅  Successfully built image for " + docker_username +
                            "/" + imageName + ":" + imageTag, 2, "green")
            built_images.append(docker_username +
                                "/" + imageName + ":" + imageTag)
        else:
            print_with_time("💤  Nothing has changed for " + repo, 2, "blue")
        os.chdir("../..")
    if built_images != []:
        for image in built_images:
            print_with_time("🐳  Pushing " + image, 1, "yellow")
            call(["docker", "push", image], stdout=subprocess.PIPE)
            print_with_time("✅  Successfully pushed " + image, 1, "green")
        built_images = []
    print_with_time("🏁  Finshed cycle " + str(cycle_instance), 0, "white")
    sleep_time = configuration_file["testTime"]
    print_with_time("⏳  Waiting {} seconds for next cycle", 0, "white".format(sleep_time))
    cycle_instance += 1
    sleep(sleep_time)

