# Example telegram bot with CI-CD on VPS

## Add to the repository secrets:
* `SSH_LOGIN` - username on VPS server
* `SSH_HOST` - VPS server IP
* `SSH_KEY` - privat ssh key for ssh connect on VPS
* `GHCR_TOKEN` - token for access github regestry
* `TELEGRAM_BOT_TOKEN` - token from botfather

## Setup VPS on Debian linux:

### 1. OS setup:
* connect to VPS `ssh root@vps_server_ip`
* `apt update && apt upgrade -y`
* `adduser my_cool_user`
* `usermod -aG sudo my_cool_user`

* add in `/etc/ssh/sshd_config`
	```
	AllowUsers my_cool_user my_cool_user_second
	PermitRootLogin no
	PasswordAuthentication yes
	```

* `service ssh restart`

* `ssh-copy-id my_cool_user@vps_server_ip`
* `ssh my_cool_user@vps_server_ip`

* add in `/etc/ssh/sshd_config`
	```
	PasswordAuthentication no
	```

* `sudo service ssh restart`


### 2. Firewall setup:
* `sudo apt install ufw`
* `sudo ufw allow OpenSSH`
* `sudo ufw enable`

### 3. Docker setup:
* Install docker https://docs.docker.com/engine/install/debian/
* `sudo usermod -aG docker my_cool_user `
	


## Setup for local development:		
* `make build` - for build dev container
* look in the Makefile
