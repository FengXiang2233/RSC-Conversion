import logging
import yaml
import os

from src import util

class rsc:

    id:str
    inPath:str

    def __init__(self,inPath):
        self.inPath=inPath

    def newInfo(self):
        logging.info("初始化Info.yml")
        infoMap={}
        id = input("id: ")
        infoMap["id"]=id
        self.id=id.upper()
        authors = input("authors: ")
        infoMap["authors"]=[authors]
        infoList=["name","version"]
        for key in infoList:
            infoMap[key]=input(f"{key}: ")
        with open("./out/info.yml","w") as file:
            file.write(yaml.dump(infoMap,allow_unicode=True))

    def groupsConversion(self):
        if not os.path.isfile(self.inPath+"/categories.yml"):
            logging.error("输入categories.yml不存在")
            logging.error("转换出错 停止转换")
            return
        scGroupsMap:dict=yaml.safe_load(open(self.inPath+"/categories.yml","r",encoding="UTF-8").read())
        if not scGroupsMap:
            logging.error("输入categories.yml为空")
            logging.error("转换出错 停止转换")
            return
        rscGroupsMap={}
        open("./out/groups.yml","w").close()
        for key in scGroupsMap.keys():
            groupID=self.id.lower()+"_"+key
            rscGroupsMap[groupID]={
                "type":scGroupsMap[key]["type"],
                "item":{
                    "name":scGroupsMap[key]["category-name"]
                }
            }
            # group item
            if len(scGroupsMap[key]["category-item"])>5 and scGroupsMap[key]["category-item"][:5]=="SKULL":
                rscGroupsMap[groupID]["item"]["material"]=scGroupsMap[key]["category-item"][5:]
            else:
                rscGroupsMap[groupID]["item"]["material"]=scGroupsMap[key]["category-item"]
            # group type
            if rscGroupsMap[groupID]["type"] == "normal":
                pass
            elif rscGroupsMap[groupID]["type"] == "nested":
                with open("./out/groups.yml","a",encoding="UTF-8") as file:
                    file.write(yaml.dump({
                        groupID:rscGroupsMap[groupID]
                    },allow_unicode=True))
                rscGroupsMap.pop(groupID)
            elif rscGroupsMap[groupID]["type"] == "sub":
                rscGroupsMap[groupID]["parent"] = self.id.lower()+"_"+scGroupsMap[key]["parent"]
            elif rscGroupsMap[groupID]["type"] == "seasonal":
                rscGroupsMap[groupID]["month"] = scGroupsMap[key]["month"]
            elif rscGroupsMap[groupID]["type"] == "locked":
                rscGroupsMap[groupID]["parent"] = scGroupsMap[key]["parent"]
            else:
                logging.error("你的物品组类型是对的吗?")
                logging.error(f"请你告诉我在\"{key}\"中\""+rscGroupsMap[groupID]["type"]+"\"这个是怎么类型")
                logging.error("转换出错 停止转换")
                return
        with open("./out/groups.yml","a",encoding="UTF-8") as file:
            file.write(yaml.dump(rscGroupsMap,allow_unicode=True))
        logging.info("group转换完成")

    def itemsConversion(self):
        if not os.path.isfile(self.inPath+"/items.yml"):
            logging.error("输入items.yml不存在")
            logging.error("转换出错 停止转换")
            return
        scItemsMap:dict=yaml.safe_load(open(self.inPath+"/items.yml","r",encoding="UTF-8").read())
        if not scItemsMap:
            logging.error("输入items.yml为空")
            logging.error("转换出错 停止转换")
        open("./out/items.yml","w").close()
        util.copy(self.inPath+"/saveditems","./out/saveditems")
        rscItemsMap={}
        for key in scItemsMap.keys():
            itemID=self.id+"_"+key
            rscItemsMap[itemID]={
                "item_group":scItemsMap[key]["category"],
                "item":{
                    
                }
            }