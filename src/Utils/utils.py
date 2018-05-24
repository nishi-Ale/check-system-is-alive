from datetime import datetime as dt
import os

LOGFILENAME = '../../log.txt'
ALERTSETTING = '../../inputdata/alert_setting.txt'
INI = '../../inputdata/ini.txt'


def generate_input_files():
    alert_items = ['[Location1] \n', 'FROM_ADDRESS = \n', 'MY_PASSWORD = \n', 'TO_ADDRESS = \n', 'BCC = \n','SUBJECT = \n','BODY =']
    ini_items = ['[User] \n', 'TARGETFOLDERPATH = \n', 'TARGETFILECATEGORY = \n', 'TARGETFILENAME = \n', 'TARGETNAMEPATTERN =']

    if not os.path.isfile(ALERTSETTING) or not os.path.isfile(INI):
        if not os.path.isfile(ALERTSETTING):
            for alert in alert_items:
                alertfile = open(ALERTSETTING,'a')
                alertfile.write(alert)

        if not os.path.isfile(INI):
            for ini in ini_items:
                alertfile = open(INI,'a')
                alertfile.write(ini)
        print('初期設定ファイルが作成されました。')
        print('プログラムを終了しました。')
        import sys
        sys.exit()


def write_log(target, status):
    header = ['date', 'location', 'status\n']
    strings = [dt.now().strftime('%Y/%m/%d %H:%M'), target, str(status) + '\n']
    # LOG出力処理
    if not os.path.isfile(LOGFILENAME):
        logfile = open(LOGFILENAME, 'a')
        logfile.write(','.join(header))
        logfile.write(','.join(strings))
    else:
        logfile = open(LOGFILENAME, 'a')
        logfile.write(','.join(strings))

    logfile.close


def main():
    pass


if __name__ == '__main__':
    main()

