"""Print interface and ip where bote status and protocol are up using slice. need when fiels separator is not space

e.g UP....UP"""

#get
with open('ipv4_int_bri.txt') as fp:
    header = fp.readline() #Ignor header
    # Parse
    iface_start = header.find('Interface')
    ip_start = header.find('IP-Address')
    status_start = header.find('Status')
    proto_start = header.find('Protocol')

    for line in fp:
        iface = line[iface_start:ip_start].strip()
        ip = line[ip_start:status_start].strip()
        status = line[status_start:proto_start].strip()
        proto = line[proto_start:-1].strip()

        
        # Analyze
        # if status == 'Up' and proto == 'Up':
        if (status, proto) == ('Up', 'Up'):
            # Output
            print '%s %s' % (iface, ip)
