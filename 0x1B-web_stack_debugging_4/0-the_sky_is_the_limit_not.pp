# configure nginx server to respond to huge number of requests

exec {'configure':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['reboot'],
}

exec {'reboot':
  provider => shell,
  command  => 'sudo service nginx restart',
}
