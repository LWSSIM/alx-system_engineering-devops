# WEB STACK DEBUGGING 4

0. Sky is the limit, let's bring that limit higher
mandatory
In this web stack debugging task, we are testing how well our web server setup featuring Nginx is doing under pressure and it turns out it’s not doing well: we are getting a huge amount of failed requests.

For the benchmarking, we are using ApacheBench which is a quite popular tool in the industry. It allows you to simulate HTTP requests to a web server. In this case, I will make 2000 requests to my server with 100 requests at a time. We can see that 943 requests failed, let’s fix our stack so that we get to 0, and remember that when something is going wrong, logs are your best friends!

Problem was found in nginx configuration at `/etc/default/nginx` where `ULIMIT` was too low!

- TIPs
```bash
# get user limits
ulimit -a

# Fire ApacheBench at the server
ab -c 100 -n 2000 localhost/

# Check what's wrong with nginx (To many open files)
cat /var/log/nginx/error.log

```

1. Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.

We changed the limit foe user holberton in `/etc/security/limits.conf` which was found to be 5,

- TIPs

```bash
# switch user
su - holberton

# get user limits
ulimit -a
```

```bash
# Solution was
root@1a1331ed882d:/etc/security# cat limits.conf
.
.
.
holberton hard nofile 2048 # was 5
holberton soft nofile 1024 # was 4
# End of file
root@1a1331ed882d:/etc/security# su - holberton
holberton@1a1331ed882d:~$ # no error
```

- > [!NOTE]
> Both solutions were implemented using puppet! Happy debugging;
