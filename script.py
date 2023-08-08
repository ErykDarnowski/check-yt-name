import json
import urllib
import urllib.request

video_id = 'H-VItggRvWA' 

params = { 'format': 'json', 'url': f'https://www.youtube.com/watch?v={video_id}'}
query_string = urllib.parse.urlencode(params)
url = f'https://www.youtube.com/oembed?{query_string}'

# Get video metadata -> title <https://stackoverflow.com/questions/1216029/get-title-from-youtube-videos>:
with urllib.request.urlopen(url) as response:
    response_text = response.read()
    data = json.loads(response_text.decode())

    print(data['title'])
