import awpy
from awpy import Demo
from awpy.stats import *


global_demo = None


def parse_demo(demo):
    dem = Demo('test.dem')
    dem.parse()
    return dem


def demo_adr(demo):
    dem = parse_demo(demo)
    return adr(dem)    


print(demo_adr('test.dem'))
