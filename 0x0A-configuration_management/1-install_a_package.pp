# Installs Flask version-2.1.0 from pip3
package { 'flask':
  ensure          => '2.1.0',
  provider        => 'pip3',
  install_options => ['--upgrade'],
  require         => Package['python3-pip'],  # Ensure pip3 is installed first
  unless          => 'pip3 show flask | grep -q "Werkzeug (2.1.1)"',  # Check if already installed
  before          => Package['werkzeug'],  # Ensure Flask is installed before Werkzeug
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['flask'],  # Ensure Flask is installed first
}
