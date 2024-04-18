# nginx_config.pp

# Define the content of the /etc/default/nginx file
file { '/etc/default/nginx':
  ensure  => file,
}

# Set the ulimit in the /etc/default/nginx file
exec { 'ulimit increase':
  command  => "sed -i 's/^ULIMIT=.*/ULIMIT=\"n 10000\"/' /etc/default/nginx",
  provider => 'shell',
  require  => File['/etc/default/nginx'],  # Ensure the package is installed after the file is created
  notify   => Service['nginx'],  # Notify the NGINX service when the file changes
}

# Manage the NGINX service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/default/nginx'],  # Ensure the service restarts after the file changes
}
