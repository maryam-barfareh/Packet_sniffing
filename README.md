#  Python Packet Sniffer

A simple packet sniffer built with **Python** and **Scapy** that captures network traffic and displays:

- IP source and destination addresses
- TCP ports
- UDP ports

This project is for learning purposes and basic network traffic analysis.

---

##  Features

- Captures live packets from the network
- Detects IP layer
- Identifies TCP and UDP protocols
- Displays source & destination IP addresses
- Shows source & destination ports
- Real-time packet monitoring

---

##  Requirements

- Python 3.x
- Scapy

Install dependencies:
On Windows, install **Npcap** (required for sniffing).

---

## How to Run

Run with administrator/root privileges:

**Windows**
---

##  How It Works

The program listens to network traffic using Scapy's `sniff()` function.  
Each captured packet is processed to check:

1. If it has an IP layer
2. Whether it uses TCP or UDP
3. Extracts and prints IP addresses and ports

---

##  Disclaimer

This tool is for **educational purposes only**.  
Do not capture network traffic without permission.

---
