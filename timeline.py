from setup import user

# Get the start and end dates of each repo
start_dates = {}
end_dates = {}
for repository in user.get_repos():
    start_dates[repository] = repository.created_at
    end_dates[repository] = repository.updated_at

# Order the repos by their start dates
ordered_start = sorted(start_dates, key=lambda repo: start_dates[repo])

# Print out the repos and their corresponding creation and update times
print("Repositories and their creation/update times")
max_length = max(user.get_repos(), key=lambda repo: len(repo.name))
for repository in ordered_start:
    print(f"{repository.name}{' ' * (len(max_length.name) - len(repository.name))} {'-'*5} created at {str(start_dates.get(repository))} {'-'*5} last updated at {str(end_dates.get(repository))}")
print()
