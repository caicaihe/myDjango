rfDIR="/root/mygithub/quality/automation/rf/compass/devops/"




def changeconfigIP(IP):
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
    data = ''
    envFile = rfDIR + "环境信息/globalEnv.txt"
    with open(envFile, "r", encoding="utf-8") as f:
        for line in f.readlines():
            if line.find('${registry_url}') == 0:
                line = "${registry_url}" + "      " + Registry + '\n'
            data += line

    with open(envFile, "w", encoding="utf-8") as f:
        f.writelines(data)
