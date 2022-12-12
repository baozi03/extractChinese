import configparser,os
#from config import path
class Config():
    def __init__(self,conf_name,encoding='utf-8'):
        current_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        print(current_path)
        self.cf = configparser.ConfigParser(allow_no_value = True)
        self.file = current_path+"/config/" + conf_name
        print(self.file)
        self.cf.read(self.file,encoding="utf-8-sig")  #编码格式就是个坑！！！

    def getSections(self):
        return self.cf.sections()

    def addSection(self,sectionName):
        self.cf.add_section(sectionName)

    def setValue(self, section, option,value):
        self.cf.set(section, option, value)

    def writeFile(self):
        try:
            with open(self.file, "w+",encoding="utf-8-sig") as f:
                self.cf.write(f)
        except ImportError:
            f.close()

    def writeInfo(self, section, option, value):
        # print(section, option,value)
        self.setValue(section, option, value)
        self.writeFile()


if __name__ == '__main__':
    test = Config("resulfText001.cfg")
    #test.addSection("app.json")
    dsksd = [0,1,2]

    test.writeInfo("app.json","dsdsdsds.js",str(dsksd))
    print(test.getSections())

