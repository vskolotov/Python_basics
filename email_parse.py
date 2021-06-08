import re


def email_parse(email):
    try:
        RE_EMAIL = re.compile(r'^\S.*@(\w*\.\w*)*$')
        assert RE_EMAIL.search(email)
    except AssertionError:
        raise ValueError(f'wrong email: {email}')
    else:
        dict_email = {}
        RE_USER = re.compile(r'^\S.*@')
        RE_DOMAIN = re.compile(r'@(\w*\.\w*)*$')
        username = RE_USER.search(email)
        domain = RE_DOMAIN.search(email)
        dict_email['username'] = username[0][:-1]
        dict_email['domain'] = domain[0][1:]
        return dict_email


print(email_parse('er456_464@6tsdrud.fert'))
