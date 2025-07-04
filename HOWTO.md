# Welcome to Connect Extension project Extension For Test

## Next steps

You may open your favourite IDE and start working with your project, please note that this project runs using docker.
You may modify at any time the credentials used to authenticate to connect modifying the file *another_extension_for_test/.another_extension_for_test_dev.env*.



In order to start your extension as a standalone docker container first of all you need to build the docker image for your project. To do that run:

```sh
$ docker compose build
```

Once your container is built, you can access the project folder and run:

```sh
$ docker compose up another_extension_for_test_dev
```

> please note that in this way you will run the docker container and if you do changes on the code you will need to stop it and start it again.


If you would like to develop and test at the same time, we recommend you run your project using the command:

```sh
$ docker compose run another_extension_for_test_bash
```

Once you get the interactive shell an help banner will be displayed to inform you about the included tools that can help you with the development of your extension.


Additionally, a basic boilerplate for writing unit tests has been created, you can run the tests using:

```sh
$ docker compose run another_extension_for_test_test
```


## Community Resources

Please take note of these links in order to get additional information:

* https://connect.cloudblue.com/
* https://connect.cloudblue.com/community/modules/devops/
* https://connect.cloudblue.com/community/sdk/python-openapi-client/
* https://connect-openapi-client.readthedocs.io/en/latest/
* https://connect-eaas-core.readthedocs.io/en/latest/
