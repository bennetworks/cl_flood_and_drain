Flood and Drain
===========================
Disclaimer: I have no affiliation with Cumulus Linux.

Flood and Drain is a tool to gracefully andministatively remove a node from a routing topology. This is probably a little unnecesary, but exists to play with flowd and its respective Python API. Additionally, the reason behind this project was to get experience with Vagrant and Ansible to manage Cumulus instances on KVM/libvirt.

What does it do?
1. Ask which leaf router to decomission

2. Determine if networks advertised on router are actually passing the router using netflow

3. Determine if networks advertised on router are seen on another same tier device (i.e. another leaf node) due to ECMP (which is validated with netflow). Also, validate if flow transits other node bidirectionally.

4. Configure ospf max-metric (RFC3137, OSPF Stub Router Advertisement support) to encourage all traffic to take path around router if available

5. Verify that traffic for advertised prefixes has stopped with netflow

6. Notify the user that it is safe to perform maintentance on router

Topology
--------

```
     +------------+       +------------+
     | spine01    |       | spine02    |
     |            |       |            |
     +------------+       +------------+
     swp1 |    swp2 \   / swp1    | swp2
          |           X           |
    swp51 |   swp52 /   \ swp51   | swp52
     +------------+       +------------+
     | leaf01     |       | leaf02     |
     |            |       |            |
     +------------+       +------------+
     swp1 | .1                 .2 | swp2
          |     172.16.1.0/24     |
     eth1 |                       | eth2
     +------------+       +------------+
     | server01   |       | server02   |
     |172.16.1.101|       |172.16.1.101|
     +------------+       +------------+
```
Note: 172.16.1.101 used on both hosts for proof of concept

Before:
```
cumulus@spine01:~$ net show route ospf | grep 172.16.1.0 -A 1
O>* 172.16.1.0/24 [110/20] via 10.0.0.11, swp1 onlink, 00:02:07
  *                        via 10.0.0.12, swp2 onlink, 00:02:0
```

After: coming soon

