import glob#, path
import os
from datetime import datetime as dt
import src.Utils.read_inputfile as read_ini
import src.Utils.send_alert as alert
import src.Utils.utils as utils


def select_targetfiles(settings):
    # iniファイルの設定からファイルを検索するファイル群を決定する。
    targetfolderpath = settings['folderpath']
    targetfilecategory = settings['category']
    # FileNameを現在の日時で決定する
    targetfilename = settings['findstring']
    targetfiles = [os.path.basename(r) for r in
                   glob.glob(targetfolderpath + '\\' + targetfilename + '.' + targetfilecategory)]

    return targetfiles


def get_target_filename(settings):
    # 検索するファイルの名称を決定する。
    # iniファイルのパターンごとにif文を追加するため改善の余地あり

    if settings['namepattern'] == 0:
        target_filename = 'Prediction' + dt.now().strftime('%Y%m%d%H') + '.' + settings['category']
    elif settings['namepattern'] == 1:
        print("定義されていません。")
    elif settings['namepattern'] == '':
        pass

    return target_filename


def exists_targetfile(settings) -> bool:
    # ファイルが出力されているか確認する機能　ok 1,error 0

    # iniファイルから検索するファイル群を決定する
    targetfiles = select_targetfiles(settings)

    # ファイル群がない場合エラー
    if targetfiles == []:
        print('PLEASE CHECK FILE CATEGORY , FILE NOT EXISTS')
        return 0

    # ファイル群から1つずつファイルを確認する。
    try:
        for targetfile in targetfiles:
            # ファイル群のファイルと設定したファイル名が一致したらflg=1
            if targetfile == get_target_filename(settings):
                print('File exists')
                flg = 1
                break
            else:
                # print('File not exist')
                flg = 0

    except UnboundLocalError:
        print('FILE NOT FOUNDの可能性')
        flg = 0

    return flg


def main():
    # 初期ファイルの作成
    utils.generate_input_files()

    # iniファイルのセクションから、場所を決定する。
    target_locations = read_ini.select_targetlocation()

    # 場所の数だけループを回してデータがあるか確認する。
    for target in target_locations:
        settings = read_ini.read_initxt(target)
        flg = exists_targetfile(settings)

        if flg == 1:
            # OKの時は特に動作しない
            print(target + ' : OK')
        else:
            print(target + ' : ERROR')
            # メール送信
            users = read_ini.select_targetuser()
            for user in users:
                alert.send_email(target, user)

        # TODO log出力
        utils.write_log(target, flg)


if __name__ == '__main__':
    main()

