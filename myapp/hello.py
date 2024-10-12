import fire

def hello(name="World"):
  return "Hello %s!" % name % "I hope everything is great"

if __name__ == '__main__':
  fire.Fire(hello)
