# Identification of Medicinal Plant by using Deep Learning

This project leverages **Machine Learning**, **Deep Learning** and **Image Processing** techniques to develop a reliable system for identifying medicinal plants by analyzing leaf images. Using **pre-trained models** like VGG-16, ResNet-50, and YOLOv8, it offers an accessible solution via a web application to address challenges in plant identification, particularly in rural and remote areas. And give the correct information about the plant which is **Ayurvedically Correct**.

## Key Features
- **Custom Dataset:** A curated collection of 17,000 leaf images representing 22 plant species for accurate model training.
- **Pre-trained Models:** Implemented CNN-based models optimized for high precision in plant recognition.
- **Web Application:** A user-friendly platform for easy plant identification and detailed species information from proper Ayurvedic Books.

## Objective
To provide a dependable, efficient, and accessible tool for recognizing medicinal plants, ensuring authenticity and supporting Ayurvedic medicine practices and other peoples (Chemist, Scientists, Students, nature lovers, etc).

---

# Dataset Collection

This dataset consists of **17,000 images**, and after applying data augmentation, **80,000 images** were generated. Due to computational limitations, **20,000 images** were used for training. The dataset includes **22 categories** of medicinal plants as listed below:

- Adulsa  
- Aloe Vera  
- Amla  
- Banana  
- Betel Leaf (Pan)  
- Brahmi  
- Curry Leaves  
- Drumstick  
- Eranda  
- Gokarna  
- Hibiscus  
- Jamun (Indian Blackberry)  
- Mango  
- Neem  
- Onion  
- Panfuti  
- Papaya  
- Satyanashi  
- Shatavari  
- Sugarcane  
- Tandulja  
- Touch Me Not  

### Image Specifications
- **Image Size:** Resized to `224 x 224` pixels.  
- **Augmentation Techniques:**
  1. Rotation  
  2. Zoom In/Out  
  3. Brightness Range  
  4. Rescale  

### Dataset Creation
This dataset was not sourced from any external platform but was entirely created by a team of 4 members from **Shirwal** and **college**. To upload the dataset to Google Colab, the **Roboflow platform** was utilized.

---

### Below is the Dataset Details
![Dataset Details](01-Database%20Detail.png)




