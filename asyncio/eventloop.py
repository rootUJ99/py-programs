import asyncio
import inspect
import requests


def an_hof(*h_args):
  def superwrapper(fn):
    def wrapper(*args, **kwargs):
      print('starts here')
      if inspect.iscoroutinefunction(fn):
        returnedFunc = fn(*args, **kwargs)
        
      print('ends here')
      return returnedFunc
    return wrapper
  return superwrapper



# @an_hof
async def multiple_requests():
  loop = asyncio.get_event_loop()
  # print('with event loop starts here')
  for i in range(10):
    f1 = loop.run_in_executor(None, requests.get, 'https://api.kanye.rest')
    req= await f1
    print(i, req.json())

# loop = asyncio.get_event_loop()
# loop.run_until_complete(multiple_requests())
# print('ended here')
@an_hof()
def muliple_requests_without_event_loop():
  # print('without event loop starts here')
  for i in range(10):
    f1 = requests.get('https://api.kanye.rest')
    print(i, f1.json())


# print('ended here')

# @an_hof
def with_generators():
  # print('with generators starts here')
  for i in range(10):
    f1 = yield requests.get('https://api.kanye.rest')
    print(i, f1.json())

# print('ended here')

if __name__ == "__main__":

  # muliple_requests_without_event_loop()
  # with_generators()
  print(len(inspect))