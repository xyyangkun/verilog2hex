#!/usr/bin/python3
import os,sys

m = {}

def _init():
    global m
    m = {}
    for i in range(0,10):
        m[str(i)] = i
    m["a"]=10
    m['b']=11
    m['c']=12
    m['d']=13
    m['e']=14
    m['f']=15

    m["A"]=10
    m['B']=11
    m['C']=12
    m['D']=13
    m['E']=14
    m['F']=15
    print(m)


def trans(inf, outf):
    infile = open(inf, "r")
    outfile = open(outf, "w")
    
    for line in infile.readlines():
        print(line)
        line = line[1:-1]
        start = ":"
        addr = line[0:4]
        count = 0
        sum   = 0
        line = line[5:]
        print("line=%s"%line[:-1])
        data = ''
        # 处理一行的数据
        for item in line.split(' '):
            #print("%s"%item)
            data += item
            count+=1
            sum += m[item[0]] * 16
            sum += m[item[1]]

        count = hex(count)[2:]
        if len(count) != 2:
            count = '0' + count

        #count 
        sum += m[count[0]] * 16
        sum += m[count[1]]
        #addr
        sum += m[addr[0]] * 16
        sum += m[addr[1]]
        sum += m[addr[2]] * 16
        sum += m[addr[3]]

        sum = sum%256
        sum = 256 - sum
        sum = hex(sum)[2:]
        print("the end sum:%s count:%s"%(sum, count))

        if len(sum) != 2:
            sum = '0'+sum
        


        # 拼接一行数据
        l  =':'
        l += count.upper()
        l += addr.upper()
        l += "00"
        l += data
        l += sum.upper()
        l += '\r\n'
        print("==>%s"%l)
        # 写入一行数据
        outfile.write(l)
        
    # 写最后一行数据
    outfile.write(":00000001FF\r\n")
        

        
    






    infile.close()
    outfile.close()
    pass


if __name__ == '__main__':
    print("ok")
    _init()

    if(len(sys.argv) != 3):
        print("usage:%s in out to transfer verilog to hex", sys.argv[0])
        exit(0)
    trans(sys.argv[1], sys.argv[2])
