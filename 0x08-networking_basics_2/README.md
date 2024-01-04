# Networking README

## Table of Contents
- [localhost/127.0.0.1](#localhost127001)
- [0.0.0.0](#0000)
- [Hosts File and /etc/hosts](#hosts-file-and-etchosts)
- [Netcat (nc)](#netcat-nc)
- [Displaying Machine's Active Network Interfaces](#displaying-machines-active-network-interfaces)
- [Commands](#commands)
  - [ifconfig](#ifconfig)
  - [telnet](#telnet)
  - [nc (Netcat)](#nc-netcat)
  - [cut](#cut)

---

## localhost/127.0.0.1
`localhost` or `127.0.0.1` refers to the loopback address on a computer. It is used to test network connectivity on the local machine without the need for an external network. Any data sent to this address is routed back to the same device, allowing applications to communicate with themselves.

**Example:**
```bash
ping localhost
```

## 0.0.0.0
`0.0.0.0` typically represents an invalid or unknown address. In the context of networking, it can have different meanings. In some cases, it can mean "any address" or "all available interfaces." For example, binding a server to `0.0.0.0` means it will listen on all available network interfaces.

**Example:**
```bash
python -m http.server 8000 --bind 0.0.0.0
```

## Hosts File and /etc/hosts
The hosts file (`/etc/hosts` on Unix-based systems) is a plain text file that maps IP addresses to hostnames. It is used to override DNS or to specify local hostnames for IP addresses. This file is consulted before querying DNS servers.

**Example:**
```bash
sudo vim /etc/hosts
```

## Netcat (nc)
Netcat (`nc`) is a versatile networking tool used for reading from and writing to network connections. It can be used for port scanning, file transfers, and as a network debugging tool. Netcat operates on the command line and is available on most Unix-like operating systems.

**Example:**
```bash
# Listen on a specific port
nc -l -p 1234

# Connect to a server
nc localhost 1234
```

## Displaying Machine's Active Network Interfaces
To display active network interfaces on your machine, you can use the following command:

**Example:**
```bash
ifconfig
```

## Commands

### ifconfig
`ifconfig` (interface configuration) is a command-line utility used to configure and display information about network interfaces on Unix-like systems.

**Example:**
```bash
ifconfig eth0
```

### telnet
`telnet` is a network protocol used to establish a connection to a remote system, typically for text-based communication. It can be used for testing network services or troubleshooting.

**Example:**
```bash
telnet example.com 80
```

### nc (Netcat)
`nc` (Netcat) is a powerful networking tool that can be used for a variety of purposes, including reading and writing data across network connections.

**Example:**
```bash
# Listen on a specific port
nc -l -p 1234

# Connect to a server
nc localhost 1234
```

### cut
`cut` is a command-line utility for cutting parts of a text file or stream. It is often used for processing delimited text files.

**Example:**
```bash
echo "John,Doe,25" | cut -d ',' -f 2
```

In this example, `cut` is used to extract the second field (surname) from a comma-delimited text.
---------------------------------------------------------------
---------------------------------------------------------------

### TASK_100-port_listening_on_localhost

<p><strong>Terminal 0</strong></p>

<p>Starting my script.</p>

<pre><code>user@ubuntu$ sudo ./100-port_listening_on_localhost
</code></pre>

<p><strong>Terminal 1</strong></p>

<p>Connecting to <code>localhost</code> on port <code>98</code> using <code>telnet</code> and typing some text.</p>

<pre><code>user@ubuntu$ telnet localhost 98
Trying 127.0.0.2...
Connected to localhost.
Escape character is &#39;^]&#39;.
Hello world
test
</code></pre>

<p><strong>Terminal 0</strong></p>

<p>Receiving the text on the other side.</p>

<pre><code>user@ubuntu$ sudo ./100-port_listening_on_localhost
Hello world
test
</code></pre>

<p>For the sake of the exercise, this connection is made entirely within <code>localhost</code>. This isn&rsquo;t really exciting as is, but we can use this script across networks as well. Try running it between your local PC and your remote server for fun!</p>

<p>This can come in very handy in a multitude of situations. Maybe you&rsquo;re debugging socket connection issues, or you&rsquo;re trying to connect to a software and you are unsure if the issue is the software or the network, or you&rsquo;re working on firewall rules&hellip; Another tool to add to your debugging toolbox!</p>
