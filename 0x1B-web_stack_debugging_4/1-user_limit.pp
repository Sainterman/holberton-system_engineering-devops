# Set for holberton
exec { 'user-limit':
  command => 'sed -i s/holberton/#holberton/ /etc/security/limits.conf',
  path    => '/bin/:/usr/bin/',
}
