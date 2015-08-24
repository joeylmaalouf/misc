def switch(case_dict, val, default):
  return case_dict.get(val, default)


if __name__ == "__main__":
  cases = {
    1: "123",
    2: "456"
  }
  for i in range(3):
    print(switch(cases, i, "default"))
