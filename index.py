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
  data = getFile()
  correctNumbers = []

  for value in data:
    if len(value) > 0:
      wholeSum = 0
      strongSum = 0
      value = value.strip()
      for singleNumber in value:
        for i in range(1, int(singleNumber)): # Factorial with singleNumber
          if strongSum == 0: # If it's first number (strongSum == 0)
            strongSum = i
          else:
            strongSum *= i
          if(value == '145'):
            print(singleNumber, i)
        # Sum factorial with whole sum and reset factorial counter for next loop
        wholeSum += strongSum
        strongSum = 0

      if wholeSum == int(value):
        correctNumbers.append(int(value))

  return '4.2 ' + str(correctNumbers)

def thirdEx():
  return '4.3'


print(firstEx())

print(secondEx())

print(thirdEx())