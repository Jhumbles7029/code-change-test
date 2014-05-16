import time
bottles = 10
while bottles > 0:
  print("{0} green bottles, hanging on the wall".format(bottles))
  time.sleep(2.5)
  print("{0} green bottles, hanging on the wall".format(bottles))
  time.sleep(2.5)
  print("And if 1 green bottle should acidentally fall,")
  time.sleep(2.5)
  bottles = bottles - 1
  print("They'll be {0} green bottles hanging on the wall.\n".format(bottles))
  time.sleep(3.5)
print("No green bottles, hanging on the wall")
time.sleep(2.5)
print("No green bottles, hanging on the wall")
time.sleep(2.5)
print("And I don't know how to sing this part of the song, so:")
time.sleep(2.5)
print("There's no green bottles hanging on the wall.")
