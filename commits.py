from setup import user

repo_commits = {}

# Get the number of commits
for repository in user.get_repos():
    repo_commits[repository] = repository.get_commits().totalCount

# Order the repositories by number of commits
most_active = sorted(repo_commits, key=lambda repo: repo_commits[repo])

# Print the repositories and their respective number of commits
print("Repositories and the number of commits")
max_length = max(user.get_repos(), key=lambda repo: len(repo.name))
for repository in most_active:
    print(f"{repository.full_name} {(' ' * (len(max_length.name) - len(repository.name)))} \t "
          f"{str(repo_commits[repository])}")
print()
