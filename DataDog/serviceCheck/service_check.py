#!/bin/py
# service_check.py
# v.iroshan

from checks import AgentCheck
import os
import subprocess

class tlsCheck(AgentCheck):
    def check(self, instance):

        service_name = 'nginx'
        service_avail_command = f'systemctl list-units --full -all | grep -Fq "{service_name}.service"'
        service_status_command = f'systemctl status {service_name}'
        instance_id = None
        datadog_gauge = f'service_availability.{service_name}'
        status = {
            'active' : 1,
            'inactive' : 0,
            'failed' : -1
        }
        
        try:
            service_available = subprocess.run(service_avail_command, capture_output=True, shell=True, text=True)
            if not service_available:
                warning_string = f"The service {service_name} is not installed in the instance."
                self.log.warning(warning_string)
                return
            
            service_status = subprocess.check_output(service_avail_command, shell=True, text=True)

            if service_status:
                ...

            self.gauge()
        except Exception as e:
            self.log.error("Error: %s", str(e))