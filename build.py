import os
import settings as s

def files(r, _ext):
    rtn = []

    if(_ext == 'o'):
        fs = os.listdir(r)
        for f in fs:
            path, ext = os.path.splitext(os.path.join(r, f))
            if ext == '.o':
                print("found: " + path + ext)
                rtn.append(path + ext)
                pass
            pass

        return rtn
        pass

    fs = os.listdir(r)
    for f in fs:
        path, ext = os.path.splitext(os.path.join(r, f))
        if ext in s.ext[_ext]:
            print("found: " + path + ext)
            rtn.append(path + ext)
            pass
                

    return rtn

if __name__ == "__main__":
    for cc in ['c', 'cpp']:
        for i in files(s.path['sources'], cc):
            cmd = s.path[cc] + ' -c ' + i + ' -o ' + s.path['obj'] + '/' + i.split('/')[1].split('.')[0] + '.o'
            print("Compile: " + cmd)
            os.system(cmd)

    cmd = s.path['cpp'] + ' -o ' + s.path['build'] + ' ' + ''.join((e + ' ') for e in files(s.path['obj'], 'o'))
    cmd = cmd if s.super_ignore_and_just_run_this == '' else s.super_ignore_and_just_run_this
    print("Run: " + cmd)
    os.system(cmd)