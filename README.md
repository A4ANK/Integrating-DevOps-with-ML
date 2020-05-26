# Integration of DevOps tools with ML for autotuning the hyperparameters of the learning model.
![Jobs](/images/pipeline.jpg)
### Task description

1. Create container image that’s has Python3 and Keras or numpy  installed  using dockerfile 

2. When we launch this image, it should automatically starts train the model in the container.

3. Create a job chain of job1, job2, job3, job4 and job5 using build pipeline plugin in Jenkins 

4. Job1 : Pull  the Github repo automatically when some developers push repo to Github.

5. Job2 : By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed interpreter install image container to deploy code  and start training( eg. If code uses CNN, then Jenkins should start the container that has already installed all the softwares required for the cnn processing).

6. Job3 : Train your model and predict accuracy or metrics.

7. Job4 : if metrics accuracy is less than 95%  , then tweak the machine learning model architecture.

8. Job5: Retrain the model or notify that the best model is being created

9. Create One extra job job6 for monitor : If container where app is running. fails due to any reason then this job should automatically start the container again from where the last trained model left.

For the required container images:-
```
# docker build -t  username/image:tag  .  
```
Now Create jobs for building job chaining.
### Solutions for above tasks:-

### Job1
For github-webhooks's payload url, use ngrok or any other tunneling to create a tunnel which gives you a random public url binded through a publicIP behind the scene.
```
# ./ngrok http 8080
```
![ngrok](/images/ngrok.png)
Then go to your repo->settings->Webhooks.
![github-webhook](/images/github-webhook.png)
Jenkins job1
![Job1.1](/images/j1.1.png)
![Job1.2](/images/j1.2.png)

### Job2
This job will either trigger when the container is not launched then it will launch or it will be triggered when job1 will be built successfully.

![Job2.1](/images/j2.1.png)
![Job2.2](/images/j2.2.png)

### Job3
This job will be triggered when the job2 will be built successfully. This job trains the model for the first time and checks whether the accuracy of the model is greater than 95% or not. If it is greater than 95 % then it will save the model at the mounted location.

![Job3.1](/images/j3.1.png)
![Job3.2](/images/j3.2.png)

### Job4
This job will be triggered when the job3 will be built successfully. This job checks whether the accuracy of the model is greater than 95% or not. If it is greater than 95 % then it will do nothing otherwise it will run another training of the model for tuning and tweaking with the hyper-parameters of the model to make the accuracy of the model >95.

![Job4.1](/images/j4.1.png)
![Job4.2](/images/j4.2.png)

### Job5
This job will be triggered when the job4 will be built successfully. This job checks whether the accuracy of the model is greater than 95% or not after tweaking the model. If it is greater than 95 % then it will do notify and send a mail otherwise it will do nothing.

![Job5.1](/images/j5.1.png)
![Job5.2](/images/j5.2.png)

### Job6
This job will be triggered using PollSCM as it works on the crontab features that are fitted to it. It will check as the container is stopped then relaunch it by triggering job2 otherwise do nothing.

![Job6.1](/images/j6.1.png)
![Job6.2](/images/j6.2.png)
