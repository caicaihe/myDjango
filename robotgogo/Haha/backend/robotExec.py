import os


def  runRobot():
    robotScrptDir = "/home/ubuntu/mygithub/rf/compass/devops/测试用例/API/devopsAPI.txt"
    resultDir = "/home/ubuntu/mygithub/tmp/report"
    command = "robot --outputdir"+"  "+resultDir+" "+robotScrptDir
    print(command)
    output = os.system(command)
    if output:
        return 1



    
