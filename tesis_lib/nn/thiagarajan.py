from keras.models import Sequential

from keras.layers import BatchNormalization
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Activation
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers import Dense

from keras.regularizers import L2
from keras import backend as K

class Thiagarajan:
    @staticmethod
    def build(width: int, height: int, depth:int, classes:int):
        model = Sequential()
        inputShape = (height, width, depth)
        chanDim = -1

        if K.image_data_format() ==  "channels_first":
            inputShape = (depth, height, width)
            chanDim = 1
        
        # capa 1
        model.add(Conv2D(
            filters=32,
            kernel_size=(3,3),
            input_shape=inputShape,
            padding= 'same'
        ))
        model.add(Activation('relu'))
        model.add(BatchNormalization(
            axis=chanDim
        ))
        model.add(MaxPooling2D(
            pool_size=(4,4),
            strides=(3,3)
        ))
        model.add(Dropout(0.5))

        # capa 2
        model.add(Conv2D(
            filters=64,
            kernel_size=(3,3),
            padding= 'same'
        ))
        model.add(Activation('relu'))
        model.add(BatchNormalization(
            axis=chanDim
        ))
        model.add(MaxPooling2D(
            pool_size=(3,3),
            strides=(2,2)
        ))
        model.add(Dropout(0.5))
        
        # capa 3
        model.add(Conv2D(
            filters=128,
            kernel_size=(3,3),
            padding= 'same'
        ))
        model.add(Activation('relu'))
        model.add(BatchNormalization(
            axis=chanDim
        ))
        model.add(Conv2D(
            filters=128,
            kernel_size=(3,3),
            padding= 'same'
        ))
        model.add(Activation('relu'))
        model.add(BatchNormalization(
            axis=chanDim
        ))
        model.add(MaxPooling2D(
            pool_size=(2,2),
            strides=(2,2)
        ))
        model.add(Dropout(0.5))

        # capa 4
        model.add(Flatten())
        model.add(Dense(1024))
        model.add(Activation('relu'))
        model.add(BatchNormalization(
            axis=chanDim
        ))
        model.add(Dropout(0.5))
        model.add(Dense(classes))
        model.add(Activation('softmax'))

        return model
        