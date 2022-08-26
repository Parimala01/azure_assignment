# azure_assignment
Connect to the Virtual machine by running this command on terminal
"ssh -i <private key path> azureuser@20.106.207.11" , the private key will already be downloaded while creating the virtual machine using SSH connect.

The next step is to deploy the flask app in the virtual machine. Download the templates and app.py file in this repository to another folder in your virtual machine.
Run the command 'python3 app.py' in your terminal, make sure you are inside the folder. The output will be a url where the information about the container is displayed.


The webpage looks something like this
![flask app](https://user-images.githubusercontent.com/100401594/186834501-f477d78b-6f62-4f8b-8ced-2e5e54f12425.png)

Exit fromt the virtual machine and stop the vm in your azure account. To get the billing information about this particulart resource, got to the resource group in which you have created the resource and on the left menu you can see cost analysis. apply filters to this cost analysis graph for you particular resource by using tags. This following charts will be visible

![costanalysis_charts (1)](https://user-images.githubusercontent.com/100401594/186835074-1b26cf34-264a-4a77-9f98-9b2c8383e30a.png)





