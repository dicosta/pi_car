import tempfile
import subprocess
import os

MJPG_STREAMER_PATH = "mjpg_streamer"
INPUT_PATH = "/usr/local/lib/input_uvc.so" #  -r 640x320 -f 30 -q 100 r: resolution, f: frame per second, q: quality
# INPUT_PATH = "/usr/local/lib/input_uvc.so -r 640x320 -f 30 -q 100" # r: resolution, f: frame per second, q: quality
OUTPUT_PATH = "/usr/local/lib/output_http.so -w /usr/local/www"

stream_cmd = '%s -i "%s" -o "%s" &' % (MJPG_STREAMER_PATH, INPUT_PATH, OUTPUT_PATH)

def run_command(cmd):
	with tempfile.TemporaryFile() as f:
		subprocess.call(cmd, shell=True, stdout=f, stderr=f)
		f.seek(0)
		output = f.read()
	return output

def start():
	files = os.listdir('/dev')
	if 'video0' in files:
		run_command(stream_cmd)
	else:
		raise IOError("Camera is not connected correctly")

def start():
	files = os.listdir('/dev')
	print(stream_cmd)
	video_files = [f for f in files if 'video' in f]
	if not video_files:
		raise IOError("Camera is not connected correctly")
	run_command(stream_cmd)

def get_host():
	return run_command('hostname -I')

def stop():
	pid = run_command('ps -A | grep mjpg_streamer | grep -v "grep" | head -n 1')
	if pid == '':
		return False
	else:
		run_command('sudo kill %s' % pid)
		return True

def restart():
	stop()
	start()
	return True
