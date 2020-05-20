import math

def getFile():
  with open('przyklad.txt') as file:
    data = file.read()
    array = data.split('\n')

    return array


def firstEx():
  data = getFile()
  howMany = 0
  powerOf3 = []
  i = 0
  while True:
    p = 3**i
    powerOf3.append(p)
    if p > 1000000:
      break
    i += 1

  for value in data: # Loop throgh values
    if len(value.strip()) > 0:
      if int(value) in powerOf3:
        howMany += 1

  return '4.1: '+ str(howMany)

def secondEx():
  return '4.2'

def thirdEx():
  return '4.3'


print(firstEx())

print(secondEx())

print(thirdEx())