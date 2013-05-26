# Google Translate Demo
By <victor.yiliangzhou@gmail.com></code>

Utilize google translate to read text for you in English or Chinese.

## Prerequsites
Platform: Ubuntu 12.04 LTS
Language: Python 2.7.3
External python module: python-pygame, check [this link](http://www.pygame.org/docs/ref/music.html) for a reference.

## How to use it
Assume you have meet all the platform prerequsites as stated before, you can try out this demo by following two steps:
+ Open your shell
+ `$ python speak.py`
or
+ `$ python speak.py -l zh-CN`

the first one will read English for you, the second one will read Chinese for you.

for example, the following output are given when I test on my own machine:
    $ python speak.py
    To speak: let us make some noise.
    To speak: bala bala bala baaaaaaaaaalaaaaaaaaaaaaaaa.
    To speak: haaaaaaaaaa.
    To speak: ha.
    To speak: this sounds cool.
    To speak:

Program exits when you have entered nothing, an empty string.

Have fun!!!
