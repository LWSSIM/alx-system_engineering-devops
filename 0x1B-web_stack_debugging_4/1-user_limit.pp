# Change user limit for open files

exec { 'hard_nofile':
    command  => "sed -i 's/\\(^holberton hard nofile \\)[0-9]\\+/\\12048/' /etc/security/limits.conf",
    provider => 'shell',
}

exec { 'soft_nofile':
    command  => "sed -i 's/\\(^holberton soft nofile \\)[0-9]\\+/\\11048/' /etc/security/limits.conf",
    provider => 'shell',
}

