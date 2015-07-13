"""Print interface and ip where bote status and protocol are up"""

#Get

with open('ipv4_int_bri.txt') as fp:
    fp.readline() # Ignore header
    for line in fp:
        # Parse
        iface, ip, status, proto = line.split()
        # Analyze
        if status == 'Up' and proto == 'Up':
            # Output
            print '%s %s' % (iface, ip)
