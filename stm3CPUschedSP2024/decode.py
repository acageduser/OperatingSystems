#!/usr/bin/python
# decode.py to decode a codeTable error message from an STM run.
# D. Parson, 2/16/2020

import sys

foundit = False

if __name__ == '__main__':
    if len(sys.argv) != 3 or not sys.argv[1].endswith('.py'):
        sys.stderr.write('ERROR, Usage: decode.py STMFILE.py codeTableLine\n')
        sys.exit(1)
    f = open(sys.argv[1], 'r')
    lnum = int(sys.argv[2])
    if (lnum < 0):
        sys.stderr.write('ERROR, negative line number: ' + str(lnum) + '\n')
        sys.stderr.write('ERROR, Usage: decode.py STMFILE.py codeTableLine\n')
        sys.exit(1)
    line = f.readline()
    codeline = -1
    while line:
        while line and not line.strip().startswith('__codeTable__ = '):
            line = f.readline()
        if line:
            # Otherwise there is no codeTable
            codeline = 0
            line = f.readline()
            while line and codeline < lnum:
                line = f.readline()
                codeline += 1
            if line and codeline == lnum:
                sys.stdout.write('\n__codeTable__[' + str(lnum) + '] = '
                    + line.strip() + '\n')
                foundit = True
                break
    f.close()
    if not foundit:
        sys.stderr.write('\nCould not find __codeTable__[' + str(lnum)
            + '] in file ' + sys.argv[1] + '\n')
        sys.exit(1)
    sys.exit(0)
