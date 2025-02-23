#!/bin/py
# service_check.py
# v.iroshan

from checks import AgentCheck
import os
import subprocess

class serviceCheck(AgentCheck):
    def check(self, instance):

        service_name = 'nginx'
        service_avail_command = 'systemctl list-units --full -all | grep -Fq "nginx.service"'
        service_status_command = f'systemctl status {service_name}'
        service_active_command = service_status_command + " | awk 'NR==3{print$1$2}'"
        datadog_gauge = f'service_availability.{service_name}'
        status = {
            'active' : 1,
            'inactive' : 0,
            'failed' : -1
        }
        
        try:
            service_available = subprocess.check_output(service_avail_command, shell=True, text=True).decode('utf-8')
            if not service_available:
                warning_string = f"The service {service_name} is not installed in the instance."
                self.log.warning(warning_string)
                return
            
            service_status = subprocess.check_output(service_active_command, shell=True, text=True).decode('utf-8')
            # service_status = 'Active:active'
            self.log.info(service_status)
            self.gauge(datadog_gauge, status[service_status.split(':')[-1]])
        except Exception as e:
            self.log.error("Error: %s", str(e))