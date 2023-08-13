#fixes apache returning a 500 error

exec { 'Fix Apache':
    command => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
    provider => shell,
}
