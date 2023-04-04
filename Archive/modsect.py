from processLogs import ProcessLogs

def file_log_file(filename):
    # create an object for processing the file
    processor = ProcessLogs()
    # ingest the file
    with open(filename) as logFile:
        # read the first line so that line will not be None (null)
        line = logFile.readline()
        # run a loop to process the file untill there is 
        # no file to process
        while len(line) != 0:
            # pass the line read into the process method to process it
            processor.process(line)
            # read another line and try again
            line = logFile.readline()
        
        # processor.output();
            
        

if __name__ == '__main__':
    file_log_file('modsec_audit.log')