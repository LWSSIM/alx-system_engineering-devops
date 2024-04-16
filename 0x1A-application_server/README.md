# Flask Web App Deployment with Gunicorn

- **This project's goal is to deploy a Flask web application [AirBnB_clone] using Gunicorn on a Linux server, running Nginx web-server. Thus implementing a web application that can be accessed over the internet.**

This README.md provides a step-by-step guide to deploying a Flask web application using Gunicorn on a Linux server. We'll cover all aspects of the deployment process, including setting up the server, installing dependencies, configuring Gunicorn, and managing the deployment.

## Prerequisites

Before starting the deployment process, ensure that you have the following:

- A Linux server (e.g., Ubuntu) with SSH access
- A Flask web application ready for deployment
- Basic knowledge of Linux command line

## Step 1: Setting up the Server

1. **Connect to the Server**: Use SSH to connect to your Linux server:
    ```bash
    ssh username@server_ip
    ```

2. **Update System Packages**: Update the package list and upgrade installed packages:
    ```bash
    sudo apt update
    sudo apt upgrade
    ```

## Step 2: Installing Dependencies

1. **Install Python**: If Python is not already installed, install it using the package manager:
    ```bash
    sudo apt install python3
    ```

2. **Install Virtual Environment**: Install `virtualenv` to create isolated Python environments for your project:
    ```bash
    sudo apt install python3-venv
    ```

## Step 3: Setting up the Flask Application

1. **Clone the Repository**: Clone your Flask web application repository to the server:
    ```bash
    git clone <repository_url>
    ```

2. **Create a Virtual Environment**: Navigate to the project directory and create a virtual environment:
    ```bash
    cd <project_directory>
    python3 -m venv venv
    ```

3. **Activate the Virtual Environment**: Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

4. **Install Flask and Dependencies**: Install Flask and any other dependencies required by your application:
    ```bash
    pip install flask <other_dependencies>
    ```

## Step 4: Configuring Gunicorn

1. **Install Gunicorn**: Install Gunicorn using pip:
    ```bash
    pip install gunicorn
    ```

2. **Test Gunicorn**: Test Gunicorn to ensure it's installed correctly:
    ```bash
    gunicorn --version
    ```

3. **Create Gunicorn Configuration File**: Create a Gunicorn configuration file (`gunicorn_config.py`) in the project directory:
    ```python
    bind = '0.0.0.0:8000'
    workers = 3
    ```

## Step 5: Running the Flask App with Gunicorn

1. **Run Gunicorn**: Start the Flask application with Gunicorn using the configuration file:
    ```bash
    gunicorn -c gunicorn_config.py <your_app_module>:<app_instance>
    ```

2. **Test the Deployment**: Open a web browser and navigate to `http://<server_ip>:8000` to verify that the Flask application is running correctly.

## Step 6: Setting up Reverse Proxy (Optional)

If you want to serve your Flask application through a web server like Nginx, set up a reverse proxy. Install Nginx using the package manager and configure it to proxy requests to Gunicorn.

## Step 7: Managing the Deployment

1. **Monitoring**: Use monitoring tools like Datadog or Prometheus to monitor the performance of your deployed Flask application and server.

2. **Logging**: Set up logging to capture application logs and server logs for debugging and troubleshooting purposes.

3. **Backup**: Regularly backup your application files, databases, and configuration to prevent data loss.

4. **Security**: Implement security best practices such as firewall configuration, HTTPS encryption, and regular security updates.

## Useful Bashing

Here are some commonly used Linux commands for debugging, networking, and managing Gunicorn:

1. **netstat**: Display network connections, routing tables, and interface statistics.
   ```bash
   netstat -tuln
   ```

2. **ss**: Show socket statistics.
   ```bash
   ss -tuln
   ```

3. **lsof**: List open files, including network connections.
   ```bash
   sudo lsof -i :<port_number>
   ```

4. **ps**: Display information about running processes.
   ```bash
   ps aux | grep <process_name>
   ```

5. **top**: Display dynamic real-time information about running processes.
   ```bash
   top
   ```

6. **kill**: Terminate a process by its PID (process ID).
   ```bash
   kill <PID>
   ```

7. **journalctl**: Query the systemd journal.
   ```bash
   journalctl -u <service_name>
   ```

8. **systemctl**: Command to manage system services using systemd.
   ```bash
   sudo systemctl start <service_name>
   ```

These commands should help you debug network issues, monitor processes, and manage the Gunicorn server effectively.

## Conclusion

Congratulations! You have successfully deployed your Flask web application using Gunicorn on a Linux server. You can now access your application over the internet and manage it effectively using the provided deployment guide.
