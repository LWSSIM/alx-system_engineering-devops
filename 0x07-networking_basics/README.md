# README: Networking Fundamentals

## OSI Model
The OSI (Open Systems Interconnection) model is a conceptual framework that standardizes the functions of a telecommunication or computing system into seven abstraction layers. Each layer serves a specific purpose and interacts with the layers directly above and below it.

### What it is
The OSI model is a reference model that guides product developers and facilitates communication between different systems.

### How many layers it has
The OSI model consists of seven layers:
1. **Physical**
2. **Data Link**
3. **Network**
4. **Transport**
5. **Session**
6. **Presentation**
7. **Application**

### How it is organized
The layers are organized in a hierarchical order, with each layer relying on the functionality provided by the layer below it. This organization ensures modularity and ease of understanding.

### Example:
*Physical Layer*: The physical layer involves hardware devices like cables and connectors. An example is the Ethernet cable used to connect a computer to a local network.

*Transport Layer*: The transport layer ensures end-to-end communication. An example is the Transmission Control Protocol (TCP), providing reliable data transfer. 

## LAN (Local Area Network)
A Local Area Network is a network that is limited to a small geographic area, such as a single building or a campus.

### Typical usage
LANs are commonly used for connecting devices within a home, office, or organization, allowing for the sharing of resources like files, printers, and internet connections.

### Typical geographical size
LANs typically cover a small geographical area, ranging from a single room to a campus or a cluster of buildings.

### Example:
A home network with multiple devices connected to the same Wi-Fi router forms a LAN. Devices can share files, printers, and access the internet through this network.

## WAN (Wide Area Network)
A Wide Area Network spans a larger geographical area and connects multiple LANs.

### Typical usage
WANs are used to connect geographically dispersed LANs, enabling communication and resource-sharing over long distances. Examples include connecting branch offices of a company.

### Typical geographical size
WANs cover a wide geographical area, potentially spanning across cities, countries, or even continents.

### Example:
A multinational corporation may have a WAN connecting its headquarters in one country to branch offices in various other countries, facilitating seamless communication and resource-sharing.

## Internet
The Internet is a global network of interconnected computers and networks, providing a vast array of services and information.

### Example:
Accessing a website, sending emails, or streaming videos are common activities on the Internet.

## IP Address
An IP (Internet Protocol) address is a numerical label assigned to each device participating in a computer network. It serves two main functions: host or network interface identification and location addressing.

### Example:
If your computer's IP address is 192.168.1.1, other devices on the network can use this address to communicate with your computer.

## Types of IP Addresses
There are two types of IP addresses:
1. **IPv4 (Internet Protocol version 4)**
2. **IPv6 (Internet Protocol version 6)**

### Example:
IPv4 address: 192.168.0.1
IPv6 address: 2001:0db8:85a3:0000:0000:8a2e:0370:7334

## Localhost
Localhost refers to the loopback network interface, allowing a device to communicate with itself.

### Example:
When you type "localhost" into your web browser, it refers to your own computer, and you may see a locally hosted website.

## Subnet
A subnet is a logical subdivision of an IP network. It enables efficient utilization of IP addresses and improves network security.

### Example:
In a large organization, different departments might be assigned to different subnets to manage IP address allocation and improve network performance.

## Why IPv6 was created
IPv6 was created to address the exhaustion of IPv4 addresses, providing a vastly expanded address space to accommodate the growing number of devices connected to the Internet.

### Example:
As more devices connect to the Internet, the limited pool of IPv4 addresses becomes insufficient. IPv6, with its larger address space, ensures a sustainable solution for the future.

## TCP/UDP
TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are two transport layer protocols used for data transfer.

### Example:
When you browse a website, your browser may use TCP to ensure that all parts of the webpage are received correctly. On the other hand, video streaming often uses UDP to prioritize speed over reliability.

## Main Difference between TCP and UDP
TCP is connection-oriented, providing reliable, ordered, and error-checked delivery of data. UDP is connectionless and offers faster, but less reliable, data transfer.

### Example:
Sending an email attachment would use TCP to ensure all data is received intact, while a real-time video call might use UDP to minimize latency.

## Port
A port is a 16-bit number used to identify specific processes to which the data is directed on a host.

### Example:
When you access a website using a web browser, your computer uses port 80 for HTTP or port 443 for HTTPS.

## Port Numbers
- **SSH (Secure Shell):** 22
- **HTTP (Hypertext Transfer Protocol):** 80
- **HTTPS (Hypertext Transfer Protocol Secure):** 443

### Example:
When connecting to a remote server via SSH, you would use port 22.

## Tool/Protocol for Device Connectivity
Ping, based on the Internet Control Message Protocol (ICMP), is commonly used to check if a device is connected to a network.

### Example:
In a command prompt or terminal, typing `ping google.com` checks if your computer can communicate with Google's servers.

