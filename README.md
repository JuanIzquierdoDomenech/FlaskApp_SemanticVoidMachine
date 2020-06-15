# FlaskApp_SemanticVoidMachine
This project is a Flask App that loads Keras models to both predict and classify values from the void machine we're working on

It also includes script utilities to convert from .h5 to saved model format (.pb) in order to convert it to .onnx format

### Based on
[FlaskApp_LoadKerasModel_TeachableMachine](https://github.com/JuanIzquierdoDomenech/FlaskApp_LoadKerasModel_TeachableMachine)

## Installation
1. Pull the code
2. Create a Python environment and activate it

*e.g.* 
`virtualenv -p python3 .venv`
`source .venv/bin/activate`

3. Install requirements

*e.g.*
`pip install -r requirements.txt`

4. Run the server

*e.g.*
`python server.py`

## Conversion to .onnx format

This tool has been used to convert the Keras model (.h5) to Barracuda (.onnx)

[tensorflow-onnx](https://github.com/onnx/tensorflow-onnx)

Take into account the `onnx` version specified in `requirements.txt`, since installing `tf2onnx` installs the latest version, but I use 1.6.0 of `onnx` instead (just uninstall and install with `pip`)

*e.g.* You can find the .onnx files for a model in models/classification/engine_button/saved_model
where both the .pb and .onnx files are stored.

#### First of all, you have to convert the **.h5** file to **.pb**

To do that, you can use the script `convert_model_to_pb.py` in the *models/* folder.

*e.g.* `python convert_model_to_pb.py classification/engine_button/model.h5 classification/engine_button/`

#### Then, you have to convert the **.pb** to **.onnx**

You can use the following command:

`python -m tf2onnx.convert --opset 10 --fold_const --saved-model classification/engine_button/saved_model --output classification/engine_button/saved_model/classification_engine_button.onnx`

## Done
- The models predicts the on/off state (classification) of the engine button

## TODO
- Training and loading the model to read void value needle (regression)
