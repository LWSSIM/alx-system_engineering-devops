# Define SSH configuration file path
$ssh_config_file = '/etc/ssh/ssh_config'

# Define the SSH host and user
$host = '54.237.2.143'
$user = 'ubuntu'

# Define the path to the private key file
$key_file = '~/.ssh/school'

# Add SSH configuration
file { $ssh_config_file:
  ensure  => present,
  content => "
Host ${host}
  HostName ${host}
  User ${user}
  IdentityFile ${key_file}
  PasswordAuthentication no
",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}
