




def changeconfigIP(IP):
    print("good")
    data = ''
    with open("/home/ubuntu/mygithub/rf/compass/devops/环境信息/globalEnv.txt","r",encoding="utf-8") as f:
        for line in f.readlines():
            if line.find('${compass_ip}') == 0:
                line = "${compass_ip}" + "      " + IP + '\n'
            data += line

    with open("/home/ubuntu/mygithub/rf/compass/devops/环境信息/globalEnv.txt", "w", encoding="utf-8") as f:
        f.writelines(data)
