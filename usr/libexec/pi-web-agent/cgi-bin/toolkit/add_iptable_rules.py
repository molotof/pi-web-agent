#!/usr/bin/python
import sys, os
if 'MY_HOME' not in os.environ:
    os.environ['MY_HOME']='/usr/libexec/pi-web-agent'
sys.path.append(os.environ['MY_HOME']+'/cgi-bin/api')
sys.path.append(os.environ['MY_HOME']+'/cgi-bin/')
from HTMLPageGenerator import *
from cernvm import Response
import cgi
import cgitb
from subprocess import Popen, PIPE

cgitb.enable()

from live_info import execute

#executes the command to add a new protocol rule
def addProtocolRule(chain, action, protocol):
    return execute('sudo iptables -A ' + chain + ' -p ' + protocol + ' ' + action)

def main():   
    form = cgi.FieldStorage()
    #form={'action':'uninstall', 'packageName':'tree'}
    chain = form['chain'].value
    protocol=form['protocol'].value
    action=form['action'].value
    output = ''
    '''
    if form['action'].value == 'install' :
        output, errorcode = installPackage(pName)
    elif form['action'].value == 'uninstall' :
        output, errorcode = uninstallPackage(pName)
    '''

    addProtocolRule(chain, action, protocol)
    response = Response(0)
        
    response.buildResponse(errorcode)
    composeXMLDocument(response.xml)

if __name__ == '__main__':
    main()
