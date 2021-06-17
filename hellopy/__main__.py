import sys

try:
  name = sys.argv[1]
except:
  name = 'WORLD'

print('Hello {0}!'.format(name))