from evdev import InputDevice, list_devices


BUTTONS = {
  288: "X",
  289: "A",
  290: "B",
  291: "Y",
  292: "L",
  293: "R",
  295: "Z",
  297: "Start",
  300: "DPadUp",
  301: "DPadRight",
  302: "DPadDown",
  303: "DPadLeft"
}
CODES = {
  value: key for key, value in BUTTONS.items()
}


class GCAdapter(object):
  # http://www.mayflash.com/Products/PCUSB/PC051.html
  def __init__(self, whitelist = [], blacklist = [], verbose = False):
    # whitelist: device paths to scan; if empty, scan all connected device paths instead
    # blacklist: device paths to ignore
    # verbose: if True, print any useful information
    super(GCAdapter, self).__init__()
    devices = whitelist if whitelist else list_devices()
    self.controllers = [InputDevice(path) for path in devices if path not in blacklist]
    if verbose:
      print("Capturing input from the following devices: ")
      for c in self.controllers:
        print(c)

  def get_controller_state(self, device_num = 0):
    try:
      pressed = self.controllers[device_num].active_keys()
    except IndexError:
      raise IndexError("Invalid device index given! Please make sure your controllers are plugged in.")
    return {
      button_code: button_code in pressed for button_code in BUTTONS.keys()
    }


if __name__ == "__main__":
  from time import sleep
  # adapter = GCAdapter(whitelist = ["/dev/input/event7", "/dev/input/event8"], blacklist = [], verbose = True)
  # adapter = GCAdapter(whitelist = [], blacklist = ["/dev/input/event7"], verbose = True)
  adapter = GCAdapter(verbose = True)
  while True:
    pressed = adapter.get_controller_state(0)
    print(pressed)
    sleep(1.0 / 60)
    if pressed[CODES["L"]] and pressed[CODES["R"]] and pressed[CODES["A"]] and pressed[CODES["Start"]]:
      break

# TODO: Control Stick and C-Stick
