import os
import settings as s

def files(r, _ext):
    rtn = []

    for root, _, files in os.walk(r):
        for file in files:
            if _ext == 'o':
                if file.endswith('.o'):
                    print("found: " + os.path.join(root, file))
                    rtn.append(os.path.join(root, file))
            else:
                path, ext = os.path.splitext(os.path.join(root, file))
                if ext in s.ext[_ext]:
                    print("found: " + path + ext)
                    rtn.append(path + ext)
                    pass

    return rtn

def main():
    llen = 0
    for cc in ['c', 'cpp']:
        for i in files(s.path['sources'], cc):
            cmd = s.path[cc] + ' -c ' + i + ' -o ' + s.path['obj'][0] + '/' + i.replace('/', '').replace('.', '').replace('\\','') + str(llen) + '.o'
            llen += 1
            print("Compile: " + cmd)
            os.system(cmd)

    if s.mode == 'exe':
        cmd = s.path['cpp'] + ' -o ' + s.path['build'] + ' ' + ''.join((e + ' ') for e in [item for i in s.path['obj'] for item in files(i, 'o')])
    print("Run: " + cmd)
    os.system(cmd)

if __name__ == "__main__":
    main()