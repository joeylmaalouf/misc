from evdev import ecodes, InputDevice, list_devices


# code to button mapping
BUTTONS = {
  000: "Control Stick X",
  001: "Control Stick Y",
  002: "C Stick Y",
  003: "L Analog",
  004: "R Analog",
  005: "C Stick X",
  288: "X",
  289: "A",
  290: "B",
  291: "Y",
  292: "L Digital",
  293: "R Digital",
  295: "Z",
  297: "Start",
  300: "DPad Up",
  301: "DPad Right",
  302: "DPad Down",
  303: "DPad Left"
}
# button to code mapping
CODES = {
  value: key for key, value in BUTTONS.items()
}


class GCAdapter(object):
  # http://www.mayflash.com/Products/PCUSB/PC051.html
  def __init__(self, whitelist = [], blacklist = [], verbose = False):
    # whitelist: device paths to attach to; if empty, use all connected device paths instead
    # blacklist: device paths to ignore
    # verbose: if True, print any useful information
    super(GCAdapter, self).__init__()
    devices = whitelist if whitelist else list_devices()
    self.controllers = [InputDevice(path) for path in devices if path not in blacklist]
    self.controller_states = [{code: 0 for code in BUTTONS.keys()} for _ in self.controllers]
    if verbose:
      print("Capturing input from the following devices: ")
      for c in self.controllers:
        print(c)

  def update(self):
    for i in range(len(self.controllers)):
      try:
        for event in self.controllers[i].read():
          # button events: digital, value 1 => pressed, value 0 => released
          # joystick events: analog, value = position
          if event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
            state[event.code] = int(event.value)
      except IOError:
        # no events found
        pass


if __name__ == "__main__":
  # example usage
  from time import sleep
  # adapter = GCAdapter(whitelist = ["/dev/input/event17", "/dev/input/event18"], blacklist = [], verbose = True)
  # adapter = GCAdapter(whitelist = [], blacklist = ["/dev/input/event17"], verbose = True)
  adapter = GCAdapter(verbose = True)
  while True:
    sleep(1.0 / 60)
    adapter.update()
    state = adapter.controller_states[0]
    print(state)
    # L + R + A + Start to quit
    if state[CODES["L Digital"]] and state[CODES["R Digital"]] and state[CODES["A"]] and state[CODES["Start"]]:
      break
