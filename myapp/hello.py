import fire

def hello(name="World"):
  return "Hello %s! I hope everything is great" % name


if __name__ == '__main__':
  fire.Fire(hello)
