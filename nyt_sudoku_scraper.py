import datetime
import json
import re
import requests

url = 'https://www.nytimes.com/puzzles/sudoku/hard'
response = requests.get(url)

pattern = r'<script type="text\/javascript">window\.gameData = (.+)<\/script><\/div><div id="portal-editorial-content">'
match = re.search(pattern, response.text)

today = datetime.date.today()


if match:
    data = json.loads(match.group(1))

    hard_puzzle = data['hard']['puzzle_data']['puzzle']
    sdk_output = f'#SNew York Times\n#B{today.strftime("%d-%m-%Y")}'
    for i in range(0, len(hard_puzzle)):
        if i % 9 == 0:
            sdk_output += '\n'
        if hard_puzzle[i] == 0:
            sdk_output += '.'
        else:
            sdk_output += str(hard_puzzle[i])

    save_path = f'./sudoku/nyt-hard-{today.strftime("%Y-%m-%d")}.sdk'
    with open(save_path, 'w') as f:
        f.write(sdk_output)
    print(f"Data saved to {save_path}")

else:
    raise Exception("Failed to find game data.")
