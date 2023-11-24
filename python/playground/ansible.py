import boto3
import yaml

def get_ec2_instances():
    ec2 = boto3.resource('ec2')
    instances = ec2.instances.all()
    return instances

def create_hosts_yaml(instances):
    hosts = []
    for instance in instances:
        host = {
            'name': instance.id,
            'private_ip': instance.private_ip_address,
            'public_ip': instance.public_ip_address,
            'name': instance.public_ip_address,

            # Add more properties as needed
        }
        hosts.append(host)
    
    with open('hosts.yaml', 'w') as file:
        yaml.dump(hosts, file)

if __name__ == '__main__':
    instances = get_ec2_instances()
    create_hosts_yaml(instances)