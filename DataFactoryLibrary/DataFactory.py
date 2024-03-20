class DataFactory:
    def __init__(self):
        # Initialize all sensor states and readings to default values
        self.startingSignalColorSensorState = 0
        self.leftIRSensorState = 0
        self.rightIRSensorState = 0
        self.clawIRSensorState = 0
        self.frontLeftDistanceReading = 0
        self.frontRightDistanceReading = 0
        self.backLeftDistanceReading = 0
        self.backRightDistanceReading = 0
        self.leftSideLeftDistanceReading = 0
        self.leftSideRightDistanceReading = 0
        self.rightSideLeftDistanceReading = 0
        self.rightSideRightDistanceReading = 0
        self.runToggleState = 0

    def data(self):
        # Create and return the data string with current sensor states and readings
        dataString = "A-CS={}-IL={}-IR={}-IC={}-FL={}-FR={}-BL={}-BR={}LL={}LR={}RL={}RR={}-RT={}-Z".format(
            self.startingSignalColorSensorState,
            self.leftIRSensorState,
            self.rightIRSensorState,
            self.clawIRSensorState,
            self.frontLeftDistanceReading,
            self.frontRightDistanceReading,
            self.backLeftDistanceReading,
            self.backRightDistanceReading,
            self.leftSideLeftDistanceReading,
            self.leftSideRightDistanceReading,
            self.rightSideLeftDistanceReading,
            self.rightSideRightDistanceReading,
            self.runToggleState
        )
        return dataString

    def interpret(self, data):
        parts = data.split('-')
        for part in parts:
            key, value = part.split('=')
            # map key to class attributes and update their values
            if hasattr(self, key):
                setattr(self, key, int(value))

    def read(self, variable):
        # Return the value of the requested variable
        if hasattr(self, variable):
            return getattr(self, variable)
        return None

    def write(self, variable, value):
        # Write the value to the requested variable
        if hasattr(self, variable):
            setattr(self, variable, value)
            return value
        return None

