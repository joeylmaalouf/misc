from optparse import OptionParser
import os
from pytube import YouTube
import re


def download(video_url = "youtu.be/dQw4w9WgXcQ", folder_path = "./"):
	if "youtube.com" in video_url:
		video_id = video_url.split("v=")[-1]
	elif "youtu.be" in video_url:
		video_id = video_url.split(".be/")[-1]
	else:
		video_id = video_url
	video_id = re.search("[\w-]+", video_id).group(0)

	yt = YouTube()
	yt.from_url("http://www.youtube.com/watch?v={}".format(video_id))
	yt.filter("mp4")[-1].download(path = folder_path, force_overwrite = True)


if __name__ == "__main__":
	parser = OptionParser(description = "A tool for downloading YouTube videos. You can supply video URLs/IDs as any number of direct arguments, or put each on its own line in a list file and use the -f option. Use the -o option to specify the output directory.")
	parser.add_option("-f", "--fromfile", action = "store", dest = "fromfile", help = "specify a source file that contains video URLs/IDs")
	parser.add_option("-o", "--outputdir", action = "store", dest = "outputdir", help = "specify the path to the directory where the videos will be saved")
	options, args = parser.parse_args()
	if len(args) == 0 and not options.fromfile:
		print("use the -h flag for help!")

	path = options.outputdir+"/" if options.outputdir else "./"
	if not os.path.isdir(path):
		os.makedirs(path)

	for video_id in args:
		download(video_id, path)

	if options.fromfile:
		with open(options.fromfile, "r") as listfile:
			video_ids = listfile.read().split("\n")
		for video_id in video_ids:
			if video_id.strip():
				download(video_id, path)
