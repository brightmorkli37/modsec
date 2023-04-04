from detection import Detection
class ProcessLogs:
    # initial variables for our program
    detections = []
    sec = ''
    dec = None
    # this is what process the line we read
    def process(self, str):
        # this section detect the markers eg: ---zuqM0xLz---A--
        if str[0:3] == '---' and str[:2] == '--':
            # we split the marker to remove the - 
            # and create an array with it
            marker = str.split("-")
            self.sec = marker[6]
            # we check if the marker is a Start marker (A)
            if marker[6] == 'A':
                if not self.dec:
                    # if this is not the first time we are 
                    # this program store the dections that has already
                    # been found
                    self.detections.append(self.dec)
                # create a new dection object for holding the data
                self.dec = Detection(marker[3])
        else:
            self.dec.add_data(str, self.sec)
            
    def output(self):
        print(self.detections)