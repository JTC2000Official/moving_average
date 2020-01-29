import timeit
import_module = '''
import moving_average
m = moving_average
for i in range(1000000):
    m.addSample(i)
'''

testcode = '''
def test():
    return m.addSample(5)
'''
print(timeit.timeit(stmt=testcode, setup=import_module))


