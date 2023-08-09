# Check YT title for str

Simple script that goes through YT links from a file and checks if any of the video's title contains a specified string.

## Setup

- Unix
	```bash
	# 1. Create virtual env:
	python3 -m venv venv
	
	# 2. Activate virtual env:
	source venv/bin/activate 
	
	# 3. Install required pkgs:
	pip install -r requirements.txt
	```
- Windows
	```bash
	# 1. Create virtual env:
	python3 -m venv venv
	
	# 2. Activate virtual env:
	.\venv\Scripts\activate 
	
	# 3. Install required pkgs:
	pip install -r requirements.txt
	```

## Usage

1. Create an `input.txt` file with links to YouTube videos / shorts separated by new line:
	```text
	https://www.youtube.com/watch?v=r6tH55syq0o
	https://www.youtube.com/shorts/qol2X_8JF9I
	https://www.youtube.com/watch?v=BPadRwJbylY
	```
2. Open `script.py` and enter the string you're searching for in the `string_to_check_for` variable:
	```python
	string_to_check_for = "changing"
	```
3. Run the script:
	```bash
	python3 script.py
	```
4. After the progress bar finishes (don't worry it will stop for a few seconds every `15` requests) you can open the `output.txt` file and easily search it for the videos that either do or don't include the string you're interested in their title (it's `True` for those that do and `False` for those that don't)

	\*In vim: `g!/True/d` / `g!/False/d`
