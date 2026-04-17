# SDN Link Failure Recovery

## Description
Simulation of link failure recovery using Mininet and SDN controller.

## Features
- Redundant topology
- Link failure simulation
- Recovery testing

## Tools Used
- Mininet
- POX Controller
- Python

## Run Instructions

### Step 1: Start POX Controller
cd pox
./pox.py controller

### Step 2: Run Mininet Topology
sudo mn --custom topology.py --topo mytopo --controller remote

## Results
- Successful communication before failure
- Packet loss during failure
- Recovery after link restoration

  ## Demo Screenshots

### 1. Mininet Topology Design
![Topology](mininet_topology_design.jpeg)

### 2. Controller Implementation
![Controller 1](controller_implementaion_1.jpeg)
![Controller 2](controller_implementation_2.jpeg)

### 3. Flow Rule Management
![Flow Rules](flow_rule_management.jpeg)

### 4. Functionality (Normal Operation)
![Normal Test](normal_test.jpeg)

### 5. Link Failure
![Link Failure](link_failure.jpeg)

### 6. Recovery
![Recovery](recovery.jpeg)

### 7. Performance Evaluation (iperf)
![Performance](performance_evaluation.jpeg)
