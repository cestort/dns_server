# dns_server

DNS server using dnsmasq and creating an interface with flask

The usage is thought to run into a virtual machine. dnsmasq works in Linux, so a ubuntu machine could be
the best idea.

Once the virtual machine is running, to install dnsmasq use those commands:

1.-To upgrade your so:

sudo apt-get update
sudo apt-get upgrade

2.-Installing dnsmasq:

sudo apt-get install dnsmasq

Configurar Permisos para Reiniciar dnsmasq

sudo visudo

('yourusername' should be your username for the ubuntu system)

yourusername ALL=NOPASSWD: /usr/bin/systemctl restart dnsmasq

3.- Configure dnsmasq and the host file taht is going to be updated by flask and read by dnsmasq:

3.1 open the config file:

sudo nano /etc/dnsmasq.conf

3.2 The file is empty. Pasta in the file the following configuration:

# Don't use the system DNS server

no-resolv

# DNS server used to resolve upstream matchings[cloudflare, google]

server=1.1.1.1
server=8.8.8.8

# Habilitar el DNS de hosts locales

listen-address=127.0.0.1
listen-address=192.168.1.1 # Your LAN IP

# Our file created to the local DNS resolution

addn-hosts=/etc/dnsmasq.hosts
