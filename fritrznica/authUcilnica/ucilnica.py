# pip install requests
import re
import requests

UCILNICA_LOGIN_URL = 'https://ucilnica.fri.uni-lj.si/login/index.php'
UCILNICA_EDIT_URL = 'https://ucilnica.fri.uni-lj.si/user/edit.php'
UCILNICA_LOGGEDIN_URL = 'https://ucilnica.fri.uni-lj.si/'
valid = False
def ucilnica_login(username, password):
    """Check login for FRI ucilnica
 
    Usage:
 
    from ucilnica import ucilnica_login
 
    user_info = ucilnica_login(username, password)
 
    if user_info:
        name = user_info['name']
    """
    #usage in neki.py
    try:
        resp = requests.post(UCILNICA_LOGIN_URL, dict(username=username, password=password), verify=False, allow_redirects = False)
        cookies = dict(MoodleSession = resp.cookies['MoodleSession'])
        resp = requests.get(UCILNICA_EDIT_URL,cookies=cookies, verify=False)
        if resp.url == UCILNICA_EDIT_URL:
            match = re.search('<a href="https://ucilnica.fri.uni-lj.si/user/profile.php\?id=(\d+)">(.*?)</a>', resp.content) #id, ime priimek
            anothermatch = re.search('value="(.*?)" id="id_idnumber"',resp.content)

            if match:
                ucilnica_id = int(match.group(1))
                name = match.group(2).decode('utf8')
                vpisna_st = anothermatch.group(1)
                valid = True

                return {
                    'ucilnica_id': ucilnica_id,
                    'name': name,
                    'vpisna_st': vpisna_st,
                    'valid': valid
                }
                #not really sure if this is important ->
            if not match:
                valid = False
                return {
                'valid': valid
                }
        if not resp.url == UCILNICA_EDIT_URL:
            valid = False
            return {
                'valid': valid
            }
            #dont know why errors in pycharm
    except Exception, e:
        print 'Ucilnica login error: ', e