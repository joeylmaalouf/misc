from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


def lmgtfy(query):
  driver = webdriver.Firefox()
  driver.maximize_window()
  driver.get("https://www.google.com")
  assert "Google" in driver.title, "Cannot access Google."
  search_box = driver.find_element_by_name("q")
  for key in query:
    search_box.send_keys(key)
    sleep(0.125)
  search_box.send_keys(Keys.RETURN)
  # driver.close()


def open_pages(urls):
  driver = webdriver.Firefox()
  driver.maximize_window()
  for i, url in enumerate(urls):
    driver.get(url)
    # assert url == driver.current_url, "Redirected!"
    if i < len(urls) - 1:
      driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "t")
  # driver.quit()


def archive(url, filename):
  driver = webdriver.Firefox()
  driver.maximize_window()
  driver.get(url)
  driver.save_screenshot(filename)
  driver.quit()


if __name__ == "__main__":
  lmgtfy("never gonna give you up")
  open_pages([
    "https://www.reddit.com/r/SmashBros",
    "https://www.reddit.com/r/SSBPM",
    "https://www.reddit.com/r/DotA2"
  ])
  archive("https://www.twitch.tv", "archived_twitch.png")
