from base64 import *
from requests import get
from sys import argv


def chat_code_to_id(chat_code):
  if chat_code[:2] == "[&" and chat_code[-1] == "]":
    chat_code = chat_code[2:-1]
  id_val = 0
  hexstr = reversed(b64decode(chat_code)[2:])
  for byte in hexstr:
    id_val *= 256
    id_val += ord(byte)
  return id_val

def id_to_chat_code(id_val, quantity = 1):
  # https://wiki.guildwars2.com/wiki/Chat_link_format
  chat_code = "\x02" + chr(quantity)
  for _ in range(4):
    chat_code += chr(id_val % 256)
    id_val /= 256
  return "[&" + b64encode(chat_code) + "]"

def item_details(id_val):
  data = get("https://api.guildwars2.com/v2/items/{0}".format(id_val)).json()
  return { prop: data[prop] for prop in ["name", "description", "level", "rarity", "restrictions"] }

def item_prices(id_val):
  data = get("https://api.guildwars2.com/v2/commerce/prices/{0}".format(id_val)).json()
  return {
    "lowest_sell": data["sells"]["unit_price"],
    "highest_buy": data["buys"]["unit_price"]
  }

def copper_to_coins(copper, as_dict = False):
  coins = (copper // 10000, copper % 10000 // 100, copper % 100)
  if as_dict:
    return dict(zip(["gold", "silver", "copper"], coins))
  else:
    return coins


if __name__ == "__main__":
  if len(argv) < 2:
    argv.append(raw_input("Please enter an item's ID value or chat code: "))
  try:
    item_id = int(argv[1])
  except ValueError:
    item_id = chat_code_to_id(argv[1])
  prices = item_prices(item_id)
  print("Lowest sell: {}".format(copper_to_coins(prices["lowest_sell"])))
  print("Highest buy: {}".format(copper_to_coins(prices["highest_buy"])))
