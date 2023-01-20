import json
'''
功能：读取 func_and_para.json，将格式转化后写入固定格式

实例：
    func_name:int add(int a, int b)
    func_para:[1, 2]

    转换后：
    typedef int (*addFunc)(int a, int b);
    addFunc addFuncPtr = (addFunc)testControl->getFunction(, "add");
    addFuncPtr(1, 2);
'''

def read_file():
    with open("func_and_para.json", "r", encoding="utf-8") as f:
        func_arr = json.load(f)
        pass
        f.close()

def write_file():
    with open("uml.h", "w+", encoding="utf-8") as f:
        f.write()

        f.close()

if __name__ == '__main__':
    pass