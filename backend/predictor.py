# import numpy as np
# import tensorflow as tf

# from classes import CLASS_NAMES

# model = tf.keras.models.load_model(
#     "model/equipment_classifier.h5"
# )

# def predict_equipment(image_path):

#     img = tf.keras.utils.load_img(
#         image_path,
#         target_size=(224,224)
#     )

#     img = tf.keras.utils.img_to_array(img)

#     img = np.expand_dims(img, axis=0)

#     prediction = model.predict(img)

#     idx = np.argmax(prediction)

#     confidence = float(np.max(prediction))

#     return CLASS_NAMES[idx], confidence




import numpy as np
import tensorflow as tf

CLASS_NAMES = [
    "C301",
    "M201",
    "P101",
    "P102"
]

model = tf.keras.models.load_model(
    "model/equipment_classifier.h5"
)


def predict_equipment(image_path):

    img = tf.keras.utils.load_img(
        image_path,
        target_size=(224, 224)
    )

    img = tf.keras.utils.img_to_array(img)

    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img, verbose=0)

    idx = np.argmax(prediction)

    confidence = float(np.max(prediction))

    return CLASS_NAMES[idx], confidence