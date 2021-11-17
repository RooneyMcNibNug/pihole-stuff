import os

tail = 'timeout 43200 pihole -t > tail_queries.txt'
egrep = 'egrep -r "track|ad|collect|stat|discover|metric|social|counter|lead|traffic|click|event|script|analytic|campaign|visit|engage|intel|monitor|audience|user|target|js|pulse|feed|tag|market|record|pixel|canvas|report" tail_queries.txt > for_grav.txt'
grav = 'cat for_grav.txt >> /etc/pihole/gravity.list'
os.system(tail)
os.system(egrep)
os.system(grav)
