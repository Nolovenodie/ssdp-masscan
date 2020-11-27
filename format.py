import sys
import json


def main():
    if len(sys.argv) <= 1:
        print('format.py <filename_json> <filename_output>')
        exit()

    f = open(sys.argv[1], encoding='utf-8')
    data = json.load(f)
    r = open(sys.argv[2], 'w')
    count = len(data)
    success = 0
    for i in data:
        ip = i['ip'].strip()
        if ip != '':
            r.writelines(i['ip']+'\n')
            success += 1
    print('All data entries :%s / Successful conversion :%s' % (count, success))


if __name__ == "__main__":
    main()
