Packet Sniffer

Github Link: https://github.com/chandanrakholia/Packet-Sniffer
This packet sniffing tool is designed to intercept and analyze network traffic in real-time. It provides two main functionalities:

    Real-time Keyword Alert: Alerts the viewer whenever a packet containing a user-defined keyword is detected.
    Credential Collection: Collects user credentials (such as username, password, and cookies) from packets and stores them into a file.

Team Members

    Shubham Yadav (2021ucs0117)
    Chandan Rakholia (2021us0091)
    Aarav Jain (2021ucs0080)
    Lalak Yadav (2021ucs0100)

Contributions

    Shubham Yadav: tester and debugger.
    Chandan Rakholia: Keyword Search Functionality, developed a test html website to test the correcness of the code.
    Aarav Jain: Credential search functionality.
    Lalak Yadav: regex search functionality.

Dependencies

    Scapy: A powerful packet manipulation library for Python.

Install dependencies using:

pip install scapy


Steps to run the code
1. sudo -E /home/aarav/anaconda3/bin/python main.py
The following output is printed:
Choose one of the following:
      1. Alert on string matched
      2. Alert on Regex matched 
      3. Collect User credentials

2. Enter the choice:
For example if you write: 2 (regex input)
Enter the Regular expression to search for: (Aarav)+

Sniffing packets -------
Alert ----- PACKET FOUND!
Interface: lo
Source IP: 127.0.0.1
Destination IP: 127.0.0.1
Protocol: TCP
Source Port: 80
Destination Port: 58788