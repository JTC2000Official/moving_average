import timeit
from moving_average import *


m = MovingAverage(100)
m2 = MovingAverage(10000)
m3 = MovingAverage(1000000)

def setup1():
    for i in range(100):
        m.addSample(i*2)

def setup2():
    for i in range(10000):
        m2.addSample(i*2)

def setup3():
    for i in range(1000000):
        m3.addSample(i*2)

def average1():
    m.getAverage()

def average2():
    m2.getAverage()

def average3():
    m3.getAverage()



if __name__ == "__main__":
    print("-----------")
    starttime = timeit.default_timer()
    setup1()
    print("addSample with N=100 was executed in :", timeit.default_timer() - starttime, " seconds!")
    starttime = timeit.default_timer()
    average1()
    print("getAverage with N=100 was executed in :", timeit.default_timer() - starttime, " seconds!")
    print("-----------")
    starttime = timeit.default_timer()
    setup2()
    print("addSample with N=10.000 was executed in :", timeit.default_timer() - starttime, " seconds!")
    starttime = timeit.default_timer()
    average2()
    print("getAverage with N=10.000 was executed in :", timeit.default_timer() - starttime, " seconds!")
    print("-----------")
    starttime = timeit.default_timer()
    setup3()
    print("addSample with N=1.000.000 was executed in :", timeit.default_timer() - starttime, " seconds!")
    starttime = timeit.default_timer()
    average3()
    print("getAverage with N=1.000.000 was executed in :", timeit.default_timer() - starttime, " seconds!")
    print("-----------")
