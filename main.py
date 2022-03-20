import time
import numpy as np
import sys

# Print the text slowly with a delay print like gameboy
def delay_print(self, str):
  for char in str:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)



if __name__ == '__main__':
  pass