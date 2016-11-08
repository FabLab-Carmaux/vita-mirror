import var

class Sensor():
    """This class is to get default sensors events (IR proximity, temp/humidity, luminosity/gesture)"""
    
    def __init__(self):
    
        self.temp=0
        self.humidity=0
    
        self.ir=0
    
        self.pr=[]
    
        self.gesture="none"
        
        #init adcs
        #TODO
        
    def is_someone(self):
        """
        is there some in front or vita ?
        
        get values from IR sensor
        if someone return True, else return False
        """
        if (self.ir>10):
            return True
        else:
            return False
        
    def get_temp(self):
        """
        get temperature from temp sensor
        return temp
        """
        return 20

    def get_humidity(self):
        """
        get humidity from humidity sensor
        return humidity in %
        """
        return 80        