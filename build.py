import os
import settings as s

def files(r):
    rtn = []

    fs = os.listdir(r)
    for f in fs:
        path, ext = os.path.splitext(os.path.join(r, f))
        if ext in s.srcExtensions:
            print("found: " + path + ext)
            rtn.append(path + ext)
            pass
                

    return rtn

if __name__ == "__main__":
    cmd = s.path['gcc'] + ' ' + s.args['pre'] + ' ' + s.path['build'] + ' ' + ''.join((e + ' ') for e in files(s.path['sources']))
    cmd = cmd if s.super_ignore_and_just_run_this == '' else s.super_ignore_and_just_run_this
    print("Run: " + cmd)
    os.system(cmd)