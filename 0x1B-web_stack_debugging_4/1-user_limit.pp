# Set nofile for holberton to 10000

exec { 'user-limit':
     command => 'sed -i s/holberton/#holberton/ /etc/security/limits.conf',
     path    => '/bin/:/usr/bin/',
}
