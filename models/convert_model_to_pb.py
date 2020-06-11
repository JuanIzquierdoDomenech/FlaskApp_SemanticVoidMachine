# https://medium.com/@aneeshpanoli/how-to-use-a-pre-trained-tensorflow-keras-models-with-unity-ml-agents-bee9933ce3c1
# https://github.com/llSourcell/Unity_ML_Agents/blob/master/docs/Using-TensorFlow-Sharp-in-Unity-(Experimental).md

# usage
# python convert_model_to_pb.py model_name.h5

import sys

import tensorflow
from tensorflow.python.saved_model import builder as pb_builder

model = tensorflow.keras.models.load_model(sys.argv[1], compile=False)
tensorflow.keras.backend.set_learning_phase(0)

builder = pb_builder.SavedModelBuilder('pb/')
builder.save()