import os

from github import Github

# Setup user with token
g = Github(os.environ["access_token"])
user = g.get_user("Andrei-Constantin-Programmer")
