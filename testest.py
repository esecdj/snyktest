"""
SCA scan example

"""
import json
import time
from datetime import datetime
from os.path import exists
import pandas as pd

from CheckmarxPythonSDK.CxScaApiSDK import (
    get_project_id_by_name,
    get_risk_report_summary,
    get_packages_of_a_scan,
    get_vulnerabilities_of_a_scan,
    get_licenses_of_a_scan,
    get_all_projects,
)
mylist = []
formatted_list = []
def sca_scan():
    for project in get_all_projects():
        #print(project)
        vuln = get_risk_report_summary(project_id=project['id'], size=1)
        mylist.append({
            'projectname': project['name'],
            'team': project['assignedTeams'],
            'critical': vuln[0]['criticalVulnerabilityCount'] if vuln else 0,
            'high': vuln[0]['highVulnerabilityCount'] if vuln else 0,
            'medium': vuln[0]['mediumVulnerabilityCount'] if vuln else 0,
            'low': vuln[0]['lowVulnerabilityCount'] if vuln else 0
        })
        print(mylist)
    print(mylist)
# testing pr
    for item in mylist:
        formatted_item = {
            'project': item.get('projectname', ''),
            'team': item['team'][0] if isinstance(item.get('team'), list) and item['team'] else item.get('team', ''),
            'critical': item.get('critical', 0),
            'high': item.get('high', 0),
            'medium': item.get('medium', 0),
            'low': item.get('low', 0),
        }
        formatted_list.append(formatted_item)
    df = pd.DataFrame(formatted_list, columns=['project', 'team', 'critical', 'high', 'medium', 'low'])
    df.to_excel("vulnerability_report.xlsx", index=False)

if __name__ == "__main__":
    projects = []
    sca_scan()
