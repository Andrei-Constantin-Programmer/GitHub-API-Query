# Script based on original script by Milovan Gveric (Unknown807)

from setup import user

ignored_languages = ["Objective-C", "CMake", "GLSL"]

# Get languages across all repositories in a dictionary
language_count = {}
for repo in user.get_repos():
    repo_languages = repo.get_languages()
    for lang in repo_languages.keys():
        if lang not in ignored_languages:
            language_count[lang] = language_count.get(lang, 0) + repo_languages[lang]

# Calculate the frequency of each language
total_sum = sum([value for key, value in language_count.items()])
frequency = language_count.copy()
for lang, count in language_count.items():
    frequency[lang] = round(100 * count / total_sum, 2)

# Sort the languages in descending order
sorted_languages = sorted(frequency, key=lambda language: language_count[language], reverse=True)

# Get the language with the longest length
max_length = max(sorted_languages, key=lambda key: len(key))

# Print the languages and their frequencies
print("Programming languages and their frequency")
for lang in sorted_languages:
    print((lang + ' ' * (len(max_length) - len(lang))) + "\t\t" + str(frequency[lang]) + "%")
print()
