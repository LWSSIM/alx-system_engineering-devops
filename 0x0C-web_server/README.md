# Web Server Creation and Configuration Guide

![image](https://github.com/LWSSIM/alx-system_engineering-devops/assets/127129101/16ba32b4-c121-4db7-84ba-63532b3f7d4b)

## Introduction
Welcome to the Web Server Creation and Configuration guide! This guide aims to provide a comprehensive walkthrough for setting up and configuring a web server using Ubuntu 16.04 and Nginx. Whether you're new to server management or looking to enhance your skills, this guide will equip you with the knowledge needed to get started and understand the inner workings of a web server.

## Table of Contents
1. Prerequisites
2. Installation of Ubuntu 16.04
3. Installation of Nginx
4. Configuration of Nginx
5. Managing Web Server
6. FAQs

## 1. Prerequisites
Before diving into web server setup and configuration, ensure you have the following prerequisites:
- Basic familiarity with the Linux command-line interface.
- Understanding of fundamental server concepts and networking.
- Access to a machine or virtual environment with Ubuntu 16.04 installed.

## 2. Installation of Ubuntu 16.04
Ubuntu 16.04 LTS (Long Term Support) is a popular Linux distribution known for its stability and support. Follow these steps to install Ubuntu 16.04:
- Download the Ubuntu 16.04 ISO image from the official Ubuntu website.
- Create a bootable USB drive or DVD from the downloaded ISO.
- Boot your machine from the bootable media and follow the on-screen instructions to install Ubuntu.

## 3. Installation of Nginx
Nginx is a powerful and lightweight web server known for its high performance and scalability. Here's how to install Nginx on Ubuntu 16.04:
- Open a terminal window.
- Update the package index to ensure you install the latest versions of software:
  ```bash
  sudo apt update
  ```
- Install Nginx using the following command:
  ```bash
  sudo apt install nginx
  ```
  This command will download and install Nginx along with any required dependencies.

## 4. Configuration of Nginx
Nginx's configuration files are located in the `/etc/nginx` directory. The main configuration file is `nginx.conf`, which includes other configuration files from the `conf.d` directory and virtual host configurations from the `sites-available` directory.

To configure a website in Nginx, follow these steps:
- Navigate to the `/etc/nginx/sites-available` directory.
- Create a new configuration file for your website, e.g., `example.com.conf`.
- Edit the configuration file using a text editor like `nano` or `vim`. Define the server block with directives such as `server_name`, `root`, and `location`.
- Here's an example configuration for a basic website:
  ```nginx
  server {
      listen 80;
      server_name example.com;

      root /var/www/example.com/html;
      index index.html;

      location / {
          try_files $uri $uri/ =404;
      }
  }
  ```
  This configuration listens on port 80, sets the server name to `example.com`, defines the root directory for the website files, and specifies the default `index.html` file.

- Once the configuration is saved, create a symbolic link to enable the site:
  ```bash
  sudo ln -s /etc/nginx/sites-available/example.com.conf /etc/nginx/sites-enabled/
  ```

## 5. Managing Web Server
After configuring Nginx, you can manage the web server using systemd commands. Here are some common commands:
- Start Nginx:
  ```bash
  sudo systemctl start nginx
  ```
- Stop Nginx:
  ```bash
  sudo systemctl stop nginx
  ```
- Restart Nginx:
  ```bash
  sudo systemctl restart nginx
  ```
- Check Nginx status:
  ```bash
  sudo systemctl status nginx
  ```

## 6. FAQs

### What is the main role of a web server?
A web server's primary role is to handle client requests and serve web pages or other resources in response to those requests.

### What is a child process?
A child process is a process spawned by another process, known as the parent process. In the context of web servers like Nginx, child processes handle incoming client requests.

### Why do web servers usually have a parent process and child processes?
Web servers typically employ a parent-child process model for scalability and performance. The parent process manages core functionalities, such as configuration reloads and error handling, while multiple child processes handle incoming client requests concurrently.

### What are the main HTTP requests?
HTTP requests include methods such as GET, POST, PUT, DELETE, HEAD, OPTIONS, and PATCH. These methods define the action to be performed on a resource identified by a URL.

### What does DNS stand for?
DNS stands for Domain Name System.

### What is DNS's main role?
The Domain Name System (DNS) serves as the internet's address book, translating human-readable domain names (e.g., example.com) into IP addresses (e.g., 192.0.2.1) that computers use to communicate with each other.

### DNS Record Types
- **A (Address) Record**: Maps a domain name to an IPv4 address.
- **CNAME (Canonical Name) Record**: Alias of one domain name to another.
- **TXT (Text) Record**: Holds arbitrary text data, often used for verification purposes.
- **MX (Mail Exchange) Record**: Specifies the mail server responsible for accepting email messages on behalf of a domain.

Feel free to explore further and experiment with different configurations to suit your needs. Happy learning!
