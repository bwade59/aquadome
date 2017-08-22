__author__ = 'bwade'

from aquadome import Aquadome

if __name__ == '__main__':
    d = Aquadome()
    d.main()
    for gb in d.growbeds:
        print(gb.getmydesignation())
    d.fishtank.feedfish()
    d.fishtank.setph(6.8)
    print("ph: %0.2f" % d.fishtank.getph())
    d.fishtank.setwatertemp(75)
    print("water temp: %0.1f" % d.fishtank.getwatertemp())
    d.setairtemp(75)
    print("air temp: %0.1f" % d.getairtemp())
