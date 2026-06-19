Lab 11: Multiple Taints
Task
Add two taints to one node.
Create:
Pod A (matches first taint)
Pod B (matches second taint)
Pod C (matches both)
Observe placement.
Deliverables

Provide:

Commands
YAML



control plane (learning-control-plane):;    Tainsts: node-role.kubernetes.io/control-plane:NoSchedule                  labels: node-role.kubernetes.io/control-plane=
Worker node1 (learning-worker) :            Taints:  node=worker1                                                      labels: env=uat , storage=hdd
Worker node 2 (learning-worker2):           Taints:  node=worker2                                                       labels: env=prod , storage=sdd



