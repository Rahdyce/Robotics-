import serial #this is for arduino serial and python to be able to communicate, make sure to pip install pyserial


class CommandFactory:
    def __init__(self):
        self.LMSpeed = 0
        self.RMSpeed = 0
        self.baseAngle = 0
        self.shoulderAngle = 0
        self.elbowAngle = 0
        self.wristAngle = 0
        self.swivelAngle = 0
        self.clawAngle = 0
        self.trayDoor = 0

    def interpret(self, input_str):
        parts = input_str.split('-')
        args = parts[1::2]
        vals = [part.split('=')[1] for part in parts[2::2]]

        # Assuming vals are ordered according to the initialization list
        self.LMSpeed = int(vals[0])
        self.RMSpeed = int(vals[1])
        self.baseAngle = int(vals[2])
        self.shoulderAngle = int(vals[3])
        self.elbowAngle = int(vals[4])
        self.wristAngle = int(vals[5])
        self.swivelAngle = int(vals[6])
        self.clawAngle = int(vals[7])
        self.trayDoor = int(vals[8])

    def reader(self, variable):
        variables = {
            "LMSpeed": self.LMSpeed,
            "RMSpeed": self.RMSpeed,
            "baseAngle": self.baseAngle,
            "shoulderAngle": self.shoulderAngle,
            "elbowAngle": self.elbowAngle,
            "wristAngle": self.wristAngle,
            "swivelAngle": self.swivelAngle,
            "clawAngle": self.clawAngle,
            "trayDoor": self.trayDoor,
        }
        return variables.get(variable, -1)

    def writer(self, variable, value):
        if hasattr(self, variable):
            setattr(self, variable, value)

    def command(self):
        command = f"A-L={self.LMSpeed}-R={self.RMSpeed}-B={self.baseAngle}-S={self.shoulderAngle}-E={self.elbowAngle}-W={self.wristAngle}-C={self.swivelAngle}-TD={self.trayDoor}-Z"
        return command
