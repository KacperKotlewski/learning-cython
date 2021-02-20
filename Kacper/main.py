from henlo.subpkg import util
from henlo import wrapper

if __name__ == '__main__':
    print(util._chars("xd"))
    name = input("give me your name! ")
    wrapper.test(name)
