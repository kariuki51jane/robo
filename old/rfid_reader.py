#!/opt/python3/bin/python3
import shlex
import subprocess
import sys
import time
###########################################################################################
#        Copyright 2014 (BSD License)
#   Credits:  Florian Otto(Solider) and hadara 
#   Contact me at: otti96@t-online.de
#   I can help you maybe to customize your code
#
###########################################################################################
#be sure to pu the file in the same directory as "rc522_reader" !!! If not, you can edit in line 79
#path to keydatabase in format: [...SERIAL...];NAME
#filename=/root/db.txt








class RFIDReaderWrapper(object):
    """runs rfid reader as a subprocess & parses tag serials
    from its output
    """
    def __init__(self, cmd):
        self._cmd_list = shlex.split(cmd)
        self._subprocess = None
        self._init_subprocess()

    def _init_subprocess(self):
        self._subprocess = subprocess.Popen(self._cmd_list,
            stderr=subprocess.PIPE)

    def read_tag_serial(self):
        """blocks until new tag is read
        returns serial of the tag once the read happens
        """
        if not self._subprocess:
            self._init_subprocess()

        while 1:
            line = self._subprocess.stderr.readline()
            if isinstance(line, bytes):
                # python3 compat
                line = line.decode("utf-8")

            if line == '':
                # EOF
                return None

            if not line.startswith("New tag"):
                continue

            serial = line.split()[-1].split("=", 1)[1]
            return serial
    
def get_serialmap(filename):
    """read serial -> name mappings from the given file
    and return them as a dictionary.
    file is assumed to look like:
    [2f75b800]; Peter Pan
    """
    serials = {}
    with open(filename, "r") as fd:
        # lets build serial -> name mapping
        for line in fd.readlines():
            serial, name = line.strip().split(";", 1)
            # XXX: we strip [ ] from the serial
            serials[serial] = name
            #[1:-1]
    return serials


try:
    if __name__ == '__main__':
        reader = RFIDReaderWrapper("./rc522_reader -d")
        while 1:
            fobj = open(filename,"r+")
            serial = reader.read_tag_serial()
            # blink the lights etc.
            #print(serial)
            serialmap = get_serialmap(filename)p
            if serial in serialmap:
                print("Card identified!")
                print("Name:",serialmap[serial],"| Card ID:",serial)
            else:
                print("Not identified! Card ID:",serial)	
            fobj.close()
except KeyboardInterrupt:
    print("EXIT!")
    sys.exit(0)		
