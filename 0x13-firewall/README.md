# Firewall Overview and ufw (Uncomplicated Firewall)

## Introduction to Firewalls

Firewalls are essential components of network security systems. They act as barriers between a secure internal network and untrusted external networks, such as the internet. The primary purpose of a firewall is to control incoming and outgoing network traffic based on predetermined security rules. By filtering traffic, firewalls help prevent unauthorized access to or from private networks and safeguard against various cyber threats.

### Types of Firewalls:

1. **Packet Filtering Firewalls**: Operate at the network layer (Layer 3) of the OSI model and examine each packet that enters or exits the network. They make decisions based on predefined rules.

2. **Stateful Inspection Firewalls**: Also known as dynamic packet filtering firewalls, these maintain a state table of active connections. They not only examine individual packets but also track the state of connections to make more intelligent filtering decisions.

3. **Proxy Firewalls**: Act as intermediaries between internal and external networks. They receive network requests on behalf of clients, forward them to the destination, and return the response to the client. This adds an extra layer of security as the actual network addresses are hidden.

4. **Next-Generation Firewalls (NGFW)**: Incorporate advanced features beyond traditional packet filtering and stateful inspection, such as intrusion detection and prevention systems (IDPS), application awareness, and deep packet inspection.

### Firewall Rule Components:

- **Source/Destination IP Address**: Specifies the IP address or range of addresses from which traffic originates or to which it is destined.
- **Source/Destination Port**: Defines the port number or range of ports associated with the source or destination service.
- **Protocol**: Indicates the network protocol (TCP, UDP, ICMP, etc.) used by the traffic.
- **Action**: Determines whether to allow or deny traffic matching the rule.
- **Logging**: Optional feature to log traffic matching the rule for analysis and auditing purposes.

## ufw (Uncomplicated Firewall)

ufw is a user-friendly command-line interface for managing iptables, the default firewall management tool for many Linux distributions. It simplifies the process of creating and managing firewall rules, making it accessible even to users without extensive networking knowledge.

### Installation:

ufw is often pre-installed on Ubuntu and other Debian-based systems. If not, it can be installed using the package manager:

```bash
sudo apt update
sudo apt install ufw
```

### Basic Usage:

1. **Enable ufw**:

```bash
sudo ufw enable
```

2. **Allowing/Denying Traffic**:

   - **Allow SSH** (port 22):

   ```bash
   sudo ufw allow ssh
   ```

   - **Allow HTTP** (port 80):

   ```bash
   sudo ufw allow http
   ```

   - **Deny FTP** (port 21):

   ```bash
   sudo ufw deny ftp
   ```

3. **Checking Status**:

```bash
sudo ufw status
```

### Advanced Configuration:

1. **Define Specific Rules**:

   ```bash
   sudo ufw allow from 192.168.1.0/24 to any port 3306
   ```

2. **Delete Rules**:

   ```bash
   sudo ufw delete allow ssh
   ```

3. **Logging**:

   ```bash
   sudo ufw logging on
   ```

### Example Rule Table:

| Rule # | From           | To       | Service | Action |
|--------|----------------|----------|---------|--------|
| 1      | 192.168.1.0/24 | Anywhere | 22/tcp  | Allow  |
| 2      | Anywhere       | Anywhere | 80/tcp  | Allow  |
| 3      | Anywhere       | Anywhere | 21/tcp  | Deny   |

## Request Forwarding using Firewalls

Firewalls can also be configured to forward requests from external networks to internal servers. This is commonly known as port forwarding or destination NAT (Network Address Translation). By forwarding requests, organizations can host services such as web servers, email servers, or VPN servers behind a firewall while still allowing external users to access them.

### Port Forwarding with ufw:

1. **Enable Port Forwarding**:

   Edit `/etc/default/ufw` and ensure `DEFAULT_FORWARD_POLICY` is set to `ACCEPT`:

   ```
   DEFAULT_FORWARD_POLICY="ACCEPT"
   ```

2. **Add Forwarding Rules**:

   ```bash
   sudo ufw route allow proto tcp from any to any port 80
   ```

   This example forwards HTTP traffic from any external IP address to an internal server listening on port 80.

3. **Enable NAT (Network Address Translation)**:

   ```bash
   sudo nano /etc/ufw/sysctl.conf
   ```

   Ensure the following lines are uncommented:

   ```
   net/ipv4/ip_forward=1
   ```

   Then reload the sysctl settings:

   ```bash
   sudo sysctl -p /etc/ufw/sysctl.conf
   ```

4. **Reload ufw**:

   ```bash
   sudo ufw reload
   ```

Now, incoming requests to port 80 will be forwarded to the internal server as configured. Ensure proper firewall rules are in place to restrict access as needed and prevent unauthorized access to internal services.


## Conclusion

Firewalls are critical components of network security, and ufw provides a simple yet powerful interface for managing firewall rules on Linux systems. Understanding firewall concepts and using tools like ufw effectively can significantly enhance the security posture of your network.
