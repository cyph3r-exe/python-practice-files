import time
import tweepy
from github import Github

# Authenticate to Twitter
auth = tweepy.OAuthHandler("consumerkey", "consumertoken")
auth.set_access_token("accesskey", "accesssecret") 

api = tweepy.API(auth, wait_on_rate_limit=True)

# Authenticate to GitHub
github_token = "yourtoken"
g = Github(github_token)

def monitor_all_repos(username):
    user = g.get_user()
    for repo in user.get_repos():
        last_commit_sha = None

        while True:
            for commit in repo.get_commits():
                if commit.sha != last_commit_sha:
                    last_commit_sha = commit.sha
                    message = f"New commit to {repo.full_name}: {commit.commit.message}"

                    """
                    Quick explnation:
                    This next line of code is used to tweet the message. Since we don't have Twitter API OAuth 2.0 with PKCE, we can't tweet the message.
                    Hence, if you some money and want try some fun stuff out, you can uncomment the next line of code and tweet the message.

                    Also, this will post ALL COMMITS you've EVER made to ANY of your repositories. So, be careful with this code.
                    """

                    """
                    To only post the latest commit, I have attached this same function modified accordingly. So, you can make the changes and try it out.
                    Have fun.
                    
                    def monitor_all_repos(username):
                        user = g.get_user()
                        repo_last_commits = {}  # Store the last commit SHA for each repo

                        while True:
                            for repo in user.get_repos():
                                latest_commit = repo.get_commits()[0]
                                repo_name = repo.full_name
                                if repo_name not in repo_last_commits or repo_last_commits[repo_name] != latest_commit.sha:
                                    repo_last_commits[repo_name] = latest_commit.sha
                                    message = f"New commit to {repo_name}: {latest_commit.commit.message}"
                                    api.update_status(message)
                                    print(f"Tweeted: {message}")
                            time.sleep(60)
                    """
                    # api.update_status(message)
                    print(f"Tweeted: {message}")
            time.sleep(60)  

username = "cyph3r-exe"

