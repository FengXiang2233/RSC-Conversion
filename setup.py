from src import util,rsc

import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    util.clean("./out")
    rscObj=rsc.rsc("./in")
    rscObj.newInfo()
    rscObj.groupsConversion()
    rscObj.itemsConversion()