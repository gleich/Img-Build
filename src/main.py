from subprocess import call
import os
from time import sleep

from printing_utils import print_with_time
import file_utils
import git_interactions
import github_api


def main():
    """Main function for the program
    """
    configuration_file = file_utils.safe_file_read("config/config.yml", "yml")
    repos = []
    for repo in configuration_file["repos"]:
        git_interactions.clone_repo(repo["cloneURL"])
        print_with_time("📂 Gathering number of commits for " + repo, "yellow")
        print_with_time(
            "✅ Successfully gathered number of commits for " + repo, "green")
        repo_commit_amount = github_api.get_repo_commits(repo)
        repo_commit_nums[repo] = repo_commit_amount
    docker_username = configuration_file["docker"]["userName"]
    docker_password = file_utils.safe_file_read(
        "dockerPassword.txt", "txt").strip("\n")
    print_with_time("🔑  Logining into Docker Hub", "yellow")
    call(["echo", "'" + docker_password + "'", "|", "docker",
          "login", "-u", docker_username, "--password-stdin"])
    print_with_time("✅ Successfully logged into Docker Hub", "yellow")
    cycle_instance = 0
    while True:
        print_with_time("♻️ Starting cycle " + cycle_instance)
        built_images = []
        for repo in repos:
            newest_commit_amount = github_api.get_repo_commits(repos[repo])
            if newest_commit_amount > repos[repo]:
                print_with_time("🚀 " + repo + " updated; " + str(
                    repos[repo]) + " commits --> " + str(newest_commit_amount) + " commits", "blue")
                repos[repo] = newest_commit_amount
                os.chdir("./repos/" + repo)
                print_with_time("☁️ Pulling " + repo, "yellow")
                call["git", "pull"]
                print_with_time("✅ Successfully pulled " +
                                repo + " repo", "green")
                imageName = configuration_file["repos"][repo]["imageName"]
                imageTag = configuration_file["repos"][repo]["imageTag"]
                print_with_time("🐳 Building image for " + docker_username +
                                "/" + imageName + ":" + imageTag, "yellow")
                call(["docker", "build", "-t", docker_username +
                      "/" + imageName + ":" + imageTag])
                print_with_time("🐳 Successfully built image for " + docker_username +
                                "/" + imageName + ":" + imageTag, "green")
                built_images.append(docker_username +
                                    "/" + imageName + ":" + imageTag)
            else:
                print_with_time("💤 Nothing has changed for " + repo, "blue")
        if built_images != []:
            if "docker-compose.yml" in os.listdir():
                print_with_time("🧪 Testing images", "yellow")
                print_with_time("✅ Tests for images passed", "green")
                call(["docker-compose", "up", "-d"])
                sleep(configuration_file["general"]["testTime"])
                call(["docker-compose", "down"])
            for image in built_images:
                print_with_time("🐳 Pushing " + image, "yellow")
                call(["docker", "push", image])
                print_with_time("✅ Successfully pushed " + image, "green")
        print_with_time("🏁 Finshed cycle " + cycle_instance)
        print_with_time("⏰ Waiting 10 seconds for next repo check")
        cycle_instance += 1


main()
