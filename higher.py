import os
import psutil
import platform

def info():
    arq = platform.machine()
    nod = platform.node()
    proc = platform.processor()
    sys = platform.system()
    rels = platform.release()
    plat = platform.platform()

    option = ("""
    Arquitetura:     {}
    Nome Sistema:    {}
    Plataforma:      {}
    Processador:     {}
    Sistema:         {}
    Release Sistema: {}
""".format(arq, nod, plat, proc, sys, rels))
    convert = str(option)
    print(convert)

def wireless():
    tcp = psutil.net_connections(kind='tcp')
    inet = psutil.net_connections(kind='inet')
    addr = psutil.net_if_addrs()
    stats = psutil.net_if_stats()
    user = psutil.users()

    print("""
    TCP:       {}
    INET:      {}
    Address:   {}
    Stats:     {}
    Users:     {}

""".format(tcp, inet, addr,stats, user))

def pid():
    for proc in psutil.process_iter(['pid', 'name', 'username']):
       print(proc.info)
