#!/bin/py
# tls_check.py
# v.iroshan

from checks import AgentCheck
import os
import subprocess
from datetime import datetime

class tlsCheck(AgentCheck):
    def check(self, instance):
        # date format
        date_format = "%Y-%m-%d"
        # Replace "certificate_path" with the actual path to your certificate file
        domain_name = "domain.com"
        certificate_path = f"/etc/nginx/ssl/{domain_name}.crt"

        try:
            # Specify the path to the file you want to check
            if os.path.exists(certificate_path):
                # Run the openssl command and capture the output
                openssl_command = f"openssl x509 -in {certificate_path} -noout -enddate"
                output = subprocess.check_output(openssl_command, shell=True, text=True)

                # Extract the end date value
                end_date = output.split("=")[1].strip()

                # Parse the date string
                parsed_date = datetime.strptime(end_date, "%b %d %H:%M:%S %Y %Z")

                # Format the date as "yyyy-mm-dd"
                expiry_date = datetime.strptime(parsed_date.strftime(date_format), date_format)
                current_date = datetime.strptime(str(datetime.now().date()), date_format)
                delta = expiry_date - current_date

                # print(f"Time left to expire: {delta.days}")
                self.gauge('tls_check.crt_days_left', delta.days)
            else:
                self.log.warning("Certificate file cannot reach.")
        except FileNotFoundError:
            self.log.warning("Certificate file not found.")
        except Exception as e:
            self.log.error("Error: %s", str(e))
