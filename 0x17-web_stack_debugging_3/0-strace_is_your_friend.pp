# Fix prefix in WordPress settings
exec { 'fix-prefix':
      command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
      provider => shell,
  }
