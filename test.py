#!/usr/bin/env python 

print("testing python import of flowd")

import flowd

flow_log = flowd.FlowLog("flows.log", "rb")
for flow in flow_log:
    print flow.format()
