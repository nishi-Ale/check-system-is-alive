import configparser

inifile = configparser.ConfigParser()
alertfile = configparser.ConfigParser()


def read_initxt(target):
    # iniファイルを読み込む
    inifile.read('../../inputdata/ini.txt')
    target_folderpath = inifile[target]['TARGETFOLDERPATH']
    target_category = inifile[target]['TARGETFILECATEGORY']
    target_findstring = inifile[target]['TARGETFILENAME']
    target_namepattern = inifile[target]['TARGETNAMEPATTERN']

    return {'folderpath': target_folderpath,
            'category': target_category,
            'findstring': target_findstring,
            'namepattern': int(target_namepattern)}


def read_setting_for_alert(target_user):
    alertfile.read('../../inputdata/alert_settings.txt')
    from_addr = alertfile[target_user]['FROM_ADDRESS']
    passwd = alertfile[target_user]['MY_PASSWORD']
    bcc = alertfile[target_user]['BCC']
    to_addr = alertfile[target_user]['TO_ADDRESS']
    subject = alertfile[target_user]['SUBJECT']
    body = alertfile[target_user]['BODY']

    return {'from': from_addr,
            'pass': passwd,
            'to': to_addr,
            'bcc': bcc,
            'subject':  subject,
            'body': body
            }


def select_targetlocation():
    # iniファイルのセクションを読み込む
    inifile.read('../../inputdata/ini.txt', encoding='UTF-8')
    targetlocation = inifile.sections()
    return targetlocation


def select_targetuser():
    # iniファイルのセクションを読み込む
    alertfile.read('../../inputdata/alert_setting.txt', encoding='UTF-8')
    targetuser = alertfile.sections()

    return targetuser