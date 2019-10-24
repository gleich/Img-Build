from subprocess import call
import os
import termcolor

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
        repo_commit_amount = github_api.get_repo_commits(repo)
        repo_commit_nums[repo] = repo_commit_amount
    docker_username = configuration_file["docker"]["userName"]
    docker_password = configuration_file["docker"]["password"]
    # echo ${{ secrets.docker_password }} | docker login -u ${{ secrets.docker_id }} --password-stdin
    print(termcolor.colored("🔑 Logining into Docker Hub", "yellow"))
    call(["echo", "'" + docker_password + "'", "|", "docker",
          "login", "-u", docker_username, "--password-stdin"])
    print(termcolor.colored("✅ Logged into Docker Hub", "yellow"))
    while True:
        for repo in repos:
            newest_commit_amount = github_api.get_repo_commits(repos[repo])
            if newest_commit_amount > repos[repo]:
                os.chdir("./repos/" + repo)
                call(["docker", "build", "-t", docker_username])
    
main()
