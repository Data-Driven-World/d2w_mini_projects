# Deploying Flask Project to Amazon Elastic Beanstalk

## Setup

You should have received an email for AWS Educate account. If you have not, please contact your instructor. 

### Installing EB CLI

You may want to install Elastic Beanstalk Command Line Interface (EB CLI). Follow the following links according to your OS:
- [Installing EB CLI for Mac OS](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-osx.html). The installation steps here assumes you have Homebrew. If you do not have, [install Homebrew first](https://brew.sh/).
- [Installing EB CLI for Windows](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-windows.html)

### Creating AWS Educate Starter Account

### Creating Access Key

1. Login to your AWS Educate Platform at [https://www.awseducate.com/](https://www.awseducate.com/).
1. Go to classroom.
    ![](https://www.dropbox.com/s/fwrvxrc374zj5hn/credential_1.png?raw=1)
1. Click the button "Account Details".
	![](https://www.dropbox.com/s/v8cwxnrap1f84yo/credential_2.png?raw=1)
1. Under AWS CLI, click "Show".
	![](https://www.dropbox.com/s/uppsfd9d6i658mt/credential_3.png?raw=1)
1. Create a new text file using any plain text editor and save the information into the text file. Keep the information in a safe place and **do not put it in your public repository**.
    ![](https://www.dropbox.com/s/m9qpgn17f1kzeae/credential_4.png?raw=1)

## Deploying to Elastic Beanstalk

Open Terminal or Anaconda Prompt. Go to the folder of your project. For example,

```
$ cd ~/fip_powerx_mini_projects/mp_sort
```
or
```
> cd %USERPROFILE%\fip_powerx_mini_projects\mp_sort
```

1. Initialze the folder for EB repository by typing the following:

	```
	$ eb init -p python-3.6 miniproject1 --region us-east-1
	```

1. Run eb init again to configure a default keypair so that you can connect to the EC2 instance running your application with SSH:

	```
	$ eb init
	Do you want to set up SSH for your instances?
	(y/n): y
	Select a keypair.
	1) my-keypair
	2) [ Create new KeyPair ]
	```
	Select a key pair if you have one already, or follow the prompts to create a new one. If you don't see the prompt or need to change your settings later, run `eb init -i`.

1. Create an environment and deploy your application to it with `eb create <name of environment>`.
    ```
	eb create flask-env
    ```

    You will see a lot of messages on the screen, but the end, if everything is successful, you should see the following:
    ```
    INFO Successfully launched environement: flask-env
    ```

1. To open the web app in your browser, type:

	```
	$ eb open
	```
	
## Checking Status

To check status of your instance, type:

```
$ eb status
```

## Terminating Instance

To terminate your instance, type:

```
$ eb terminate 
```
## References

- [Deploying a Flask Application to Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html#python-flask-setup-venv)

