import math

def getFile():
  with open('przyklad.txt') as file:
    data = file.read()
    array = data.split('\n')

    return array


def firstEx():
  data = getFile()
  howMany = 0

  for value in data: # Loop throgh values
    if len(value) > 0:
      sqrNumber = int(value) # Set value to int
      if sqrNumber >= 0: # Do it if its higher than 3
        while sqrNumber > 4:
          sqrNumber = math.sqrt(sqrNumber)
        if sqrNumber == 3:
          howMany += 1

  return '4.1: '+ str(howMany)

def secondEx():
  return '4.2'

def thirdEx():
  return '4.3'


print(firstEx())

print(secondEx())

print(thirdEx())