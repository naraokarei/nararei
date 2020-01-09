import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential,Model,load_model
from PIL import Image
import sys

#パラメータの初期化
classes = ["ferrari","lamborghini"]
num_classes = len(classes)
image_size=250

#引数から画像ファイルを参照して読み込む
image = Image.open(sys.argv[1])
image = image.convert("RGB")
image = image.resize((image_size,image_size))
data = np.asarray(image) / 255.0#0~255の値を0~1に変換
X = []
X.append(data)
X = np.array(X)

#モデルのロード
model = load_model('./vgg16_supercar.h5')

result = model.predict([X])[0]#1こめの推定結果
predicted = result.argmax()
percentage = int(result[predicted]*100)

print(classes[predicted], percentage)
        




