# Web infrastructure design

### **On the abstarctions of networking and web-design!**


# Networking Basics

## Introduction
This section provides a fundamental understanding of networking concepts.

### Networking Definition
Networking involves the connection of computers and other devices to share resources and information.

### Key Terminology
- **IP Address**: A numerical label assigned to each device participating in a computer network.
- **Router**: A device that forwards data packets between computer networks.
- **Switch**: A network device that connects devices within the same local network.
- **Gateway**: A node on a network that serves as an entry or exit point to another network.

## Articles and Resources
- [Computer Networking Basics](https://www.geeksforgeeks.org/basics-computer-networking/)

---

# Server

## Introduction
This section covers the basic concepts related to servers in a networked environment.

### Server Definition
A server is a computer program or device that provides functionality to other programs or devices, known as clients.

### Types of Servers
- **Web Server**: Hosts web applications and serves web pages.
- **File Server**: Manages access to files on a network.
- **Database Server**: Stores and retrieves database information.
- **Application Server**: Runs application software.

## Articles and Resources
- [Understanding Servers](https://www.geeksforgeeks.org/what-is-server/)

---

# Web Server

## Introduction
A web server is a software application responsible for handling HTTP requests and serving web pages.

### Key Features
- **HTTP**: Hypertext Transfer Protocol, the foundation of data communication on the World Wide Web.
- **Static vs. Dynamic Content**: Serving pre-existing content vs. generating content on-the-fly.

### Example (Using Node.js)
```javascript
const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello, World!\n');
});

server.listen(3000, 'localhost', () => {
  console.log('Server listening on port 3000');
});
```

## Articles and Resources
- [How Do Web Servers Work?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_web_server)

---

# DNS

## Introduction
Domain Name System (DNS) translates human-readable domain names into IP addresses.

### Key Components
- **DNS Server**: Resolves domain names to IP addresses.
- **DNS Record**: Contains information about a domain.

### Common DNS Record Types
- **A Record**: Maps a domain to an IPv4 address.
- **CNAME Record**: Alias of one domain to another.
- **MX Record**: Specifies mail servers for the domain.

## Articles and Resources
- [Introduction to DNS](https://www.geeksforgeeks.org/details-on-dns/)

---

# Load Balancer

## Introduction
A load balancer distributes incoming network traffic across multiple servers to ensure no single server is overwhelmed.

### Key Features
- **Server Health Monitoring**: Checks server status to route traffic to healthy servers.
- **Session Persistence**: Ensures a user's requests always go to the same server.

### Example (Using Nginx)
```nginx
http {
  upstream backend {
    server backend1.example.com;
    server backend2.example.com;
  }

  server {
    location / {
      proxy_pass http://backend;
    }
  }
}
```

## Articles and Resources
- [Introduction to Load Balancing](https://www.nginx.com/resources/glossary/load-balancing/)

---

# Monitoring

## Introduction
Monitoring involves observing and checking the performance of a system to ensure it operates correctly.

### Key Metrics
- **CPU Usage**: Percentage of CPU being utilized.
- **Memory Usage**: Amount of RAM in use.
- **Network Traffic**: Data transfer rates.

## Articles and Resources
- [Introduction to System Monitoring](https://www.oreilly.com/library/view/effective-monitoring-and/9781449333515/ch01.html)

---

# What Is a Database

## Introduction
A database is an organized collection of data, typically stored and accessed electronically.

### Types of Databases
- **Relational Databases**: Use tables to organize data.
- **NoSQL Databases**: Store and retrieve data without using the traditional table-based relational database structure.

## Articles and Resources
- [Database Basics](https://www.geeksforgeeks.org/basic-database-concepts/)

---

# Web Server vs. App Server

## Introduction
Web servers handle HTTP requests and responses, while app servers execute application code.

### Key Differences
- **Responsibilities**: Web servers handle static content, while app servers manage dynamic content and application logic.

## Articles and Resources
- [Understanding the Difference Between Web Server and Application Server](https://www.infoworld.com/article/2077354/app-server-web-server-what-s-the-difference.html)

---

# DNS Record Types

## Introduction
DNS records contain information about a domain and its associated services.

### Common DNS Record Types
- **A Record**: Maps a domain to an IPv4 address.
- **CNAME Record**: Alias of one domain to another.
- **MX Record**: Specifies mail servers for the domain.

## Articles and Resources
- [DNS Records Explained](https://www.site24x7.com/learn/dns-record-types.html)

---

# Single Point of Failure

## Introduction
A single point of failure is a component whose failure can cause an entire system to fail.

### Mitigation Strategies
- **Redundancy**: Duplicate critical components.
- **Load Balancing**: Distribute traffic across multiple servers.

## Articles and Resources
- [Understanding Single Points of Failure](https://avinetworks.com/glossary/single-point-of-failure/)

---

# Avoiding Downtime When Deploying New Code

## Introduction
Avoiding downtime during code deployment is crucial for maintaining service availability.

### Strategies
- **Blue-Green Deployment**: Shift traffic between two identical environments.
- **Rolling Deployment**: Gradual update of instances without downtime.

## Articles and Resources
- [Zero-Downtime Deployment Strategies](https://www.pingidentity.com/en/resources/blog/post/what-is-zero-downtime-deployment.html)

---

# High Availability Cluster

## Introduction
A high availability cluster ensures system availability through redundancy and failover mechanisms.

### Types
- **Active-Active**: Both nodes actively handle requests.
- **Active-Passive**: One node handles requests, while the other remains on standby.

## Articles and Resources
- [Introduction to High Availability Clusters](https://docs.oracle.com/cd/E17904_01/core.1111/e10106/intro.htm#ASHIA713)

---

# What Is HTTPS

## Introduction
HTTPS (Hypertext Transfer Protocol Secure) is the secure version of HTTP.

### Key Features
- **Encryption**: Secure transmission of data.
- **Authentication**: Ensures the identity of the website.

## Articles and Resources
- [HTTPS Explained](https://www.instantssl.com/http-vs-https)

---

# What Is a Firewall

## Introduction
A firewall is a network security device that monitors and controls incoming and outgoing network traffic.

### Types
- **Packet Filtering**: Examines packets and allows or denies based on pre-defined rules.
- **Proxy Firewall**: Acts as an intermediary between client and server.

## Articles and Resources
- [Understanding Firewalls](https://www.webopedia.com/definitions/firewall/)

---

# Tasks-Description

## 0-simple_web_stack:

---

**1. User Wants to Access www.foobar.com:**

When a user wants to access www.foobar.com, their browser sends a request to the specified domain. The request is resolved to an IP address (in this case, 8.8.8.8) through DNS (Domain Name System) resolution.

**2. Infrastructure Components:**

- **Server (1):** A physical or virtual machine responsible for hosting the entire web infrastructure.

- **Web Server (Nginx):** Acts as a reverse proxy and handles incoming HTTP requests. It forwards requests to the application server.

- **Application Server:** Runs the application code and processes dynamic content. It communicates with the web server to handle user requests.

- **Application Files:** The code base of the web application resides on the server and is executed by the application server.

- **Database (MySQL):** Stores and manages data required by the web application.

- **Domain Name (foobar.com):** Serves as a human-readable alias for the server's IP address (8.8.8.8). The www subdomain is used to specify the web service.

**3. Specifics:**

- **Server:** A computer or system that hosts resources and services accessible over a network.

- **Domain Name:** An easy-to-remember alias for an IP address, making it user-friendly. DNS translates domain names into IP addresses.

- **www DNS Record:** It is a subdomain record indicating the web service for the domain (www.foobar.com). It points to the IP address of the server.

- **Web Server:** Manages HTTP requests, serves static content, and forwards dynamic requests to the application server.

- **Application Server:** Executes application code, processes dynamic requests, and communicates with the database to retrieve or store data.

- **Database:** Stores and manages the structured data required by the web application.

- **Communication:** The server communicates with the user's computer using the HTTP/HTTPS protocols. The web server handles the communication for static content, and the applicationserver manages dynamic content.

**4. Issues:**

- **Single Point of Failure (SPOF):** The entire infrastructure relies on a single server. If it fails, the entire system becomes unavailable. To address this, consider redundancy, load balancing, or a failover mechanism.

- **Downtime during Maintenance:** Deploying new code or performing maintenance may require restarting the web server, resulting in downtime. To minimize this, implement rolling updates, canary releases, or use redundant servers.

- **Scalability Issues:** If incoming traffic exceeds the capacity of the single server, the system cannot scale. To address this, consider load balancing, horizontal scaling (adding more servers), and optimizing database performance.

---

## 1-disbuted_web_infrastructure

**1. Three-Server Web Infrastructure for www.foobar.com:**

- **Servers (3):** Three physical or virtual machines to distribute the load and provide redundancy.

- **Web Server (Nginx):** Handles incoming HTTP requests, forwards dynamic requests to the application server.

- **Application Server:** Executes application code, processes dynamic requests.

- **Load Balancer (HAProxy):** Distributes incoming requests across multiple servers to ensure load balancing and high availability.

- **Application Files:** The code base of the web application resides on each server, ensuring redundancy and load distribution.

- **Database (MySQL):** Stores and manages the structured data required by the web application.

**2. Specifics:**

- **Additional Elements:**
- **Two Servers:** Introducing redundancy and scalability.
- **Load Balancer (HAProxy):** Distributes incoming requests, ensures high availability, and prevents a single point of failure.

- **Load Balancer Algorithm:** Configured with a Round Robin distribution algorithm. It works by sequentially routing requests to the servers in a circular order. This helps distribute the load evenly among the servers.

- **Active-Active vs. Active-Passive Setup:**
- **Active-Active:** Both servers are actively serving requests simultaneously. In this setup, the load balancer distributes incoming traffic across all active servers.
- **Active-Passive:** One server is actively serving requests, while the others are on standby. If the active server fails, the load balancer redirects traffic to the passive server. This setup provides redundancy but may result in underutilized resources.

- **Database Primary-Replica (Master-Slave) Cluster:**
- The Primary node (Master) accepts write operations and updates the database.
- The Replica nodes (Slaves) replicate data from the Primary node and serve read operations.
- This setup provides data redundancy, load balancing, and high availability.

- **Difference between Primary and Replica in the Application:**
- **Primary Node:** Handles write operations, ensuring data consistency.
- **Replica Node:** Serves read operations, distributing the read load and enhancing overall performance.

**3. Issues:**

- **Single Points of Failure (SPOF):**
- Load Balancer: If the load balancer fails, the entire system may be affected. Consider implementing redundancy or failover mechanisms.
- Database: If the Primary node fails, the system might experience downtime. Implement measures such as automatic failover or clustering for improved reliability.

- **Security Issues:**
- No Firewall: Lack of a firewall exposes the servers and database to potential security threats. Implement a firewall to control incoming and outgoing traffic.
- No HTTPS: Without HTTPS, data transmission is insecure. Integrate SSL/TLS certificates to encrypt data in transit.

- **No Monitoring:**
- Lack of monitoring makes it challenging to identify and address performance issues, security breaches, or hardware failures. Implement monitoring tools to ensure proactive management and rapid response to issues.

---

## 2-secured_and_monitored_web_infrastructure


**1. Three-Server Secured and Monitored Web Infrastructure for www.foobar.com:**

- **Servers (3):** Three physical or virtual machines to distribute the load and provide redundancy.

- **Firewalls (3):** Implementing firewalls for added security to control incoming and outgoing traffic.

- **SSL Certificate:** To encrypt traffic and ensure secure communication between the user's browser and the server.

- **Monitoring Clients (Sumologic or other):** Deployed on each server to collect and send data to a monitoring service, ensuring proactive management.

**2. Specifics:**

- **Additional Elements:**
- **Firewalls:** Add an additional layer of security by filtering and monitoring network traffic based on predetermined security rules.
- **SSL Certificate:** Encrypts data transmitted between the user's browser and the server, ensuring privacy and preventing data interception.
- **Monitoring Clients:** Used for tracking performance, identifying issues, and ensuring the health and availability of the infrastructure.

- **Firewalls:**
- **Purpose:** Firewalls are added to control and monitor incoming and outgoing network traffic. They act as a barrier between the servers and potential threats, enhancing security.

- **Traffic Served over HTTPS:**
- **Purpose:** HTTPS encrypts data during transit, preventing eavesdropping and ensuring the confidentiality and integrity of user data.

- **Monitoring:**
- **Purpose:** Monitoring is essential for proactive management of the infrastructure. It helps identify performance bottlenecks, security breaches, and hardware failures before they impact the system.

- **Monitoring Data Collection:**
- **Method:** Monitoring clients (Sumologic or other tools) collect data such as server performance metrics, error logs, and other relevant information. This data is sent to a central monitoring service for analysis.

- **Monitoring Web Server QPS:**
- **Procedure:** To monitor Web Server Queries Per Second (QPS), set up monitoring tools to track the number of incoming requests per second. Analyze this data to identify patterns, spikes, or anomalies in web traffic.

**3. Issues:**

- **Terminating SSL at Load Balancer Level:**
- **Issue:** Terminating SSL at the load balancer level may expose decrypted data between the load balancer and the servers. For end-to-end encryption, SSL termination should occur at the application servers.

- **Single MySQL Server Accepting Writes:**
- **Issue:** Having only one MySQL server capable of accepting writes creates a single point of failure. Implement a Primary-Replica (Master-Slave) cluster to distribute the write load and enhance reliability.

- **Identical Components in Servers (Database, Web Server, Application Server):**
- **Problem:** If all servers have the same components, a failure in one component (e.g., web server) might affect all servers simultaneously. Introduce diversity in components or distribute them across different servers to minimize the risk of a single failure impacting the entire infrastructure.

---
This Readme offers some good reads for each topic, make sure to check the included links for more info.
Happy coding!
