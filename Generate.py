import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import os
import tensorflow as tf
from tensorflow import keras
from keras.layers import (Dropout, Input, Dense, Conv2D, 
                          MaxPooling2D, GlobalAveragePooling2D, 
                          UpSampling2D, Conv2DTranspose, 
                          Reshape, Flatten, Activation, 
                          BatchNormalization)
from keras.models import Model, Sequential
from keras.preprocessing import image
from keras.layers import LeakyReLU
from keras.initializers import RandomNormal
from keras.optimizers import Adam
import os
import cv2
from PIL import Image
#from extra_keras_datasets import emnist
from keras.utils import np_utils


for filename in os.listdir("Generated"):
    os.remove("Generated/"+filename)


# Folder path containing the images
# folder_path = "Correct_Images"
# d=[]
# # Iterate over all files in the folder
# for filename in os.listdir(folder_path):


#     # Check if the file is an image
#     if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
#         # Construct the full file path
#         file_path = os.path.join(folder_path, filename)
        
#         # Open the image using PIL
#         image = Image.open(file_path)
        
#         # Perform operations on the image (e.g., display, process, etc.)
#         # ...
#         d.append([image])
        
#         # Close the image
#         image.close()



# data = pd.read_csv("data/A_Z Handwritten Data.csv").astype('float32')
# data.head()

width, height, channel = 28, 28, 1
# # d = d.reshape((len(os.listdir(folder_path)), width, height))
# X = data.iloc[:,1:].values
# X = X.reshape((372450, width, height))
# np.random.shuffle(X)
# print(X.shape)
# X = (X - 127.5) / 127.5


def show_data(X, title=""):
    plt.figure(figsize=(11,11))
    
    i = 1
    for img in X:
        plt.subplot(10, 10, i)
        plt.imshow(img.reshape((height, width)), cmap='gray')
        plt.axis('off')
        i+=1
        if i>100: break

    plt.suptitle(title, fontsize = 25)
    plt.show()
    
# show_data(X, title="Original Alphabets")


gen_optimizer = Adam(0.0001, 0.5)
disc_optimizer = Adam(0.0002, 0.5)
noise_dim = 100


def buildGenerator():
    model = Sequential()

    model.add(Dense(1024, input_dim=noise_dim))
    model.add(BatchNormalization(momentum=0.8))
    model.add(Activation("relu"))
    
    model.add(Dense(6272, input_dim=noise_dim))
    model.add(BatchNormalization(momentum=0.8))
    model.add(Activation("relu"))
    
    model.add(Reshape((7, 7, 128)))
    
    model.add(UpSampling2D((2, 2)))
    model.add(Conv2D(64, (2, 2), padding='same', 
                     kernel_initializer=RandomNormal(0, 0.02)))
    model.add(BatchNormalization(momentum=0.8))
    model.add(LeakyReLU(0.2))
    
    model.add(UpSampling2D((2, 2)))
    model.add(Conv2D(channel, (3, 3), padding='same', activation = "tanh", 
                     kernel_initializer=RandomNormal(0, 0.02)))
    
    return model

def buildDiscriminator():
    model = Sequential()
    
    model.add(Conv2D(64, (5, 5), strides=2, padding='same', 
                     kernel_initializer=RandomNormal(0, 0.02), 
                     input_shape=(width, height, channel)))
    model.add(LeakyReLU(0.2))
    
    model.add(Conv2D(128, (5, 5), strides=2, 
                     kernel_initializer=RandomNormal(0, 0.02)))
    model.add(LeakyReLU(0.2))
    
    model.add(Flatten())
    
    model.add(Dense(256))
    model.add(LeakyReLU(0.2))
    
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='sigmoid'))
    
    model.compile(loss='binary_crossentropy', optimizer=disc_optimizer)
    return model

# generator=keras.models.load_model("GAN/generator.ckpt")
# #generator=buildGenerator()
# generator.summary()

# discriminator =keras.models.load_model("GAN/discriminator.ckpt")
# #discriminator=buildDiscriminator()
# discriminator.summary()

# noise = Input(shape=(noise_dim,))
# fake_data = generator(noise)
# discriminator.trainable = False
# output = discriminator(fake_data)
# # gan = Model(noise, output)
# # gan.compile(loss='binary_crossentropy', optimizer=gen_optimizer)
# gan=keras.models.load_model("GAN/gan.ckpt")
# gan.summary()

fixed_noise = np.random.normal(0, 1, size=(300000, noise_dim))

def show_generated_alphabets(title, epoch):
    generator=keras.models.load_model("GAN/generator.ckpt")
    imgs = generator.predict(fixed_noise)
    imgs = 0.5 * imgs + 0.5
    plt.figure(figsize=(11,11))
    
    i = 1
    for img in imgs:
        plt.subplot(10, 10, i)
        plt.imshow(img.reshape((height,width)), cmap='gray')
        plt.axis('off')
        i+=1
    plt.suptitle(title, fontsize = 25)
    plt.savefig(str(epoch)+".png", transparent=True)
    plt.show()

# epochs = 51
# batch_size = 128
# steps_per_epoch = len(X)//batch_size


# for epoch in range(epochs):
#    t = time.localtime()
#    current_time = time.strftime("%H:%M:%S", t)
#    print(f"##################epoch:{epoch}  time:{current_time}#######################")
#    for batch in range(steps_per_epoch):
#        input_gen = np.random.normal(0, 1, size=(batch_size, noise_dim))
#        fake_data = generator.predict(input_gen)

#        real_data = X[np.random.randint(0, X.shape[0], size=batch_size)]
#        real_data = real_data.reshape((batch_size, width, height, channel))

#        input_disc = np.concatenate((real_data, fake_data))

#        label_disc = np.zeros(2*batch_size)
#        label_disc[:batch_size] = 0.9
#        label_disc[batch_size:] = 0.1
#        loss_disc = discriminator.train_on_batch(input_disc, label_disc)

#        label_gen = np.ones(batch_size)
#        loss_gen = gan.train_on_batch(input_gen, label_gen)

#    print("epoch: ", epoch)
#    print("discriminator loss: ", loss_disc)
#    print("generator loss: ", loss_gen)
#    print("-"*80)

#    if (epoch) % 5 == 0:
#        discriminator.save('GAN/discriminator.ckpt')
#        generator.save('GAN/generator.ckpt')
#        gan.save('GAN/gan.ckpt')
#        show_generated_alphabets("Generated Alphabets",epoch)


def generate():
    generator=keras.models.load_model("GAN/generator.ckpt")
    imgs = generator.predict(fixed_noise)
    imgs = 0.5 * imgs + 0.5
    i=0
    for img in imgs:
        result = cv2.normalize(img, dst=None, alpha=0, beta=255,norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        cv2.imwrite(f'Generated/img_{i}.png', result)
        i+=1
# show_generated_alphabets("Generated Alphabets",1) 
#generate()


