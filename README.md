
# Working 😁👍✔
 - first we need an image file 
 - then we will check image size ratio by funtion - check_image_size_ratio
 - then we compress the image according to our github size
	- which will chisle the image (make image for compression)
	- compress image by a dimention ex- make a sqaure and place more as possible all over the image amd take average of every pixle inside it and make a single pixle of that square {the chisleing is to make image fit squares properly}
	- return dimention and compressed image

 - then we get (git_im) amd (compressed image) with git commit colors for respresentation
	- [git_im] which get numbres of commits for each pixle which is take action daily 

 - save results in a folder server-files
	- results will save as image of git image 
	- git_commit_file_for_server

### github commits colours in RGB and hash colors 
🐇🐸🐲🐍🦎

```sh
commit_colours = [
[255,255,255], # #ffffff
[155,233,168], # #9be9a8
[64,196,99],   # #40c463
[48,161,78],   # #30a14e
[33,110,57]    # #216e39
]
```


### To RUN the files  🎈🥈🥉🏆
**first change dir**
```
cd <folder name>
```
**python runner.py `file-name with path>`**
```sh 
python runner.py img/6.png 
```
example results

<img src='https://github.com/rishabhjainfinal/git-commit-drawing/blob/master/ss/6.png?raw=true'>

<img src='https://github.com/rishabhjainfinal/git-commit-drawing/blob/master/ss/64801rishi.png?raw=true' >




### to Run the GUI of the program  🤵 
**first change dir**
```
cd <folder name>
```
** you can use the commend to start Drawing 
this will help you to create image like drawing canvas after drawing our image save it **
```
python gui.py
```

<img src='https://github.com/rishabhjainfinal/git-commit-drawing/blob/master/ss/Screenshot%20(7).png?raw=true' >

## server work after creating the files 😎(⌐■_■) 
** after saving or running files results will save in `server-files` folder **
### *just drop this folder on your server *
**after downloading the files in server **
```
cd server-files 
```
**run file in background so it will not killed or terminated after you close ssh**
```
nohup python server-commits.py
```
**[read more about nohub here link to a article ](https://janakiev.com/blog/python-background/)**

### In some days your cool github drawing will apear in your [git contributions chart]  

---
I am also providing `reserch2.txt` cointain most of the data of finding of this project  
.
