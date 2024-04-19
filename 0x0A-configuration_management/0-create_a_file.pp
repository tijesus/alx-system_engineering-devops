# Create a file in /tmp.

file { '/tmp/school':
  ensure  => 'file',        # Ensures that the file exists
  mode    => '0744',        # Sets file permission to 0744
  owner   => 'www-data',    # Sets file owner to www-data
  group   => 'www-data',    # Sets file group to www-data
  content => 'I love Puppet',  # Sets the content of the file
}
