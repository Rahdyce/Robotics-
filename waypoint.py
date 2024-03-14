true = True
false = False

class wayPoint:
    def __init__(self,  LMspeed, RMspeed, dt, leftD, rightD, backD, frontD, lineLeft, lineRight, camX, camY, keyNum):
        self.LMspeed = LMspeed
        self.RMspeed = RMspeed
        self.dt = dt
        self.leftD = leftD
        self.rightD = rightD
        self.backD = backD
        self.frontD = frontD
        self.lineLeft = lineLeft
        self.lineRight = lineRight
        self.camX =camX
        self.camY = camY
        self.keyNum = keyNum

    def getAll(self):
        return [self.LMspeed, self.RMspeed, self.dt, self.leftD, self.rightD, self.backD, self.frontD, self.lineLeft, self.lineRight, self.camX, self.camY, self.keyNum]

    def getDist(self, LD, RM):  #calculate the distance from where the robot is to the waypoint
