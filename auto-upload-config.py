#!/usr/bin/env python3
import os
import sys
import json


#filePath = sys.argv[2]
def upload(filePath, password):
    filePathName = os.path.basename(filePath)
    fileName = os.path.splitext(filePathName)[0]
    os.system("mkdir -p upload")
    os.system(f'sshpass -p "{password}" rsync -avP -e ssh "{filePath}" gfdgd-xi@frs.sourceforge.net:/home/frs/project/deep-wine-runner-wine-download')
    os.system(f"git clone git@github.com:gfdgd-xi/wine-mirrors-websize.git")
    os.system("cd wine-mirrors-websize ; git pull")
    lists = []
    with open("wine-mirrors-websize/information.json", "r") as file:
        lists = json.loads(file.read())

    archMap = {
        "i386": "/usr/lib/i386-linux-gnu/ld-linux.so.2",
        "amd64": "/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2",
        "armhf": "/usr/lib/arm-linux-gnueabihf/ld-linux-armhf.so.3",
        "armel": "/usr/lib/arm-linux-gnueabi/ld-linux.so.3",
        "arm64": "/usr/lib/aarch64-linux-gnu/ld-linux-aarch64.so.1",
        "aarch64": "/usr/lib/aarch64-linux-gnu/ld-linux-aarch64.so.1",
        "riscv64": "/usr/lib/riscv64-linux-gnu/ld-linux-riscv64-lp64d.so.1",
        "mips64el": "/usr/lib/mips64el-linux-gnuabi64/ld.so.1",
        "ppc64el": "/usr/lib/powerpc64le-linux-gnu/ld64.so.2",
        "loong64": "/usr/lib/loongarch64-linux-gnu/ld-linux-loongarch-lp64d.so.1",
        "loongarch64": "/usr/lib/loongarch64-linux-gnu/ld.so.1",
        "x86_64": ["/usr/lib/i386-linux-gnu/ld-linux.so.2", "/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2"]
    }
    systemGlibcMap = {
        "debian11": "2.31",
        "debian12": "2.36",
        "ubuntu18": "2.27",
        "ubuntu20": "2.31",
        "ubuntu22": "2.35",
        "ubuntu24": "2.39"
    }
    isSearch = False
    tagList = []
    for k in archMap.keys():
        if k in fileName:
            isSearch = True
            isSystem = False
            for g in systemGlibcMap.keys():
                if g in fileName:
                    isSystem = True
                    if (type(archMap[k]) == list):
                        allTag = [k, systemGlibcMap[g]]
                        for d in archMap[k]:
                            allTag.append(d)
                        tagList.append(allTag)
                    else:
                        tagList.append([systemGlibcMap[g], archMap[k]])
            if (not isSystem):
                if (type(archMap[k]) == list):
                    allTag = [k]
                    for d in archMap[k]:
                        allTag.append(d)
                    tagList.append(allTag)
                else:
                    tagList.append([archMap[k]])
            # box86+binfmt
            if k == "i386":
                tagList.append("exagear")
                tagList.append(["box86", "binfmt"])
                tagList.append(["lat", "lat-i386", "binfmt"])
                tagList.append(["qemu-user", "qemu-user-i386", "binfmt"])
            if k == "amd64":
                tagList.append("exagear")
                tagList.append(["box64", "binfmt", "!loong64-kernel-8k-pagesize", "!loong64-kernel-16k-pagesize", "!loong64-kernel-32k-pagesize", "!loong64-kernel-64k-pagesize"])
                tagList.append(["lat", "lat-amd64", "binfmt"])
                tagList.append(["qemu-user", "qemu-user-amd64", "binfmt"])
            if k == "x86_64":
                tagList.append("exagear")
                tagList.append(["box86", "box64", "binfmt", "!loong64-kernel-8k-pagesize", "!loong64-kernel-16k-pagesize", "!loong64-kernel-32k-pagesize", "!loong64-kernel-64k-pagesize"])
                tagList.append(["lat", "lat-i386", "lat-amd64", "binfmt"])
                tagList.append(["qemu-user", "qemu-user-i386", "qemu-user-amd64", "binfmt"])
            if ("wow64" in fileName or "deepin-wine8-stable" in fileName) and (not "box64" in fileName):
                tagList.append(["box64", "!loong64-kernel-8k-pagesize", "!loong64-kernel-16k-pagesize", "!loong64-kernel-32k-pagesize", "!loong64-kernel-64k-pagesize"])
                tagList.append("exagear")            
                tagList.append(["lat", "lat-amd64", "binfmt"])
                tagList.append(["qemu-user", "qemu-user-amd64", "binfmt"])
            #if ("box64" in fileName and "wow64" in fileName):
            #    tagList.append(["!loong64-kernel-8k-pagesize", "!loong64-kernel-16k-pagesize", "!loong64-kernel-32k-pagesize", "!loong64-kernel-64k-pagesize"])
    if (not isSearch):
        tagList = []
        allTag = []
        # 没有被任何一种情况识别到，则使用默认
        for d in archMap["x86_64"]:
            allTag.append(d)
            tagList = []
            tagList.append("exagear")
            tagList.append(["box86", "box64", "binfmt", "!loong64-kernel-8k-pagesize", "!loong64-kernel-16k-pagesize", "!loong64-kernel-32k-pagesize", "!loong64-kernel-64k-pagesize"])
            tagList.append(["lat", "lat-i386", "lat-amd64", "binfmt"])
            tagList.append(["qemu-user", "qemu-user-i386", "qemu-user-amd64", "binfmt"])
    #lists.insert(8, [fileName, f"https://sourceforge.net/projects/deep-wine-runner-wine-download/files/{fileName}.7z", tagList])
    lists.insert(8, [fileName, f"https://sourceforge.net/projects/deep-wine-runner-wine-download/files/{fileName}.7z", []])
    jsonStr = json.dumps(lists, ensure_ascii=False, indent=4)
    print(tagList)
    #print(jsonStr)
    with open("wine-mirrors-websize/information.json", "w") as file:
        file.write(jsonStr)
    os.system("cd wine-mirrors-websize ; git add .")
    os.system(f"cd wine-mirrors-websize ; git commit -m 'Add {fileName}.7z'")
    os.system(f"cd wine-mirrors-websize ; git push")
    #"https://sourceforge.net/projects/deep-wine-runner-wine-download/files/spark-wine8-8.20.7z/download"

password = sys.argv[1]
for i in sys.argv[2:]:
    upload(i, password)