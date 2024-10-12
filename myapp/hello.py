import fire

def hello(name="World"):
    return "Hello %s! I hope everything is great, and now we are using vim to edit this filet" % name


if __name__ == '__main__':
  fire.Fire(hello)
