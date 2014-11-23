from period import Period
from knut1 import Knut
from lkm2 import LKM
from mm3 import MM
from pm4 import PM
from cts5 import CTS
from mine6 import Mine


class Interf():

    @staticmethod
    def knut():
        seed = 380636297739.0
        km = Knut(seed)
        count = 50
        for i in reversed(range(1, count)):
            rand = km.get_next()
            print "Random number #%d\t - \t%d" % (count - i + 1, rand)
        print "Period: ", Period(Knut(seed)).find_period()

    @staticmethod
    def lkm():
        # m - modulus, m > 0
        # a - multiplier, 0 <= a < m
        # c - increment, 0 <= c < m
        # x - start, 0 <= x < m
        count = 50
        x = 11
        a = 7
        c = 17
        m = 2230
        lkm = LKM(x, a, c, m)

        for i in range(1, count):
            rand = lkm.get_next()
            print "Random number #%d\t - \t%d" % (i, rand)
        print "Period: ", Period(LKM(x, a, c, m)).find_period()

    @staticmethod
    def mm():
        count = 350
        mm = MM(25, count)
        for i in range(0, count):
            rand = mm.get_next()
            print "Random number #%d\t - \t%d" % (i, rand)
        print "Period: ", Period(MM(25, count)).find_period()

    @staticmethod
    def pm():
        count = 50
        rands = []
        pm = PM()
        for i in range(0, count):
            rands.append(pm.get_next())
            print "Random number #%d\t - \t%d" % (i, rands[i])
        print "Period: ", Period(PM()).find_period()

    @staticmethod
    def cts():
        count = 40
        cts = CTS(50, count)
        for i in range(1, count):
            rand = cts.get_next()
            print "Random number #%d\t - \t%d" % (i, rand)
        print "Period: ", Period(CTS(50, count)).find_period()

    @staticmethod
    def mine():
        mi = Mine()
        count = 50
        for i in reversed(range(1, count)):
            rand = mi.get_next()
            print "Random number #%d\t - \t%d" % (count - i + 1, rand)
        print "Period: ", Period(Mine()).find_period()
