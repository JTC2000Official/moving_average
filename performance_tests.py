
import timeit

mysetup = """
import moving_average
module = moving_average.MovingAverage(N)
for i in range(100):
    module.addSample(i)
"""

mysetup2 = """
module = moving_average.MovingAverage(N)
for i in range(10000):
    module.addSample(i)
"""

mysetup3 = """
module = moving_average.MovingAverage(N)
for i in range(1000000):
    module.addSample(i)
"""

test="""
def test_addsample_withoutSamples(N):
    module = moving_average.MovingAverage(N)
    for i in range(N):
        module.addSample(i)
"""

def test_addsample_withSamples(N):
    module.addSample(N)

def test_getAverage(N):
    module = moving_average.MovingAverage(N)

def test_getAverage_and_addsample(N):
    module = moving_average.MovingAverage(N)

if __name__ == "__main__":
    print(timeit.repeat(stmt=test, setup=mysetup))
    """
    print(timeit.timeit(stmt="test_addsample_withoutSamples(100)"))
    print(timeit.timeit(stmt="test_addsample_withoutSamples(10000)"))
    print(timeit.timeit(stmt="test_addsample_withoutSamples(1000000)"))
    print("---------------------------------------------------------------------------------")
    print(timeit.timeit(stmt="test_addsample_withSamples(100)", setup = mysetup))
    print(timeit.timeit(stmt="test_addsample_withSamples(10000)", setup = mysetup2))
    print(timeit.timeit(stmt="test_addsample_withSamples(1000000)", setup = mysetup3))
    print("---------------------------------------------------------------------------------")
    print(timeit.timeit(stmt="test_getAverage(100)", setup = mysetup))
    print(timeit.timeit(stmt="test_getAverage(10000)", setup = mysetup2))
    print(timeit.timeit(stmt="test_getAverage(1000000)", setup = mysetup3))
    print("---------------------------------------------------------------------------------")
    print(timeit.timeit(stmt="test_getAverage_and_addsample(100)", setup = mysetup))
    print(timeit.timeit(stmt="test_getAverage_and_addsample(10000)", setup = mysetup2))
    print(timeit.timeit(stmt="test_getAverage_and_addsample(1000000)", setup = mysetup3))
    """
