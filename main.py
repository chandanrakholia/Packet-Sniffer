from scapy.all import sniff, TCP, Raw, IP, UDP, get_if_list
from keyword_search import regex_search, keyword_search
from user_credentials import get_all_user_credentials


def print_packet(packet):
    print("Alert ----- PACKET FOUND!")
    print("Interface:", packet.sniffed_on)
    print("Source IP:", packet[IP].src)
    print("Destination IP:", packet[IP].dst)

    if packet.haslayer(TCP):
        print("Protocol: TCP")
        print("Source Port:", packet[TCP].sport)
        print("Destination Port:", packet[TCP].dport)
    elif packet.haslayer(UDP):
        print("Protocol: UDP")
        print("Source Port:", packet[UDP].sport)
        print("Destination Port:", packet[UDP].dport)

    print("\n\n")



def execute(packet, data, check_packet):
    if packet.haslayer(Raw):
        if data != {} and check_packet(packet, data):
            print_packet(packet=packet)
        elif data == {}:
            check_packet(packet, data)


def main():
    print("""Choose one of the following:
      1. Alert on string matched
      2. Alert on Regex matched 
      3. Collect User credentials""")
    
    choice = input("Enter your choice: ")
    check_packet = 0
    data = {}

    if choice == "1":
        check_packet = keyword_search
        keyword_to_search = input("Enter the keyword: ")
        data["keyword"] = keyword_to_search
    elif choice == "2":
        check_packet = regex_search
        regex_to_search = input("Enter the Regular expression to search for: ")
        data["regex"] = regex_to_search
    elif choice == "3":
        check_packet = get_all_user_credentials
    print("Sniffing packets ------- \n")

    interfaces = get_if_list()
    sniff(prn=lambda packet: execute(packet, data, check_packet), iface=interfaces ,store=False)

if __name__ == "__main__":
    main()