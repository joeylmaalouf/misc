def cipher(string, shift):
  return "".join(chr(ord(c) + shift) for c in string)

if __name__ == "__main__":
  message = "Top-secret stuff!"
  key = 5
  encrypted = cipher(message, key)
  decrypted = cipher(encrypted, -key)
  print("Original:           {0}".format(message))
  print("Encrypted with {0: 3d}: {1}".format(key, encrypted))
  print("Decrypted with {0: 3d}: {1}".format(-key, decrypted))
  print("Success:            {0}".format(message == decrypted))
