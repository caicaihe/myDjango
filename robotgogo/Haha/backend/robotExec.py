import os


def  runRobot():
    robotScrptDir = "~/mygithub/quality/automation/rf/compass/devops/测试用例/API/devopsAPI.txt"
    resultDir = "/opt/rfresult/devops/report"
    command = "robot --outputdir"+"  "+resultDir+" "+robotScrptDir
    print(command)
    output = os.system(command)
    if output:
        return 1



    
