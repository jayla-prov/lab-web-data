# Load master_2009.json through master_2018.json, analyze the tweets, and make a bar chart.
# Follow the linked course assignment in README.md.
import json
import matplotlib.pyplot as plt

tweets = []

for year in range(2009, 2019):
    filename = f'master_{year}.json'
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)
    tweets.extend(data)

print('Total tweets:', len(tweets))

phrases = [
    'Obama',
    'Trump',
    'Mexico',
    'Russia',
    'Fake News',
    'wall',
    'America',
    'jobs'
]

counts = []

for phrase in phrases:
    count = 0
    for tweet in tweets:
        if 'full_text' in tweet:
            message = tweet['full_text']
        else:
            message = tweet['text']

        if phrase.lower() in message.lower():
            count += 1

    counts.append(count)
    print(phrase, count)

print()
print('| phrase            | percent of tweets |')
print('| ----------------: | ----------------- |')

for i in range(len(phrases)):
    percent = counts[i] / len(tweets) * 100
    print(f'| {phrases[i]:>17} | {percent:05.2f}             |')

plt.figure(figsize=(8, 5))
plt.barh(phrases, counts)
plt.xlabel('Number of tweets')
plt.ylabel('Phrase')
plt.title('Phrase frequency in the 2009–2018 tweet archive')
plt.tight_layout()
plt.savefig('tweets.png')
plt.close()