import numpy as np
import math
from PIL import Image

def attacker_success(n, fail_chance, report_chance):
  if n == 0:
    return 0.0
  this_user = fail_chance
  following_users = attacker_success(n - 1, fail_chance, report_chance) * (1.0 - report_chance - fail_chance)
  return this_user + following_users

table = np.empty((401, 401, 3), np.uint8)

for y in range(401):
  for x in range(401):
    fail_chance = x * 0.0025 * 0.1
    report_chance = (400 - y) * 0.0025 * 0.1
#    print (fail_chance, report_chance, 255 * attacker_success(200, fail_chance, report_chance))
    if fail_chance + report_chance > 1.0:
      table[y][x][0] = 0
      table[y][x][1] = 0
      table[y][x][2] = 0
    else:
      colour = round(255 * attacker_success(200, fail_chance, report_chance))
      table[y][x][0] = colour
      table[y][x][1] = 0
      table[y][x][2] = 255 - colour

im = Image.fromarray(table)
im.save("gradient-closeup.png")

