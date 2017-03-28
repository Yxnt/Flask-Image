Flask-Image
====

简介
----

动态处理jpg、jpeg、png图片，支持压缩、高宽设置、等比例压缩操作，跳过10k以下的文件


使用说明
----

|参数|说明|例子|
|----|----|----|
|`w`|设置图片宽度|http://127.0.0.1:5000/e93dc940635f469dafeb41f5fe49676c.jpg?w=1000
|`h`|设置图片高度|http://127.0.0.1:5000/e93dc940635f469dafeb41f5fe49676c.jpg?h=1000
|`q`|设置图片质量 |http://127.0.0.1:5000/e93dc940635f469dafeb41f5fe49676c.jpg?q=10
|`p`|等比例压缩图片|http://127.0.0.1:5000/e93dc940635f469dafeb41f5fe49676c.jpg?p=75

默认打开图片时，图片的质量为50。

p参数的结果是以当前图片的宽高为基准数×提供的百分比所得到的图片宽和高（图片宽高各为100p的值为75，那么最终生成出来的图片宽高为75*75）

**当P参数存在时w和h无效**


使用方式
----

首先确保python 是3.5以上的
```
git clone https://github.com/Yxnt/Flask-Image.git
cd Flask-Image
virtualenv venv
source venv/bin/active && pip install -r requirements.txt
mkdir img
./start.sh
```

上传文件到img目录中，根据使用说明中的进行测试