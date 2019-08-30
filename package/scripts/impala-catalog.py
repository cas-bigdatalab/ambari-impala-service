# -*- coding: utf-8 -*-
from resource_management import *
from impala_base import ImpalaBase


class ImpalaCatalog(ImpalaBase):
    # Call setup.sh to install the service
    def install(self, env):

        # Install packages listed in metainfo.xml
        self.install_packages(env)

        cmd = 'yum-config-manager --add-repo  ' \
              'http://archive.cloudera.com/cdh5/redhat/6/x86_64/cdh/cloudera-cdh5.repo'

        Execute('echo "Running ' + cmd + '"')
        Execute(cmd)


        cmd = 'yum -y install  impala-server impala-catalog impala-state-store impala-shell'
        Execute('echo "Running ' + cmd + '"')
        Execute(cmd)
        self.configure(env)

    def configure(self, env):
        self.configureImpala(env)

    # Call start.sh to start the service
    def start(self, env):
        # self.configure(env)
        cmd = 'service impala-catalog start'
        Execute('echo "Running cmd: ' + cmd + '"')
        Execute(cmd)

    # Called to stop the service using the pidfile
    def stop(self, env):
        cmd = 'service impala-catalog stop'
        Execute('echo "Running cmd: ' + cmd + '"')
        Execute(cmd)

    def status(self, env):
        check_process_status("/var/run/impala/catalogd-impala.pid")


if __name__ == "__main__":
    ImpalaCatalog().execute()
