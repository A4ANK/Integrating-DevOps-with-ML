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
![github-webhook](/images/github-webhook.png)

Then go to your repo->settings->Webhooks.
![Job1.1](/images/j1.1.png)
![Job1.2](/images/j1.2.png)

### Job2

![Job2.1](/images/j2.1.png)
![Job2.2](/images/j2.2.png)

### Job3

![Job3.1](/images/j3.1.png)
![Job3.2](/images/j3.2.png)

### Job4

![Job4.1](/images/j4.1.png)
![Job4.2](/images/j4.2.png)

### Job5

![Job5.1](/images/j5.1.png)
![Job5.2](/images/j5.2.png)

### Job6

![Job6.1](/images/j6.1.png)
![Job6.2](/images/j6.2.png)