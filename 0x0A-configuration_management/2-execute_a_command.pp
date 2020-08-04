# Execute a command with a puppet manifesto

exec { 'killmenow':
  path    => '/usr/bin/',
  command => 'pkill killmenow',
  returns => [0],
}
