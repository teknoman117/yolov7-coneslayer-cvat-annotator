import io
import base64
import json

import cv2
import numpy as np
import yolov7

def init_context(context):
    model = yolov7.load('coneslayer-redux.pt')
    model.conf = 0.54
    model.iou = 0.5

    context.user_data.model_handler = model
    context.logger.info('coneslayer initialized')

def handler(context, event):
    context.logger.info('run coneslayer')
    data = event.body
    image_buffer = io.BytesIO(base64.b64decode(data['image']))
    image = cv2.imdecode(np.frombuffer(image_buffer.getvalue(), np.uint8), cv2.IMREAD_COLOR)
    image = image[:,:,::-1]
   
    results = context.user_data.model_handler(image)
    result = results.pred[0]

    boxes = result[:, :4]
    confs = result[:, 4]
    clss = result[:, 5]
    class_name = results.names

    detections = []
    for box, conf, cls in zip(boxes, confs, clss):
        label = class_name[int(cls)]
        detections.append({
            'confidence': str(float(conf)),
            'label': label,
            'points': box.tolist(),
            'type': 'rectangle'
        })

    return context.Response(body=json.dumps(detections), headers={},
        content_type='application/json', status_code=200)
