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

### Below is the Dataset Details (01-Dataset Detail.png)
![Dataset Details](01-Dataset%20Detail.png)

# Sample Dataset

Below are sample images from the dataset, representing 22 categories of medicinal plants:

<div style="display: flex; flex-wrap: wrap; justify-content: space-around;">

  <!-- Row 1 -->
  <img src="02-Sample Dataset/Adulsa/Adulsa/20241105_151710.jpg" alt="Adulsa" width="200" height="200" style="margin: 10px; object-fit: cover;">
  <img src="02-Sample Dataset/Adulsa/Alovera/20241106_130132.jpg" alt="Aloe Vera" width="200" height="200" style="margin: 10px; object-fit: cover;">
  <img src="02-Sample Dataset/Adulsa/Amla/20241104_164119.jpg" alt="Amla" width="200" height="200" style="margin: 10px; object-fit: cover;">
  <img src="02-Sample Dataset/Adulsa/Banana/20241105_144735.jpg" alt="Banana" width="200" height="200" style="margin: 10px; object-fit: cover;">

  <!-- Row 2 -->
  <img src="02-Sample Dataset/Adulsa/Beetal Leaf (Pan)/20241012_173519 (1).jpg" alt="Betel Leaf (Pan)" width="200" height="200" style="margin: 10px; object-fit: cover;">
  <img src="02-Sample Dataset/Adulsa/Bramhi/20241023_163346.jpg" alt="Brahmi" width="200" height="200" style="margin: 10px; object-fit: cover;">
  <img src="02-Sample Dataset/Adulsa/Curry Leaves/20241012_174204.jpg" alt="Curry Leaves" width="200" height="200" style="margin: 10px; object-fit: cover;">
  <img src="02-Sample Dataset/Adulsa/Drumstick/20241104_140151.jpg" alt="Drumstick" width="200" height="200" style="margin: 10px; object-fit: cover;">

  <!-- Row 3 -->
  <img src="02-Sample Dataset/Adulsa/Eranda/20241105_135709.jpg" alt="Eranda" width="200" height="200" style="margin: 10px; object-fit: cover;">
  <img src="02-Sample Dataset/Adulsa/Gokurna/20241023_155619.jpg" alt="Gokarna" width="200" height="200" style="margin: 10px; object-fit: cover;">
  <img src="02-Sample Dataset/Adulsa/HIbiscus/20241023_155917.jpg" alt="Hibiscus" width="200" height="200" style="margin: 10px; object-fit: cover;">
  <img src="02-Sample Dataset/Adulsa/Jamun (Indian Blackberry)/20241105_132418.jpg" alt="Jamun (Indian Blackberry)" width="200" height="200" style="margin: 10px; object-fit: cover;">

  <!-- Row 4 -->
  <img src="02-Sample Dataset/Adulsa/Mango/20241104_170544.jpg" alt="Mango" width="200" height="200" style="margin: 10px; object-fit: cover;">
  <img src="02-Sample Dataset/Adulsa/Neem/20241106_141856(0).jpg" alt="Neem" width="200" height="200" style="margin: 10px; object-fit: cover;">
  <img src="02-Sample Dataset/Adulsa/Onion/20241104_175539.jpg" alt="Onion" width="200" height="200" style="margin: 10px; object-fit: cover;">
  <img src="02-Sample Dataset/Adulsa/Panfuti/20241023_144521.jpg" alt="Panfuti" width="200" height="200" style="margin: 10px; object-fit: cover;">

  <!-- Row 5 -->
  <img src="02-Sample Dataset/Adulsa/Papaya/20241105_134557.jpg" alt="Papaya" width="200" height="200" style="margin: 10px; object-fit: cover;">
  <img src="02-Sample Dataset/Adulsa/Satynashi/20241104_172716(0).jpg" alt="Satyanashi" width="200" height="200" style="margin: 10px; object-fit: cover;">
  <img src="02-Sample Dataset/Adulsa/Shatavari/20241023_151335.jpg" alt="Shatavari" width="200" height="200" style="margin: 10px; object-fit: cover;">
  <img src="02-Sample Dataset/Adulsa/Sugarcane/20241105_141329.jpg" alt="Sugarcane" width="200" height="200" style="margin: 10px; object-fit: cover;">

  <!-- Row 6 -->
  <img src="02-Sample Dataset/Adulsa/Tandulja/20241105_175945.jpg" alt="Tandulja" width="200" height="200" style="margin: 10px; object-fit: cover;">
  <img src="02-Sample Dataset/Adulsa/Touch Me Not/20241023_153601.jpg" alt="Touch Me Not" width="200" height="200" style="margin: 10px; object-fit: cover;">

</div>
