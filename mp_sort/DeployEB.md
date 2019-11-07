# Deploying Flask Project to Amazon Elastic Beanstalk

## Setup

You should have received an email for AWS Educate account. If you have not, please contact your instructor. 

### Installing EB CLI

You may want to install Elastic Beanstalk Command Line Interface (EB CLI). Follow the following links according to your OS:
- [Installing EB CLI for Mac OS](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-osx.html). The installation steps here assumes you have Homebrew. If you do not have, [install Homebrew first](https://brew.sh/).
- [Installing EB CLI for Windows](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-windows.html)

### Creating AWS Educate Starter Account

### Creating IAM Users

1. Login to your AWS Educate Platform at [https://www.awseducate.com/](https://www.awseducate.com/).
1. Go to the AWS console.
    ![](https://www.dropbox.com/s/pwgdgvoruuacneq/iam_create_1.png?raw=1)
1. Select IAM service and click.
    ![](https://www.dropbox.com/s/ja49hnlmtdph2ov/iam_create_2.png?raw=1)
1. Create User.
    ![](https://www.dropbox.com/s/natg7zii1m3lo35/iam_create_3.png?raw=1)
1. Enter user name and choose programmatic access.
    ![](https://www.dropbox.com/s/vjroz5iso4vvzw9/iam_create_4.png?raw=1)
1. Create Group.
    ![](https://www.dropbox.com/s/a0nknc9jafmdtl4/iam_create_5.png?raw=1)
1. Enter Group name and choose AdministratorAccess.
    ![](https://www.dropbox.com/s/4odytdfu6n32czd/iam_create_6.png?raw=1)
1. Add the user to the group and click next.
    ![](https://www.dropbox.com/s/7val7qfzd03jw8m/iam_create_7.png?raw=1)
1. Skip tag and click next.
    ![](https://www.dropbox.com/s/mcc2ovu4p5q12us/iam_create_8.png?raw=1)
1. Download the CSV file containing your Access key ID and Secret access Key.
    ![](https://www.dropbox.com/s/csskhflpieru52h/iam_create_9.png?raw=1)

## Deploying to Elastic Beanstalk

Open Terminal or Anaconda Prompt. Go to the folder of your project. For example,

```
$ cd ~/Downloads/d2w_mini_projects/mp_sort
```
or
```
> cd %USERPROFILE%\Downloads\d2w_mini_projects\mp_sort
```

1. Initialze the folder for EB repository by typing the following:

	```
	$ eb init -p python-3.6 miniproject1 --region ap-southeast-1
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

