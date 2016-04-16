class Command:

    def __init__(self, az, el):
        self.az = az
        self.el = el
    def __repr__(self):
        return "w " + "%.03d" % self.az + " " +"%.03d" % self.el