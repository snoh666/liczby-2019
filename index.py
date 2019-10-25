def getFile():
  with open('przyklad.txt') as file:
    data = file.read()
    array = data.split('\n')

    return array


def firstEx():
  print(getFile())
  return '4.1'

def secondEx():
  return '4.2'

def thirdEx():
  return '4.3'


print(firstEx())

print(secondEx())

print(thirdEx())