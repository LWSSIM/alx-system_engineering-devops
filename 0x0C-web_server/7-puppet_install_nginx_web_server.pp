# Setup new ubuntu server with nginx with some config

exec { 'update system':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system']
}

file {'/var/www/html/index.html':
  content => 'Hello World!'
}

exec {'redirect_me':
  command  => 'sed -i  "/server_name _;/a \ \n\n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}" /etc/nginx/sites-available/default',
  provider => 'shell'
}

service {'nginx':
  ensure  => running,
  require => Package['nginx']
}
