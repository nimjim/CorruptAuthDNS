import random
import dns.zone

def corrupt_response(response, zone):
    changed = {}  # {key: (before_value, after_value)}
    qname = str(response.question[0].name)

    # qname case randomization (dns-0x20) test
    # incorrect case pattern for qname in the response from the auth dns
    # Unbound -- use-caps-for-id: yes
    # Knot Resolver -- NO_0X20 = False
    # PowerDNS Recursor -- lowercase-outgoing = False
    if qname.lower().startswith('case_rand_test'):
        new_name = ''.join(random.choice((c.upper(), c.lower())) for c in qname)
        response.question[0].name = dns.name.from_text(new_name)
        response.answer[0].name = dns.name.from_text(new_name)
        changed['qname'] = (qname, new_name)
        return response, changed

    # secret response in additional section
    if qname.lower().startswith('open_sesame'):
        secret_name = dns.name.from_text('secret.' + str(zone.origin))
        secret_rrset = zone.get_rrset(secret_name, dns.rdatatype.A)
        print(secret_rrset)
        response.additional.append(secret_rrset)
        changed['additinal section'] = ("no answer", "secret answer")
        return response, changed

    # drop the query if directly queried for secret records
    if qname.lower().startswith('secret'):
        changed['response'] = ("answer normally", "drop query")
        return None, changed

    return response, changed
