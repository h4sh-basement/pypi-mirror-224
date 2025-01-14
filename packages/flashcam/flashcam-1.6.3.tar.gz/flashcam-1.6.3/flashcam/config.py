#!/usr/bin/env python3
from flashcam.version import __version__
from fire import Fire
import json
import os
import sys
"""
 Config for all modes of use. This is a primary source, as Flask is the primary operation mode
-------------------------------------
 o) encoding:
 oo) in the flow:
   - real_camera.py  ... cv2 VideoCapture .... V4L2 ... I use YUYV lately (v 1.2.) rather than MJPG
   - web.py          ... jpg creation with compression - COMPR = config.CONFIG['kompress']
   - stream_enhancer ... frame  via send_image  .... should be no compression
 oo ) recording:
   - izmq_receiver ... IYUV ... together with AVI .....   is HUGE ( I used to save 1 frame twice?)
   - stream_enhancer
         - seconds < 0 => motion detect/uni ... XVID + avi
         - seconds > 0 => laps ... XVID + avi  ***  IYUV good for astro: config.CONFIG['FOURCC']
"""
# ----- port here. 5000 is flask; is moved to 8000 by gunicorn; to 80 by nginx
CONFIG={  'filename':'~/.config/test/cfg.json',
          #'recommended':"",

          'average':0,
          'blur':0,
          'datapath': os.path.expanduser("~/DATA/"),
          'expo':'auto',  # EXPO
          'framekind':"direct", # direct , histo , detect
          'FOURCC':'DIVX',  # XVID=notmkv DIVX=mkv or IYUV
          'gain':'def',  # GAIN
          'Histogram':False,
          'imagezmq':None,
          'jtelegram':False,
          'kompress':90,
          'laps':0,
          'mmaga':'def',  # GAMMA
          'otate':0, # rotate 0
          'password':'aaa',
          'port':5000,
          'product':"",
          'qpassfile':"~/.pycamfw_userpass", # useless ??
          'resolution':"640x480",
          'save':False,  # ???
          'threshold':0,
          'user':'aaa',
          'vof':(110,-1), # field of view 110 degrees default (uniwrec only) and measured distance
          'web5000':False, # ????
          'XY':'1x1',  # position (uppercase)
          'x':0,
          'y':0,
          'zoom':1,

          'placeholder':False
}

#CFG_DEBUG = True
#CFG_DEBUG = False


#===========================================================
#===========================================================
#===========================================================

def verify_config(filename = ""):
    '''used inside, verification of bak json version'''
    global CONFIG
    if filename != "":
        CONFIG['filename'] = filename
    cfg = CONFIG['filename']
    #if CFG_DEBUG:print("D... verifying config from",cfg)
    ok = False
    try:
        if os.path.isfile( os.path.expanduser(cfg)):
            with open(os.path.expanduser(cfg), "r") as f:
                dicti = json.load(f)
        ok = True
        #if CFG_DEBUG:print("D... config verified")
    except:
        #if CFG_DEBUG:
        print("X... verification config FAILED")
    return ok

def get_config_file():
    ''' returns the filename where config is stored'''
    global CONFIG
    return CONFIG['filename']

def show_config( cdict=None , filename = ""):
    '''used inside, shows current config dictionary OR other dict'''
    global CONFIG
    if filename != "":
        CONFIG['filename'] = filename
    if cdict==None:
        print( json.dumps(CONFIG, indent=1) )
    else:
        print( json.dumps(cdict, indent=1) )


def cfg_to_bak(filenamebk="", filename = ""):
    '''used inside, rename config (before save)'''
    global CONFIG
    if filename != "":
        CONFIG['filename'] = filename

    if filenamebk=="":
        cfg = CONFIG['filename']
    else:
        cfg = filenamebk

    cfgbak = cfg + ".bak"
    #print("D... cfg:",cfg)
    #print("D... cfgbak:",cfgbak)
    #if CFG_DEBUG:
    #print("D... creating a backup config:", cfgbak )
    if not os.path.isfile( os.path.expanduser(cfg)):
        print(f"X... config {cfg} doesnt exist (yet?, OK)")
        return True

    ### rozXXXX
    try:
        os.rename(os.path.expanduser(cfg),
                  os.path.expanduser(cfgbak))
        result = True
    except:
        print("X... couldnt rename old:", cfg,"no bak file created")
        result = False
    return result


def bak_to_cfg(filenamebk="", filename = ""):
    '''used inside, rename back the bak version'''
    global CONFIG
    if filename != "":
        CONFIG['filename'] = filename

    if filenamebk=="":
        cfg = CONFIG['filename']
    else:
        cfg = filenamebk

    cfgbak = cfg + ".bak"
    #if CFG_DEBUG:
    #print("D... testing if backup config exists:", cfgbak)
    if os.path.isfile( os.path.expanduser(cfgbak)):
        #if CFG_DEBUG:
        #print("D... BACUP config exists:",cfgbak, "... renaming to:", cfg)
        os.rename(os.path.expanduser(cfgbak),
                  os.path.expanduser(cfg))
        #if CFG_DEBUG:print("D... config is recovered from:", cfgbak)
    #else:
        #if CFG_DEBUG:
        #print("D... bak config did not exist:", cfgbak,"no bak file recovery")


def save_config(filenamesv="", filename = ""): # duplicit... filename overrides
    '''FRONT function, save config to filename'''
    global CONFIG
    if filename != "":
        CONFIG['filename'] = filename

    if filenamesv=="":
        cfg = CONFIG['filename']
    else:
        cfg = filenamesv

    #print("D... calling cfg_to_bak:", cfg)
    if not cfg_to_bak(cfg):
        sys.exit(1)

    print("D... writing config:", cfg)

    ### rozxxx
    dir2create = os.path.dirname( cfg )
    #print("D...",dir2create)
    if not os.path.isdir( os.path.expanduser(dir2create )):
        print(f"D... trying to create directory {dir2create} if needed")
        result = False
        os.mkdir( os.path.expanduser(dir2create ))

    with open(os.path.expanduser(cfg), "w+") as f:
        f.write(json.dumps(CONFIG, indent=1))
        #if CFG_DEBUG:print("D... config was written:", cfg)

    if verify_config(filename):
        #if CFG_DEBUG:
        #print("D... verified by verify_config ... ok ... ending here")
        return True
    else:
        print("D... verified by verify_config ... NOT ok ... ending here")
        return False
    #====ELSE RECOVER BAK
    return bak_to_cfg()



def load_config(filename=""):
    '''FRONT function, load config file'''
    global CONFIG
    if filename != "":
        CONFIG['filename'] = filename
    cfg = CONFIG['filename']
    cfg = cfg+".from_memory"
    #if CFG_DEBUG:
    #print("D... calling save_config to frommemory:")
    save_config( cfg ) # from_memory file

    cfg = CONFIG['filename']
    #if CFG_DEBUG:print("D... loading config from",cfg)

    if not verify_config(filename):
        print("X... FAILED on verifications")
        return False

    #if CFG_DEBUG:
    #print("D... passed verification of:",cfg)
    dicti = CONFIG

    #if CFG_DEBUG:
    #print("D... directly loading json:",cfg)
    if os.path.isfile( os.path.expanduser(cfg)):
        with open(os.path.expanduser(cfg), "r") as f:
            dicti = json.load(f)

    # rewriting in memory
    if sorted(dicti.keys()) == sorted(CONFIG.keys()):
        #if CFG_DEBUG:
        #print("D... memory and disk identical:")
        pass
    else:
        #if CFG_DEBUG:
        print("X... memory and disk differ:")
        # show_config(CONFIG)
        # there may be more lines in the CODE after upgrade.
        for k in CONFIG.keys(): # search CODE version
            if not (k in dicti.keys()):
                print("D... key not on DISK:", k )
                dicti[k] = CONFIG[k]
                print(f"+... /{k}/ added to dicti with: ", dicti[k])


    CONFIG = dicti
    return True
    #if CFG_DEBUG:
    #print("D... final CONFIG:")
    #show_config(filename)
    #if CFG_DEBUG:
    #print("D... end load")


def loadsave(filename = ""):
    '''FRONT function, if DISK is earlier version than CODE, this may update DISK'''
    if filename != "":
        CONFIG['filename'] = filename

    load_config(filename)
    save_config() #?



#==========================================================



def func(debug = False):

    print("D... in unit config function func DEBUG may be filtered")
    print("i... in unit config function func - info")
    print("X... in unit config function func - ALERT")
    return True

def test_func():
    print("i... TESTING function func")
    assert func() == True

if __name__ == "__main__":
    print("i... in the __main__ of config of codeframe")
    Fire()
