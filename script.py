import json
import time
import urllib
import urllib.request
from tqdm import tqdm


# *this is case insensitive but doesn't support regex!!!
# *it's better to check for a smaller piece than a more complex one
# as there's a much higher chance of getting it
string_to_check_for = ""
input_filename = 'input.txt' # <- yt / yt short links separated by `\n`

every_wait = 0.5 # <- wait in s between every req
bunch_wait = 5   # <- wait in s between 15 req


# Going through each line (URL) of the file:
counter = 0
base_url = 'https://www.youtube.com/'

output_file = open('output.txt', 'w')

for line in tqdm(open(input_filename, 'r').readlines()):
    counter += 1
    time.sleep(every_wait)

    if (counter % 15) == 0:
        time.sleep(bunch_wait)

    # Remove trailing `\n`:
    line = line.rstrip()

    # Get video ID:
    video_id = line.split('/')[-1].split('?v=')[-1]

    # Get video metadata and check title
    # <https://stackoverflow.com/questions/1216029/get-title-from-youtube-videos>
    params = {
        'format': 'json',
        'url': f'{base_url}watch?v={video_id}'
    }
    query_string = urllib.parse.urlencode(params)
    url = f'{base_url}oembed?{query_string}'
    
    # Catching 404 and other errors:
    try:
        with urllib.request.urlopen(url) as response:
            response_text = response.read()
            data = json.loads(response_text.decode())
        
            output_file.write(line + ' ' + str(string_to_check_for.lower() in data['title'].lower()) + '\n')
    except Exception:
        output_file.write(line + ' Err\n')

output_file.close()
