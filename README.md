# cl_flood_and_drain

1. Ask which leaf router to decomission 

2. Determine if networks advertised on router are passing device using netflow
    a. If yes, continue
    b. If no, abort 

3. Determine if networks advertised on router are seen on another same tier device (i.e. another leaf) due to ECMP (validate with netflow). Validate if flow transits other router bidirectionally.

4. Configure ospf max-metric (RFC3137, OSPF Stub Router Advertisement support) to encourage all traffic to take path around router if available

5. Verify that traffic for advertised prefixes has stopped with netflow

6. Notify the user that it is safe to perform maintentance on  router

