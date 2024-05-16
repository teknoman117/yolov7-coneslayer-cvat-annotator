Coneslayer Automatic Annotater for CVAT
=======================================
An automatic annotator based on Coneslayer (https://github.com/mkrupczak3/Coneslayer) for CVAT to aid in labelling traffic cones for robotics projects

Installation 
------------
```
# From the CVAT checkout directory
pushd serverless/pytorch
git clone https://github.com/teknoman117/yolov7-coneslayer-cvat-annotator
popd

# Deploy the annotator
serverless/deploy_cpu.sh serverless/pytorch/yolov7-coneslayer-cvat-annotator
```

Demonstration
-------------
![Demo](/assets/screenshot.png)
