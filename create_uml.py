# 目标：读取文件内容(json、excel、txt)，转换格式后生成uml.h
'''
    unsigned int ConsoleAdd(int a, int b)
    [1, 2]
'''

'''
    typedef unsigned int (*ConsoleAddFunc)(int a, int b);

    ConsoleAddFunc ConsoleAddFuncPtr = (ConsoleAddFunc)testControl->getFunction(aa, bb, "ConsoleAdd");
    ConsoleAddFuncPtr(1, 2);
'''

def read_file():
    with open("a.txt", "r") as f:
        line = f.readline
        while(line):
            pass
            line = f.readline
        
        f.close()

def write_file():
    with open("uml.h", "w+") as f:
        f.write()

        f.close()  