__author__ = 'bwade'

from aquadome import Aquadome

if __name__ == '__main__':
    d = Aquadome()
    d.main()
    for gb in d.growbeds:
        print(gb.getmydesignation())
    d.fishtank.feedfish()
    d.fishtank.setph(6.8)
    print("ph: %f" % d.fishtank.getph())
    d.fishtank.setwatertemp(75)
    print("water temp: %f" % d.fishtank.getwatertemp())
