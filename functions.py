__author__ = 'RoGeorge'

import platform
import os
import telnetlib
import sys

# Constants for field index of the instrument answer at a *IDN? command
COMPANY = 0
MODEL = 1
SERIAL = 2


# Check network response (ping)
def ping_IP(instrument, IP):
    if platform.system() == "Windows":
        response = os.system("ping -n 1 " + IP + " > nul")
    else:
        response = os.system("ping -c 1 " + IP + " > /dev/null")

    if response != 0:
        print
        print "No response pinging " + IP
        print "Check network cables and settings."
        print "You should be able to ping the " + instrument + "."
        print


# Open a telnet session for Rigol instrument
def connect_to(instrument, IP, port):
    tn = telnetlib.Telnet(IP, port)
    # Ask for instrument ID
    tn.write("*IDN?\n")
    instrument_id = tn.read_until("\n", 1)

    id_fields = instrument_id.split(",")

    # Check if the instrument is set to accept LAN commands
    if id_fields[COMPANY] != "RIGOL TECHNOLOGIES":
        print instrument_id
        print "Non Rigol:,", instrument, "or the", instrument, "does not accept LAN commands."
        print "Check the", instrument, "settings."
        if instrument == "oscilloscope":
            print "Utility -> IO Setting -> RemoteIO -> LAN must be ON"
        if instrument == "power supply":
            print "Utility -> IO Config -> LAN -> LAN Status must be Configured"
        sys.exit("ERROR")

    return tn, id_fields


def connect_verify(instrument, IP, port):
    ping_IP(instrument, IP)
    tn, idFields = connect_to(instrument, IP, port)
    if instrument == "oscilloscope" and idFields[MODEL] != "DS1104Z" or \
                            instrument == "power supply" and idFields[MODEL] != "DP832":
        print idFields[MODEL], "is an unknown", instrument, "type."
        sys.exit("ERROR")
    return tn, idFields


def command(tn, SCPI):
    response = ""
    while response != "1\n":
        tn.write("*OPC?\n")  # operation(s) completed ?
        response = tn.read_until("\n", 1)  # wait max 1s for an answer

    tn.write(SCPI)


def init_oscilloscope(tn):
    # Channel 4 ON
    # BW Limit 20 MHz
    # 10 mV/div
    # POS 0

    # Trig Auto
    # Trig Edge
    # Trig CH4

    tn.write(":MEAS:ITEM VAVG, CHAN1\n")
    tn.write("*OPC?\n")  # operation(s) completed ?
    tn.read_until("\n", 1)  # wait max 1s for an answer

    tn.write(":MEAS:ITEM VAVG, CHAN2\n")
    tn.write("*OPC?\n")  # operation(s) completed ?
    tn.read_until("\n", 1)  # wait max 1s for an answer

    tn.write(":MEAS:ITEM VAVG, CHAN3\n")
    tn.write("*OPC?\n")  # operation(s) completed ?
    tn.read_until("\n", 1)  # wait max 1s for an answer

    tn.write(":MEAS:ITEM VAVG, CHAN4\n")
    tn.write("*OPC?\n")  # operation(s) completed ?
    tn.read_until("\n", 1)  # wait max 1s for an answer
