from awpy import Demo

demo = None

def parse_demo(demo_path):
    global demo 
    dem = Demo(demo_path)
    dem.parse()
    demo = dem


