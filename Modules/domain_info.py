import whois
def domain_info(target):
    w = whois.whois(target)
    return w
print(domain_info("wp.pl"))