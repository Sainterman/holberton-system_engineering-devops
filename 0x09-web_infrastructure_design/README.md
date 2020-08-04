# 0x09. Web infrastructure design

## Resources:books:
Read or watch:

* [Protocolos](https://searchnetworking.techtarget.com/definition/protocol)
* [What is a IP?](https://computer.howstuffworks.com/internet/basics/what-is-an-ip-address.htm)
* [What is TCP/IP?](https://searchnetworking.techtarget.com/definition/TCP-IP)
* [What is an Internet Protocol (IP) port?](https://www.lifewire.com/port-numbers-on-computer-networks-817939)
* [What is a server](https://en.wikipedia.org/wiki/Server_(computing)#Hardware_requirement)
* [What is a Server.](https://www.youtube.com/watch?v=B1ANfsDyjeA)
* [Data center](https://www.youtube.com/watch?v=iuqXFC_qIvA&feature=youtu.be&t=33)
* [Do not mix up server and web server.](https://en.wikipedia.org/wiki/Web_server)
* [webserver](https://whatis.techtarget.com/definition/Web-server)
* [what is web server?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_web_server)
* [DNS](https://howdns.works/ep1/)
* [main DNS record types](https://kb.pressable.com/article/dns-record-types-explained/)
* [A](https://support.dnsimple.com/articles/a-record/)
* [CNAME record](https://en.wikipedia.org/wiki/CNAME_record)
* [MX record](https://en.wikipedia.org/wiki/MX_record)
* [TXT record](https://en.wikipedia.org/wiki/TXT_record)
* [DNS Knowledge](https://www.dnsknowledge.com/whatis/round-robin-dns/)
* [NS Record](https://support.dnsimple.com/articles/ns-record/)
* [SOA Record](https://support.dnsimple.com/articles/soa-record/)
* [The root domain and sub domain - differences](https://intranet.hbtn.io/concepts/12)
* [The www prefix always leads to the main domain](https://intranet.hbtn.io/rltoken/WmJ_HTaBD1RZVfY6IJFBSA)
* [Load balancer](https://intranet.hbtn.io/concepts/46)
* [load balancing](https://www.youtube.com/watch?v=xJ7BKnZbwCU)
* [Load balancer intro](https://www.thegeekstuff.com/2016/01/load-balancer-intro/)
* [Load balancing Algorithms](https://devcentral.f5.com/s/articles/intro-to-load-balancing-for-developers-ndash-the-algorithms)
* [Monitoring](https://intranet.hbtn.io/concepts/13)
* [Database](https://searchsqlserver.techtarget.com/definition/database)
* [Whats the difference between Web and App Server?](https://www.youtube.com/watch?v=S97eKyv2b9M)
* [Single point of failure](https://en.wikipedia.org/wiki/Single_point_of_failure)
* [How to avoid downtime when deploying new code](https://softwareengineering.stackexchange.com/questions/35063/how-do-you-update-your-production-codebase-database-schema-without-causing-downt#answers-header)
* [High availability cluster (active-active/active-passive)](https://docs.oracle.com/cd/E17904_01/core.1111/e10106/intro.htm#ASHIA712)
* [HTTPS](https://www.instantssl.com/http-vs-https)
* [Firewall](https://www.webopedia.com/TERM/F/firewall.html)

* [Network basics](https://intranet.hbtn.io/rltoken/Sn9ZSSHjyEW5aRfKvNiZCg)
* [Server](https://intranet.hbtn.io/rltoken/83joH7-HzuV9gBNe16iTrA)
* [Web server](https://intranet.hbtn.io/rltoken/7moqhXcFOXP6zNMWdsjWjQ)
* [DNS](https://intranet.hbtn.io/rltoken/G0a1v98rwb2RHA8VHxo36A)
* [Load balancer](https://intranet.hbtn.io/rltoken/H6TVgGaqt13JhXKzJ2rVAA)
* [Monitoring](https://intranet.hbtn.io/rltoken/JY6524JCvX9dREoNgnQUFw)
* [What is a database](https://intranet.hbtn.io/rltoken/XLIOfzfuaxPQu39VQ0TLtw)
* [Whats the difference between a web server and an app server?](https://intranet.hbtn.io/rltoken/Nb8B47Y2D8SLqQMOKVoQyQ)
* [DNS record types](https://intranet.hbtn.io/rltoken/pSGVxlKznxONwGEHIXLSwA)
* [Single point of failure](https://intranet.hbtn.io/rltoken/wYpewVpIp9PSqqL27RPafg)
* [How to avoid downtime when deploying new code](https://intranet.hbtn.io/rltoken/Mlvynt0OgLQXrxjrC5Wlnw)
* [High availability cluster (active-active/active-passive)](https://intranet.hbtn.io/rltoken/POX3jE0S6TChQHSYQraYeQ)
* [What is HTTPS](https://intranet.hbtn.io/rltoken/N4BwU4wYDNW02kdzMiekFw)
* [What is a firewall](https://intranet.hbtn.io/rltoken/HrYI70d_nxUPZeufjUYzIw)
---
## Learning Objectives:bulb:
What did I learn from this project:

* You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects
* You must be able to explain what each component is doing
* You must be able to explain system redundancy
* Know all the mentioned acronyms: LAMP, SPOF, QPS

---

### [0. Simple web stack](./0-simple_web_stack)
* A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a LAMP stack.

#### Requirements:
* You must use:
- 1 server
- 1 web server (Nginx)
- 1 application server
- 1 application files (your code base)
- 1 database (MySQL)
- 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8
* You must be able to explain some specifics about this infrastructure:
* What is a server
* *What is the role of the domain name
* What type of DNS record www is in www.foobar.com
* What is the role of the web server
* What is the role of the application server
* What is the role of the database
* What is the server using to communicate with the computer of the user requesting the website
* You must be able to explain what the issues are with this infrastructure:
- SPOF
- Downtime when maintenance needed (like deploying new code web server needs to be restarted)
- Cannot scale if too much incoming traffic

### [1. Distributed web infrastructure](./1-distributed_web_infrastructure)
* On a whiteboard, design a three server web infrastructure that hosts the website www.foobar.com.

#### Requirements:
* You must add:
- 2 servers
- 1 web server (Nginx)
- 1 application server
- 1 load-balancer (HAproxy)
- 1 set of application files (your code base)
- 1 database (MySQL)
* You must be able to explain some specifics about this infrastructure:
* For every additional element, why you are adding it
* What distribution algorithm your load balancer is configured with and how it works
* Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
* How a database Primary-Replica (Master-Slave) cluster works
* What is the difference between the Primary node and the Replica node in regard to the application
* You must be able to explain what the issues are with this infrastructure:
- Where are SPOF
- Security issues (no firewall, no HTTPS)
- No monitoring

### [2. Secured and monitored web infrastructure](./2-secured_and_monitored_web_infrastructure)
* On a whiteboard, design a three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.

#### Requirements:
* You must add:
- 3 firewalls
- 1 SSL certificate to serve www.foobar.com over HTTPS
- 3 monitoring clients (data collector for Sumologic or other monitoring services)
* You must be able to explain some specifics about this infrastructure:
* For every additional element, why you are adding it
* What are firewalls for
* Why is the traffic served over HTTPS
* What monitoring is used for
* How the monitoring tool is collecting data
* Explain what to do if you want to monitor your web server QPS
* You must be able to explain what the issues are with this infrastructure:
* Why terminating SSL at the load balancer level is an issue
* Why having only one MySQL server capable of accepting writes is an issue
* Why having servers with all the same components (database, web server and application server) might be a problem


### [3. Scale up](./3-scale_up)

#### Requirements:
* You must add:
- 1 server
- 1 load-balancer (HAproxy) configured as cluster with the other one
* Split components (web server, application server, database) with their own server
* You must be able to explain some specifics about this infrastructure:
- For every additional element, why you are adding it

---
