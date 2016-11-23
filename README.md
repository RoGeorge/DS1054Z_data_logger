# DS1054Z_data_logger
'**DS1054Z_logger.py**' is a Python script that adds Vavg measurement for all the 4 channels of a Rigol DS1054Z oscilloscope, then periodically log the Vavg values in a PC file using a LAN connexion between computer and oscilloscope. No drivers are required to be installed on the PC.

<pre># Print usage
def print_help():
    print
    print "This program periodically reads the Vavg measured"
    print "    for all 4 channels of a Rigol DS1054Z oscilloscope."
    print
    print "    The reading time interval (in seconds) can be specified"
    print "    in the command line. A timestamp is added for each new reading."
    print
    print "    At each new reading, the Vavg values for each channel"
    print "    are listed in CSV format, then saved in a log file. The log file"
    print '    is saved as "MODEL_YYYY-MM-DD_HH.MM.SS.csv"'
    print
    print "The program is using LXI protocol, so the computer"
    print "    must have LAN connection with the DS1054Z instrument."
    print "    USB and/or GPIB connections are not used by this software."
    print
    print "    No VISA, IVI or Rigol drivers are needed."
    print
    print "Usage syntax:"
    print "    " + "python " + scriptName + " [read_interval [instrument_IP]]"
    print
    print "Usage examples:"
    print "    " + "python " + scriptName + "                   # log outputs (1s, 192.168.1.3)"
    print "    " + "python " + scriptName + " 60                # log at each minute (192.168.1.3)"
    print "    " + "python " + scriptName + " 3600 192.168.1.7  # log hourly from IP 192.168.1.7"
    print
    print "To end the logging, press 'ESC'."
    print
    print
    print
</pre>