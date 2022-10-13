---
toc: true
layout: post
description: This is a post that has the notes for the Collegeboard videos on the Internet
categories: [markdown, Week 8]
title: Collegeboard Internet Notes
---

### Computer Systems and Network Diagram:


### Computer Networks and Systems
- A computing device is a physical artifact that can run a program.
    - Computers
    - Tablets
    - Servers
    - Routers
    - Smart sensors
- A computer network is a type of computing system
- A path between two computing devices on a computer network (a sender and a reciever) is a sequence of directly connected computing devices that begins at the sender and ends at the receiver.
- Routing is the process of finding a path from sender to receiver.
- The bandwidth of a computer network is the maximum amount of data that can be sent in a fixed amount of time.
- Bandwidth is usually measured in bits per second.

---

### How Computers Are Connected
- A computing system is a group of computing devices and programs working together for a common purpose.
- A computer network is a group of interconnected computing devices capable of sending or receiving data.

---

### Packets
- A packet is a small amount of data sent over a network. Each packet also includes the source and the destination information.
- Packet Switching:
    - The message (file) is broken up into packets and sent in any order. The packets are reassembled by the recipient's device. Ex:
        - Hello. How are you? ==>
        - Hello.    You?     How are


---

### The Internet
- The Internet is a computer network consisting of interconnected networks that use standardized, open (nonpropritary) communication protocols.
- Access to the Internet depends on the ability to connact a computing dvice to an internet connected device.
- Routing on the Internet is usually dynamic; it is not specified in advance
- Information is passed through the Internet as a data stream. Data streams contain chunks of data, which are encapsulated in packets
- Packets contain a chunk of data and metadata used for routing the packet between the origin and the destination on the Internet, as well as for data reassembly
- Packets may arrive at the destination in order, our of order, or not at all
- The World Wide Web is a system of linked pages, programs, and files
- The World Wide Web uses the Internet

---

### Protocols
- A protocol is an agreed-upon set of rules that specify the behavior of a system.
- The protocols used in the Internet are open, which allows users to easily connect additional computing devices to the Internet.
- IP, TCP, and UDP are common protocols used on the Internet
    - TCP does error checking and error recovery so it is slower
    - UDP performs error checking, but it discards erroneous packets
- HTTP is a protocol used by the World Wide Web

---

### Internet and Transport Layers
- Transport Layer - How the packets are sent, and for what
    - Reliability - reliable - sender gets a receipt back, resend as needed
    TCP
    - Unreliability - send and forget.
    UDP
- Internet Layer
    - IPv4: Example 192.168.24.1
    32 bits, separated into 4 "octets"
    8 bits long (0-255)
    - Separated into 2 parts:
        - Network (1-31)
        - Device (32-network bits)
- Three targets that can be addressed using IP
    - Unicast - A specific device. Internet wide access. TCP is used.
    - Multicast - A group of devices. It is specific range of IP addresses. Internet-wide access. UDP is used.
    - Broadcast - All devices. LAN-wide. Data stops at the router. UDP is used.

---

### Application Layer
- Key protocols used:
    - http. How to ask and receive data from web servers. Normally uses TCP, Port 80 at the transport layer
    - https. Like http but with security. Usually uses TCP Port 443
- Web Servers:
    - Programs running on machines connected to the Internet
    - Provides clients web pages - data linked to other pages using URLs (Uniform Resource Locations)
    - Ex, https://www.mycompany.com
    - The World Wide Web (WWW) is this network of linked data and programs, running over the Internet
- DNS - Domain Name Service
    - Applications that translate a human readable URL (e.g. www.mycompany.com) to an IP address
    - DNS holds a database of mapping of names to IPs. Servers running DNS are spread across the internet
    - There are large computers serving and managing these name/IP Mappings for each Domain (.com, .net, .gov, etc.)
    - You use a DNS server every time you ask for a web page on a browser



---

### Scalibility of the Internet
- The scalability of a system is the capacity for the system to change in size and scale to meet new demands.
- The Internet was designed to be scalable
    - Able to change in size and scale to meet new demands
- Local Area Network (LAN):
    - Physical Connections
    - Limited by hardware and physics
    - 1 to 100s of systems
- Intranet:
    - LANs connected by Routers within an organization
- Autonomous Systems (AS):
    - Large intranets linked together under the control and policies of major organizations. Large routers link networks with large telecommunications connections
- The Internet:
    - Autonomous Systems linked together
    - Large Routers linking Ass via special telecom means (Fiber, T3, Satellites)
    - Major infrastructures - DNS (.com, .net, etc.), Cyber Operations

---

### Authentication
- Authentication measures protect devices and information from unauthorized access. Ex:
    - Strong passwords 
    - Multifactor authentication.
- A strong passwrod is something that is easy for a user to remember, but would be difficult for someone else to guess based on knowledge of that user.
- Multifactor authentication is a method of computer access control in which a user is only granted access after successfully presenting several separate pieces of evidence to an authentication mechanism, typically in at least two of the following categories: 
    - knowledge (something they know)
    - possession (something they have)
    - ingerence (something they are)
- Multifactor authentication requires a least two steps to unlock protected information; each step adds a new layer of security that must be broken to gain unauthorized access.

---

### Encryption
- Encryption: the process of encoding data to prevent unauthorized access
- Decryption: the process of decoding the data. 
- Two common encryption approaches are:
    - Symmetric key encryption involves one key for both encryption and decryption
    - Public key encryption pairs a public key for encryption and a private key for decryption.
        - The sender does not need the receiver's private key to encrypt a message, but the receiver's private key is required to decrypt the message
- Certificate authorities issue digital certificates that validates the ownership of encryption keys used in secure communications and are based on a trust model.

---

### Viruses and Malware
- Computer virus and malware scanning software can help protect a computing system against infection.
- A computer virus is a malicious program that can copy itself and gain access to a computer in an unauthorized way. Computer viruses often attach themselves to legitimate programs and start running independently on a computer.
- Malware is software intended to damage a computing system or to take partial control over its operation.
    - Can infiltrate a system by posing as legitimate programs or by attachign itself to legitimate programs, like an email attachment
- Virus scans can help to prevent malicious code from getting into and affecting your system


---

### Prevention
- All real-world systems have errors or design flaws that can be exploited to compromise them. Regular software updates help fix errors that could compromise a computing system.
- Users can control the permissions programs they have for collecting user information. Users should review the permission settings of programs to protect their privacy.

---

### Quiz Results
![]({{ site.baseurl }}/images/Fastpages-collegeboard-internet.png)