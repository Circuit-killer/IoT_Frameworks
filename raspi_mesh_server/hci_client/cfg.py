import sys,os
import json
import logging as log
import socket

# -------------------- config -------------------- 
def get_local_json():
    """fetches the config.json file in the local directory
       if config_hostname.json is found it is used over the default one
    """
    config = None
    dirname = os.path.dirname(sys.argv[0])
    if(len(dirname) == 0):
        dirname = "."
    config_file = dirname+'/'+"config_"+socket.gethostname()+".json"
    if(os.path.isfile(config_file)):
        print("loading: ",config_file)
        config = json.load(open(config_file))
    else:
        config_file = dirname+'/'+"config.json"
        if(os.path.isfile(config_file)):
            print("loading: %s",config_file)
            config = json.load(open(config_file))
        else:
            print("Fatal error 'config.json' not found")
    return config


def configure_log(config):
    log_level_map = {
        "Debug"     :10,
        "Info"      :20,
        "Warning"   :30,
        "Error"     :40,
        "Critical"  :50
    }
    log.basicConfig(    filename=config["logfile"],
                        level=log_level_map[config["level"]],
                        format='%(asctime)s %(name)s %(levelname)-8s %(message)s',
                        datefmt='%d %H:%M:%S'
                        )
    log.getLogger('').addHandler(log.StreamHandler())
    log.info("log started @ level:%s",config["level"])
    return
