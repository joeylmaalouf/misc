from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sys import argv
from time import sleep


def main(argv):
	if len(argv) < 2:
		argv.append("selenium python")

	browser = webdriver.Firefox()
	browser.get("http://www.google.com")
	assert "Google" in browser.title

	elem = browser.find_element_by_name("q")  # Find the search box
	elem.send_keys(" ".join(argv[1:]) + Keys.RETURN)

	sleep(5)
	browser.quit()


if __name__ == "__main__":
	main(argv)
