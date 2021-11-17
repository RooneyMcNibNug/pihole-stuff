import os

tail = 'sudo timeout 500 tshark -i wlan0 -f "src port 53" -n -T fields -e dns.qry.name > tail_queries.txt'
egrep = 'egrep -r "track|ad|collect|stat|discover|metric|social|counter|lead|traffic|click|event|script|analytic|campaign|visit|engage|intel|monitor|audience|user|target|js|pulse|feed|tag|market|record|pixel|canvas|report" tail_queries.txt > for_grav.txt'
grav = 'cat for_grav.txt >> /etc/pihole/gravity.list'

os.system(tail)
os.system(egrep)
os.system(grav)
