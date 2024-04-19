# installing flask from pip3

exec { 'install_flask':
command => 'pip3 flask=2.1.0',
path => '/usr/bin/pip3'
}
