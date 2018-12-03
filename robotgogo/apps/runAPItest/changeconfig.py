rfDIR="/root/mygithub/quality/automation/rf/compass/devops/"




def changeconfigIP(IP):
    print("good")
    data = ''
    envFile=rfDIR + "环境信息/globalEnv.txt"
    with open(envFile,"r",encoding="utf-8") as f:
        for line in f.readlines():
            if line.find('${compass_ip}') == 0:
                line = "${compass_ip}" + "      " + IP + '\n'
            data += line

    with open(envFile, "w", encoding="utf-8") as f:
        f.writelines(data)


def changeconfigRegistry(Registry):
    print("good")
    data = ''
    with open(envFile,"r",encoding="utf-8") as f:
        for line in f.readlines():
            if line.find('${compass_ip}') == 0:
                line = "${compass_ip}" + "      " + IP + '\n'
            data += line

    with open("/home/ubuntu/mygithub/rf/compass/devops/环境信息/globalEnv.txt", "w", encoding="utf-8") as f:
        f.writelines(data)
