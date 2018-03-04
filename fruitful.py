import sys, traceback, telnetlib, time

def main():
    if len(sys.argv) < 4:
        print("Invalid Arguments, instead use: fruitful.py port command address1 adress2 ...")
        sys.exit()

    path_of_script = sys.argv[0]
    targetPort = sys.argv[1]
    commandToSend = sys.argv[2]

    ip_list = []
    for index in range(3, len(sys.argv)):
        ip_list.append(sys.argv[index])

    global tn

    tn = telnetlib.Telnet()

    def sendCommand(host_address, port, command):
        tn.open(str(host_address), int(port), 5)
        tn.write(command.encode("ascii")+b"\r\n")
        tn.close()

    for aHost in ip_list:
        try:
            sendCommand(aHost, targetPort, commandToSend)
        except:
            print("Exception sending: " + str(commandToSend) + " to: " + str(aHost) + ":" + str(targetPort))
            continue

if __name__=="__main__":
    print("main")
    main()
