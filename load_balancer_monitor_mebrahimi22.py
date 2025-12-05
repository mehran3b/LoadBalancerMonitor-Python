# load_balancer_monitor.py
# Author: Mehran Ebrahimi

import subprocess


class Node:
    def __init__(self, ip):
        """Build a node with an IP address (string)."""
        self.ip = ip

    def canExist(self):
        """Check if the IP address is valid."""
        parts = self.ip.split(".")

        # must have exactly 4 octets
        if len(parts) != 4:
            return False

        octets = []

        # each octet must be a number between 0 and 254
        for p in parts:
            if not p.isdigit():
                return False

            value = int(p)

            if value < 0 or value >= 255:
                return False

            octets.append(value)

        # first octet cannot be 0
        if octets[0] == 0:
            return False

        # last octet cannot be 0
        if octets[3] == 0:
            return False

        return True

    def isRunning(self):
        """Ping the IP address; return True if it replies."""
        # -W 2 : wait max 2 seconds
        # -c 1 : send 1 packet
        cmd = f"ping -W 2 -c 1 {self.ip}"
        status, output = subprocess.getstatusoutput(cmd)
        return status == 0


class LoadBalancerMonitor:
    def __init__(self, networkAddress, bitmask, master):
        """Build a load balancer monitor."""
        self.networkAddress = networkAddress  # string
        self.bitmask = bitmask                # int
        self.master = master                  # Node object
        self.slaves = []                      # list of Node objects

    def addSlave(self, node):
        """Add a slave node if its IP can exist."""
        if node.canExist():
            self.slaves.append(node)
        else:
            print(f"Error: invalid IP address for slave: {node.ip}")

    def removeSlave(self, slave):
        """Remove a slave node if it is in the list."""
        if slave in self.slaves:
            self.slaves.remove(slave)

    def getStatus(self):
        """Print the status of master and slaves."""
        print("Checking", end="")

        # check master
        print(".", end="", flush=True)
        master_online = self.master.canExist() and self.master.isRunning()

        # check slaves
        online = 0
        offline = 0

        for slave in self.slaves:
            print(".", end="", flush=True)
            if slave.isRunning():
                online += 1
            else:
                offline += 1

        print()  # newline
        print()
        print("Load Balancer Status")
        print("====================")

        if master_online:
            print("Master: ONLINE")
        else:
            print("Master: OFFLINE")

        print(f"Slaves: {online} ONLINE, {offline} OFFLINE")


# You can use this block to test your code.
# It will NOT run when your file is imported by the marker.
if __name__ == "__main__":
    ip1 = Node("0.168.0.1")
    print(ip1.canExist())  # False

    ip1 = Node("192.168.0.0")
    print(ip1.canExist())  # False

    ip1 = Node("192.168.1")
    print(ip1.canExist())  # False

    ip1 = Node("192.268.0.1")
    print(ip1.canExist())  # False

    ip1 = Node("10.4.45.100")
    print(ip1.canExist())  # True
    print("ip1.ip is running: " + str(ip1.isRunning()))

    master = Node("1.1.1.1")  # For easy testing
    print(master.canExist())  # True
    print("master.ip is running: " + str(master.isRunning()))

    monitor = LoadBalancerMonitor("1.1.1.0", 24, master)

    slave = Node("127.0.0.0")
    monitor.addSlave(slave)  # invalid → prints error

    slave = Node("127.0.0.1")
    monitor.addSlave(slave)
    slave = Node("127.0.0.2")
    monitor.addSlave(slave)
    slave = Node("127.0.0.3")
    monitor.addSlave(slave)
    slave = Node("10.4.45.100")
    monitor.addSlave(slave)

    slave = Node("127.0.0.2")
    monitor.addSlave(slave)
    monitor.removeSlave(slave)

    monitor.getStatus()
