from scapy.all import IP, TCP, UDP, sniff *

# ---------------------------------
# ---------------------------------
def packet_callback(packet):

     
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst

        
        if TCP in packet:
            protocol = 'TCP'
            sport = packet[TCP].sport
            dport = packet[TCP].dport

            print(f"[TCP] {ip_src}:{sport}  →  {ip_dst}:{dport}")

      
        elif UDP in packet:
            protocol = 'UDP'
            sport = packet[UDP].sport
            dport = packet[UDP].dport

            


# ---------------------------------

# ---------------------------------
print(f"[*] {protocol} packet, {ip_src}, {sport} --> {ip_dst}, {dport}")

sniff(prn=packet_callback, store=0)
