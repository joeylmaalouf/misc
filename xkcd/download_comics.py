import json
from os.path import exists
from pattern.web import URL


def download(url):
	return URL(string = url).download()


def download_comic(id_num):
	return json.loads(download("http://www.xkcd.com/{0}/info.0.json".format(id_num)))


def save_image(id_num, img_url):
	url_obj = URL(string = img_url)
	f = open("xkcd_comic_{0:04d}.jpg".format(id_num), "wb")
	f.write(url_obj.download())
	f.close()


def main():
	id_num = 0
	most_recent = json.loads(download("http://www.xkcd.com/info.0.json"))["num"]
	while id_num <= most_recent:
		if exists("xkcd_comic_{0:04d}.jpg".format(id_num)):
			print("Skipped download of comic number {0}; file already exists.".format(id_num))
		else:
			try:
				comic = download_comic(id_num)
				save_image(comic["num"], comic["img"])
				print("Comic number {0} successfully downloaded from \"{1}\".".format(comic["num"], comic["img"]))
			except:
				print("Error: Could not find comic with ID number {0}.".format(id_num))
		id_num += 1
	print("XKCD comic download complete!")


if __name__ == "__main__":
	main()
