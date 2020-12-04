from imageai.Prediction import ImagePrediction
import os
execution_path = os.getcwd()

prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(os.path.dirname(__file__) + '/model/resnet50_weights_tf_dim_ordering_tf_kernels.h5'))
prediction.loadModel()

predictions, probabilities = prediction.predictImage(os.path.join(os.path.dirname(__file__) + '/image/anime.jpg'), result_count=5 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction + " : " + eachProbability)


