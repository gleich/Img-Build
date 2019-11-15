import github_api
import git_interactions
import file_utils
from printing_utils import print_with_time
import docker
from time import sleep
import os
from subprocess import call


print_with_time("🐳  Getting Docker Client", 0, "yellow")
docker_client = docker.from_env()
print_with_time("✅  Successfully got the Docker Client", 1, "green")
configuration_file = file_utils.safe_file_read("config/config.yml", "yml")
repos = {}  # RepoName: Number of commits
print_with_time("📩  Getting Commit Numbers for all repos and cloning them", 0, "white")
for repo in configuration_file["repos"]:
    print_with_time("☁️  Cloning " + repo, 1, "yellow")
    git_interactions.clone_repo(
        configuration_file["repos"][repo]["cloneURL"])
    print_with_time("✅  Successfully Cloned " + repo, 2, "green")
    print_with_time("🚀  Gathering number of commits for " + repo, 1, "yellow")
    repo_commit_amount = github_api.get_repo_commits(
        configuration_file["repos"][repo]["fullName"])
    print_with_time(
        "✅  Successfully gathered number of commits for " + repo, 2, "green")
    repos[configuration_file["repos"][repo]["fullName"]] = repo_commit_amount
docker_username = configuration_file["docker"]["userName"]
docker_password = file_utils.safe_file_read(
    "config/dockerPassword.txt", "txt").strip("\n")
print_with_time("🔑  Logining into Docker Hub", 0, "yellow")
docker_client.login(username=docker_username, password=docker_password)
print_with_time("✅  Successfully logged into Docker Hub", 1, "yellow")
cycle_instance = 0
while True:
    print_with_time("♻️  Starting cycle " +
                    str(cycle_instance), 0, "white")
    built_images = []
    for fullRepoName in repos:
        newest_commit_amount = github_api.get_repo_commits(fullRepoName)
        print_with_time("🎬  Starting for " + fullRepoName + " repo", 1, "yellow")
        if newest_commit_amount > repos[fullRepoName]:
            print_with_time("📭  " + fullRepoName + " updated; " + str(
                repos[fullRepoName]) + " commits --> " + str(newest_commit_amount) + " commits", 2, "blue")
            repos[fullRepoName] = newest_commit_amount
            os.chdir("./repos/" + fullRepoName)
            print_with_time("📩  Pulling " + fullRepoName, 3, "yellow", "True")
            call(["git", "pull"])
            print_with_time("✅  Successfully pulled " +
                            fullRepoName + " repo", 3, "green")
            imageName = configuration_file["repos"][fullRepoName]["imageName"]
            imageTag = configuration_file["repos"][fullRepoName]["imageTag"]
            print_with_time("🐳  Building image for " + docker_username +
                            "/" + imageName + ":" + imageTag, 3, "yellow", "True")
            call(["docker", "build", "-t", docker_username +
                    "/" + imageName + ":" + imageTag])
            print_with_time("✅  Successfully built image for " + docker_username +
                            "/" + imageName + ":" + imageTag, 3, "green")
            built_images.append(docker_username +
                                "/" + imageName + ":" + imageTag)
        else:
            print_with_time("💤  Nothing has changed for " + fullRepoName, 2, "blue")
    if built_images != []:
        for image in built_images:
            print_with_time("🐳  Pushing " + image, 2, "yellow", "True")
            call(["docker", "push", image])
            print_with_time("✅  Successfully pushed " + image, 0, "green")
    print_with_time("🏁  Finshed cycle " + str(cycle_instance), 0, "white")
    print_with_time("⏳  Waiting 10 seconds for next cycle", 0, "white")
    cycle_instance += 1
    sleep(10)

