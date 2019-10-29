# Deploying Static Website in AWS using Ansible

This project is to create and deploy a running instance of static webserver using Ansible. 

### Step1:  Ansible Setup
Create an Ec2 instance with RHEL8 and install Ansible, this instance will act as a Ansible centralized server. Create a user "ansible" and assign to Sudo, add SSH keypair and allow ansible user to work without password. 

### Step2: Ansible playbook roles
Write playbooks to create roles for:
* apache - To install and configure apache in the servers,
* aws_ec2 - To provision and configure Ec2 instances
* ami_snapshot - To build customized AMI for auto scaling

Create a playbook (deployStaticWebsite.yml) that uses these roles to create Ec2 instance from the AMI, install apache and deploy the static website.

### Step3: Run Playbooks
Once the playbooks are ready, run playbooks using the command :
ansible-playbook <playbookname>.yml
 
* Run env_vars_files/env_variables playbook to get the environment variables such as VPC_subnet_id, security group name etc..
* Include the <>.pem file to env_vars_files folder
* Run aws_ec2/defaults/main.yml file to provision EC2 instances
* Run ami_snapshot/defaults/main.yml file to build a customized AMI
* Finally run deplotStaticWebsite.yml file to deploy static website.

___________________________________________________________________________________

# Python code for Complex numbers operations:

Please find the code that perform addition, subtraction, multiplication, division, modulus operations on two Complex numbers.

Command to run:
python3 ComplexNumberOperations.py

