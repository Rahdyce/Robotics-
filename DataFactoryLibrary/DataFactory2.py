class DataFactory2:
    def __init__(self):
        self.LeftIR = False
        self.RightIR = False
        self.ColorSensor = False
        self.RightDistance = 0
        self.FrontDistance = 0
        self.BackDistance = 0
    
    def interpret(self):
        return f"A - IL = {int(self.LeftIR)} - IR = {int(self.RightIR)} - FD = {self.FrontDistance} - RD = {self.RightDistance} - BD = {self.BackDistance} - CS = {int(self.ColorSensor)} -Z"
    
    def reader(self, data_type):
        if data_type == 0:
            return self.LeftIR
        elif data_type == 1:
            return self.RightIR
        elif data_type == 2:
            return self.FrontDistance
        elif data_type == 3:
            return self.RightDistance
        elif data_type == 4:
            return self.BackDistance
        elif data_type == 5:
            return self.ColorSensor
        else:
            raise ValueError("Invalid data type")
