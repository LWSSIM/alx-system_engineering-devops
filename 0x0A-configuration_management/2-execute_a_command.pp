# Kills a process named killmenow, using exec+pkill
exec { 'kill_killmenow':
  command     => '/usr/bin/pkill killmenow',
}
