from subprocess import call
import os

from printing_utils import print_with_time
import file_utils
import git_interactions
import github_api

def main():
    """Main function for the program
    """
    configuration_file = file_utils.safe_file_read("config.yml", "yml")
    repos = []
    for repo in configuration_file["repos"]:
        git_interactions.clone_repo(repo["cloneURL"])
        print_with_time("📂 Gathering number of commits for " + repo, "yellow")
        print_with_time(
            "✅ Successfully gathered number of commits for " + repo, "green")
        repo_commit_amount = github_api.get_repo_commits(repo)
        repo_commit_nums[repo] = repo_commit_amount
    docker_username = configuration_file["docker"]["userName"]
    docker_password = configuration_file["docker"]["password"]
    print_with_time("🔑  Logining into Docker Hub", "yellow")
    call(["echo", "'" + docker_password + "'", "|", "docker",
          "login", "-u", docker_username, "--password-stdin"])
    print_with_time("✅ Successfully logged into Docker Hub", "yellow")
    while True:
        for repo in repos:
            newest_commit_amount = github_api.get_repo_commits(repos[repo])
            if newest_commit_amount > repos[repo]:
                print_with_time("🚀 " + repo + " updated; " + str(repos[repo]) + " commits --> " + str(newest_commit_amount) + " commits", "blue")
                repos[repo] = newest_commit_amount
                os.chdir("./repos/" + repo)
                imageName = configuration_file["repos"][repo]["imageName"]
                imageTag = configuration_file["repos"][repo]["imageTag"]
                print_with_time("🐳 Building image for " + docker_username + "/" + imageName + ":" + imageTag, "yellow")
                call(["docker", "build", "-t", docker_username + "/" + imageName + ":" + imageTag])
                print_with_time("🐳 Successfully built image for " + docker_username +
                                "/" + imageName + ":" + imageTag, "yellow")
                os.chdir("../..")
            else:
                print_with_time("💤 Nothing has changed for " + repo, "blue")
        print_with_time("🏁 Finshed Cycle")
        print_with_time("⏰ Waiting 10 seconds for next repo check")
            
    
main()
