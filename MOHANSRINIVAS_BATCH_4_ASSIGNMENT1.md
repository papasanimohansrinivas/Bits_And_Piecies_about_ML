## Name is  :m::o:H:a:N SRINI:v::a:S  From  B:a:tch  4

#### My  TOPICS : 

#  Kernel/Filters :

##### kernels help to detect some features that are present in the image
![](https://adeshpande3.github.io/assets/Filter.png)


##### convolving a kernel with a image gives a high value if feature that kernel represents is init like below.

![](https://adeshpande3.github.io/assets/FirstPixelMulitiplication.png)

##### if kernel doesn't match very well with the input 
##### then 

![](https://adeshpande3.github.io/assets/SecondMultiplication.png)

# <sub>1</sub>  X <sub>1</sub> Convolution

##### 1X1 convolution can't be explained with out a image.

![alt text](http://ashukumar27.io/assets/neuralnets/1x1.png)

##### Above is a 6 * 6 2 dimension image with 32 channels 

##### if you look blue block from top down not left to right. 
##### we multiply 6*6  with  1 *1 for 32 layers and we have
##### 6*6  32 layers as output and in computer vision we just add them ===> 6 *6 *1.

# Feature Maps

#### when a kernel is applied to all parts of image then we will have a 2 dimension map of where in  that image is our selected features are highlighted i.e yields high values.

#### this is called a feature map

# Creating Github Account And Uploading a project 

#### * i am assuming u are u a private individual
##### first fill the username and email address and fill the password of your choice.

![](https://i.imgur.com/Laqqfvl.png)

##### second there are two options  i think it's best to choose private if you don't want to others to view or fork or clone  your repository  (that's my opinion.) Then click create account.
![](https://www.wikihow.com/images/2/20/Join-github-4.jpg)

##### I came to know from wikihow page that there is a option to fill the quiz or skip it.

![](https://www.wikihow.com/images/thumb/8/88/Join-github-5.jpg/664px-Join-github-5.jpg.webp)

##### later your github account is created .

##### now login into your new repository .in dashboard you will see a + sign then click on it .

![](https://i.stack.imgur.com/WWTOi.png)

##### now you will see a page like below 
##### choose appropriate name with out spaces and choose option of initialising with repo with readme.

![](https://i.stack.imgur.com/4I9ij.png)

##### now after repo is initialised you have actaully 3 options to upload a project 

##### first one is to do it with UI
##### second is to do it with git bash from cmd
##### i will show from command line.

##### cd into your project dir.
##### then do git init from cmd it will create .git repo (linux/Windows)
##### ==> git init
##### then if we want to add all files then do 
##### ==> git add . or git add  < filename >
##### ==> git commit -m "< message >"
##### finally do 
##### git push -f https://< urname >:< password >@ github.com/< username >/< reponame >.git master
##### above command if it is first time repository.
##### else do
##### git checkout branch < branch name >
##### then 
##### git push -f https://< urname >:< password >@ github.com/< username >/< reponame >.git < branch name >