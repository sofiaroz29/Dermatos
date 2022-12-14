import numpy as np
import tensorflow
from tensorflow.keras.preprocessing import image
from keras.applications.resnet import preprocess_input
from PIL import Image



def receive_resize_img(imgPath):    
    img = image.load_img(imgPath, target_size=(224,224))
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    img_preprocessed = preprocess_input(img_batch)
    return img_preprocessed


def predict_img(img):
  loaded_model = tensorflow.keras.models.load_model('model.h5')
  resultado = loaded_model.predict(img)
  predicted_class= (resultado > 0.5).astype("int32")
  
  # print('Outputs shape')    
  # print(resultado.shape) # prints (n,1) but  need (n,)
  # resultado=np.transpose(resultado)[0]  # transformation to get (n,)
  # print(resultado.shape)  # now the shape is (n,)
  # # Applying transformation to get binary values predictions with 0.5 as thresold
  print(resultado)
  #resultado = list(map(lambda x: 0 if x<0.5 else 1, resultado))
  #res = resultado[0]
  #res_list = resultado.tolist()
  #print(res_list)
  res_string = np.array_str(resultado)
  firstDigitRes = res_string[2]
  #print(firstDigitRes)

 #print("----RESULTADO-----")
  #print(resultado)

  #print("----CLASS-----")
  #if resultado[0] == 0:
   # print ("maligno")
  #else:
  #  print("benigno")  
  #print([np.argmax(resultado)])

  #return res_string

  r = " "

  if firstDigitRes == "0":
    r = "maligno"
  else:
    r = "benigno"

  return r 
  #return firstDigitRes

#receive_resize_img
#predict_img(img_preprocessed)