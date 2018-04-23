import libvirt
import sys
import os

conn = libvirt.open("test:///opt/libvirt-python/tests/config.xml")

print('Version: '+str(conn.getLibVersion()))

(cpus, cpu_map, online) = conn.getCPUMap()
for cpu in range(cpus):
  print cpu

print conn.getType()
print conn.getHostname()
print conn.getInfo()
print conn.nodeDeviceLookupByName("computer")
print conn.listDevices("pci", 0)


dom = conn.lookupByUUIDString('c7a5fdbd-edaf-9455-926a-d65c16db1809')
print dom

nodeinfo = conn.getInfo()

print('Model: '+str(nodeinfo[0]))
print('Memory size: '+str(nodeinfo[1])+'MB')
print('Number of CPUs: '+str(nodeinfo[2]))
print('MHz of CPUs: '+str(nodeinfo[3]))
print('Number of NUMA nodes: '+str(nodeinfo[4]))
print('Number of CPU sockets: '+str(nodeinfo[5]))
print('Number of CPU cores per socket: '+str(nodeinfo[6]))
print('Number of CPU threads per core: '+str(nodeinfo[7]))

# discover all the virtual networks
networks = conn.listNetworks()
print('Virtual networks:')
for network in networks:
    print('  '+network)
print()

# lookup the default network by name
network = conn.networkLookupByName('default')
print('Virtual network default:')
print('  name: '+network.name())
uuid = network.UUIDString()
print('  UUID: '+uuid)
print('  bridge: '+network.bridgeName())
print()


domain = conn.lookupByID(1)
xmldesc = domain.XMLDesc(0)

print xmldesc
