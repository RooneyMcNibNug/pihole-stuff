import os
import dns.resolver

domain = 'marketo.com'
answers = dns.resolver.query(domain,'track','ad','stat','metric','click','analytic','js')
for server in answers:
    print(server.target)
