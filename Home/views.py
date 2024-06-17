from django.shortcuts import render
from django.http import HttpResponseRedirect , HttpResponse
# Create your views here.
from django.views import View
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as keras_image
import os,tempfile
from PIL import Image
from django.http import JsonResponse
import cv2
import tensorflow as tf
import numpy as np


# from ..cancerproject.settings import BASE_DIR  




# h5_path = "./static/test.h5"

# model = load_model(model_path)



def home(request):
    
    return render(request, 'Home/index.html')



<<<<<<< HEAD

=======
>>>>>>> 90db5ac (result page updated)
def upload_image(request):
    if request.method == 'POST':
        # H5 dosyasının yolu
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        static_path = os.path.join(BASE_DIR, 'static')
        h5_file_path = os.path.join(static_path, 'test.h5')
        
        try:
            # Modeli yükle
            model = load_model(h5_file_path)
            
            # POST isteğinden resmi alın
            image_file = request.FILES.get('image')
            
            if image_file:
                try:
                    # Resmi PIL formatına dönüştürün
                    img = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), -1)
                    
                    # Resmi yeniden boyutlandırın
<<<<<<< HEAD
                    resize = tf.image.resize(img, (256,256))
                    
                    # Resmi modelin beklentilerine uygun hale getirin
                    # (örneğin, normalizasyon yapın)
                    image_array = np.expand_dims(resize/255, 0)
                    
                    # Tahmin yapın
                    prediction = model.predict(image_array)
                    
                    # Tahminleri JSON formatında döndürün
                    if prediction > 0.5: 
                        print(f'Belirlenen sınıf kötü huylu')
                        # return JsonResponse({'prediction': prediction.tolist() , "deneme":"kötü huylu" })
                        context = {'prediction': prediction,"result":"Kötü Huylu" }
                    
                        # Template ile birlikte context'i render edin ve HttpResponse döndürün
                        return render(request, 'Home/result.html', context)


                    else:
                        context = {'prediction': prediction,"result":"İyi Huylu" }
=======
                    resized_img = cv2.resize(img, (256, 256))
                    
                    # Resmi modelin beklentilerine uygun hale getirin
                    image_array = np.expand_dims(resized_img / 255.0, axis=0)
                    
                    # Tahmin yapın
                    predictions = model.predict(image_array)
                    
                    # En yüksek olasılıklı sınıfı bulun
                    predicted_class_index = np.argmax(predictions)
                    predicted_class_label = class_labels[predicted_class_index]
                    predicted_confidence = predictions[0][predicted_class_index]
                    
                    class_labels_and_predictions = list(zip(class_labels, predictions[0]))
>>>>>>> 90db5ac (result page updated)
                    
                        # Template ile birlikte context'i render edin ve HttpResponse döndürün
                        return render(request, 'Home/result.html', context)

                    # return JsonResponse({'prediction': prediction.tolist()})
                
                except Exception as e:
                    return JsonResponse({'error': str(e)}, status=400)
                
            else:
                return JsonResponse({'error': 'No image found in the request'}, status=400)
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
    else:
        return render(request, 'Home/test.html')
    




# def upload_image(request):
#     if request.method == 'POST':
#         # H5 dosyalarının yolu
#         BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#         static_path = os.path.join(BASE_DIR, 'static')

#         # POST isteğinden kanser türünü ve resmi alın
#         cancer_type = request.POST.get('cancer_type')
#         image_file = request.FILES.get('image')

#         # Kanser türüne göre model dosyasını belirleyin
#         model_file_map = {
#             'Brain': 'brain.h5',
#             'Breast': 'breast.h5',
#             'Kidney': 'kidney.h5',
#             # Daha fazla kanser türü ekleyebilirsiniz
#         }

#         # Modelde kullanılan sınıf etiketlerini belirleyin
#         class_labels_map = {
#             'Brain': ['brain_glioma', 'brain_menin', 'brain_tumor'],
#             'Breast': ['breast_benign', 'breast_malignant'],
#             'Kidney': ['kidney_normal', 'kidney_tumor'],
#         }

#         if cancer_type not in model_file_map:
#             return JsonResponse({'error': 'Invalid cancer type provided'}, status=400)

#         h5_file_path = os.path.join(static_path, model_file_map[cancer_type])
#         class_labels = class_labels_map.get(cancer_type, [])
#         print(type(class_labels))
#         try:
#             # Modeli yükle
#             model = load_model(h5_file_path)
            
#             if image_file:
#                 try:
#                     # Resmi PIL formatına dönüştürün
#                     img = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), -1)
                    
#                     # Resmi yeniden boyutlandırın
#                     resize = tf.image.resize(img, (256, 256))
                    
#                     # Resmi modelin beklentilerine uygun hale getirin
#                     image_array = np.expand_dims(resize / 255.0, axis=0)
                    
#                     # Tahmin yapın
#                     predictions = model.predict(image_array)[0]
                    
#                     # En yüksek olasılıklı sınıfı bulun
#                     predicted_class = np.argmax(predictions)
#                     predicted_class_label = class_labels[predicted_class]
#                     predicted_confidence = predictions[predicted_class]
                    
#                     class_labels_and_predictions = list(zip(class_labels, predictions))
                    
#                     context = {
#                         'predicted_class_label': predicted_class_label,
#                         'predicted_confidence': predicted_confidence,
#                         'class_labels_and_predictions': class_labels_and_predictions
#                     }
                    
#                     # Template ile birlikte context'i render edin ve HttpResponse döndürün
#                     return render(request, 'Home/result.html', context)
                
#                 except Exception as e:
#                     return JsonResponse({'error': str(e)}, status=400)
                
#             else:
#                 return JsonResponse({'error': 'No image found in the request'}, status=400)
            
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
        
#     else:
#         return render(request, 'Home/test.html')





# Modeli Yükleme

# def upload_image(request):
#     # H5 dosyasının yolu
#     BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#     static_path = os.path.join(BASE_DIR, 'static')
#     h5_file_path = os.path.join(static_path, 'test.h5')
    
#     # Modeli yükle
#     model = load_model(h5_file_path)

#     if request.method == 'POST' and request.FILES:
#         # Yüklenen resmi al
#         uploaded_image = request.FILES['image']
#         img = keras_image.load_img(uploaded_image, target_size=(256, 256))
#         img_array = keras_image.img_to_array(img)
#         img_array = img_array / 255.0  # Normalizasyon
#         img_array = img_array.reshape((1,) + img_array.shape)
#         # Sınıflandırma yap
#         prediction = model.predict(img_array)

#         # Sınıf tahminini değerlendir
#         if prediction > 0.5:
#             result = "Kötü Huylu"
#         else:
#             result = "İyi Huylu"

#         # Sonucu göster
#         return HttpResponse( result)
#     else:
#         return render(request, 'Home/test.html')




# def upload_image(request):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    static_path = os.path.join(BASE_DIR, 'static')
    h5_file_path = os.path.join(static_path, 'test.h5')
    # print(h5_file_path)
    model = load_model(h5_file_path)

    if request.method == 'POST' and request.FILES:
        uploaded_image = request.FILES['image']

        img = keras_image.load_img(uploaded_image, target_size=(256, 256))
        img_array = keras_image.img_to_array(img)
        img_array = img_array / 255.0  # Normalizasyon
        img_array = img_array.reshape((1,) + img_array.shape)


        image= request.FILES['image']

        
        # Sınıflandırma Yapma
        prediction = classify_image(image,model)
        if prediction > 0.5:
            result = "Kötü Huylu"
        else:
            result = "İyi Huylu"
        return render(request, 'result.html', {'result': result})
    else:
        return render(request, 'Home/test.html')
    


def process_image(image_path,image):
    img = image.load_img(image_path, target_size=(256, 256))
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0  # Normalization
    img_array = img_array.reshape((1,) + img_array.shape)  # Reshape for model input
    return img_array

def classify_image(image_file,model):
    processed_image = process_image(image_file)
    prediction = model.predict(processed_image)
    return prediction

