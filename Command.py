class Command:

    def __init__(self, az, el):
        self.az = az
        self.el = el
    def __repr__(self):
        return "w " + "%.2f" % self.az + " " +"%.2f" % self.el