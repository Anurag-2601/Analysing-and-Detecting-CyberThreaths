# Analysing-and-Detecting-CyberThreaths

🧠 Analyzing and Detecting Cyber Threats:

Machine Learning–based Cybersecurity System for IoT-enabled Cyber-Physical Systems

B.Tech Mini Project (2024–2025)

Department of Computer Science and Engineering

Methodist College of Engineering and Technology, Hyderabad
<br><br>

📘 Overview:

This project focuses on analyzing and detecting cyberattacks in IoT-enabled Cyber-Physical Systems (CPS) using advanced Machine Learning and Deep Learning techniques.

The system is designed to identify both known and unknown attacks in industrial environments through intelligent algorithms integrated into a Tkinter-based desktop 
application.

The project uses the SWaT (Secure Water Treatment) dataset — a benchmark for industrial control system cybersecurity — and compares the performance of AutoEncoder, Decision Tree with PCA, and Deep Neural Network (DNN) models.
<br><br>

🎯 Objectives:

Detect and classify cyber threats in real-time within IoT-enabled CPS environments.

Identify and attribute various types of cyberattacks such as DoS, CMRI, NMRI, MSCI, MPCI, and MFCI.

Improve detection accuracy without using oversampling/undersampling methods.

Provide a user-friendly GUI for data upload, training, testing, and visualization.
<br><br>

⚙️ System Architecture:

The system follows a modular architecture consisting of:

Feature Generation – Extract and preprocess IoT sensor data.

Detection Modeling – Train and evaluate ML/DL models for anomaly and attack detection.

Visualization and Reporting – Display metrics like accuracy, precision, recall, and confusion matrix.

Tkinter-based GUI – Simplifies user interaction for non-technical users.
<br><br>

🧩 Models Implemented:

| Model                         | Purpose           | Description                                                 |
| ----------------------------- | ----------------- | ----------------------------------------------------------- |
| **AutoEncoder**               | Anomaly Detection | Unsupervised feature extraction from imbalanced IoT data    |
| **Decision Tree + PCA**       | Classification    | Efficient classical ML model with dimensionality reduction  |
| **Deep Neural Network (DNN)** | Classification    | High-accuracy model for complex, non-linear attack patterns |

<br><br>

🧪 Dataset:

Dataset Used: SWaT (Secure Water Treatment)

Attack Types:

Normal

NMRI (Naive Malicious Response Injection)

CMRI (Complex Malicious Response Injection)

MSCI (Malicious State Command Injection)

MPCI (Malicious Parameter Command Injection)

MFCI (Malicious Function Code Injection)

DoS (Denial of Service)
<br><br>

💡 Features:

 📂 Upload dataset via GUI

 ⚙️ Automatic preprocessing and normalization

🧠 Train ML/DL models (AutoEncoder, Decision Tree, DNN)

 📈 View accuracy, recall, F1-score comparisons

 🔍 Detect and classify cyberattacks from test data

 🪟 Interactive visualization (graphs, tables, and charts)
<br><br>

🧠 Implementation Details:

Frontend: Tkinter GUI

Backend: Python, TensorFlow/Keras, scikit-learn

Libraries: pandas, numpy, matplotlib, pickle, PCA

Modules:

train_model.py – Data loading and model training

test_model.py – Model evaluation and metric generation

ui_app.py – User interface and interaction handling

| Model               | Accuracy | Precision | Recall   | F1-Score |
| ------------------- | -------- | --------- | -------- | -------- |
| AutoEncoder         | 90%      | 0.89      | 0.88     | 0.88     |
| Decision Tree + PCA | 95%      | 0.93      | 0.94     | 0.93     |
| DNN                 | **99%**  | **0.98**  | **0.99** | **0.99** |


✅ DNN achieved the highest detection accuracy, effectively identifying both known and novel attack patterns.
<br><br>

Outputs: 
<p align="center">
 To run project double click on ‘Main.py’ file to get below screen
</p>
<p align="center">
 <img width="744" height="402" alt="image" src="https://github.com/user-attachments/assets/4e563068-ba9d-4a8f-b736-426b5d33c85f" />
</p>


<p align="center">
  <b>Upload Swat Water Dataset</b>
</p>

<br><br>
<p align="center">
In below screen click on ‘Upload SWAT Water Dataset’ button to upload application and get below output
</p>
  <p align="center">
  <img width="744" height="394" alt="image" src="https://github.com/user-attachments/assets/c6520994-6fd6-4823-9a6f-2256c64dcc26" />
</p>
 <p align="center">
  Selecting Swat Dataset
 </p>

<p align="center">
In above screen selecting and uploading SWAT dataset file and then click on ‘Open’ button to load dataset and get below output.
</p>

<br><br>
 <p align="center">
 <img width="796" height="414" alt="image" src="https://github.com/user-attachments/assets/922f57a0-b537-4f8a-b058-21d39b994938" />
</p>

 <p align="center">
 Various Cyber-Attacks Found in Dataset
</p>
<p align="center">
In above screen dataset loaded and in graph x-axis contains ATTACK NAME and y-axis contains count of those attacks found in dataset and we can see ‘NORMAL’ class contains so many records and other attacks contains very few records so it will raise data imbalance problem which can be solved using Auto-Encoder, Decision Tree and DNN. Now close above graph and then click on ‘Preprocess Dataset’ button to remove missing values and then normalized values with MIN-MAX algorithm.
</p>
<br><br>

  <p align="center">
  <img width="771" height="400" alt="image" src="https://github.com/user-attachments/assets/020f631d-2745-498b-802d-00cbbbd99bab" />
  </p>
  
<p align="center">
 Preprocess the Dataset
</p>

<p align="center">
In above screen all values are normalized (converting data between 0 and 1 called as
normalization) and then we can see total records in dataset and then dataset train and test split records count also displaying.
 </p>
 <br><br>
 
 <p align="center">
 <img width="825" height="427" alt="image" src="https://github.com/user-attachments/assets/70fe4fde-ea53-4f50-b236-3e7117edaeb8" />
</p>

<p align="center">
Running Auto-encoder Algorithm
</p>

<p align="center">
In above screen with Auto-Encoder we got 90% accuracy and this accuracy can be enhance by implementing Decision Tree with PCA algorithm and now click on ‘Run Decision Tree with PCA’ button to get below output
</p>
<br><br>

<p align="center">
<img width="815" height="419" alt="image" src="https://github.com/user-attachments/assets/5ca4b665-ae54-4f6d-9e6b-0d9b2f09742d" />
</p>

<p align="center">
  Running Decision Tree Which Are Extracted From Auto Encoder
</p>


<p align="center">
  In above screen we can see with decision tree accuracy and precision value is enhanced and now click on ‘Run DNN Algorithm’ button to further enhance accuracy and get       below output
</p>
<br><br>

 <p align="center">
   <img width="787" height="404" alt="image" src="https://github.com/user-attachments/assets/31a22b76-d64c-4d3b-89ad-7bceaa093d11" />
</p>

<p align="center">
  Running DNN Algorithm
</p>


<p align="center">
  In above screen with DNN we got 99% accuracy and now click on ‘Detection & Attribute Attack Type’ button to upload test DATA and detect attack attributes
 </p>
 <br><br>
 
<p align="center">
  <img width="797" height="417" alt="image" src="https://github.com/user-attachments/assets/5dd3e0a6-9ffb-45f7-a479-4123d3ff2114" />
</p>

<p align="center">
  Uploading Test Dataset
</p>
 
<p align="center">
  In above screen selecting and button to get below output
 </p>
 
<p align="center">
  uploading ‘TEST DATA’ file and then click on ‘Open’
 </p>
 
<p align="center">
  <img width="840" height="371" alt="image" src="https://github.com/user-attachments/assets/93b705fd-8d54-46f2-bdd5-ed28b76d19bc" />
</p>

<p align="center">
  Result After Uploading Test Dataset
</p>

<p align="center">
  In above screen in square bracket we can see TEST data values and after arrow = symbol we can see detected ATTACK TYPE and scroll down above text area to view all          detection
</p>

<p align="center">
  <img width="819" height="423" alt="image" src="https://github.com/user-attachments/assets/8df207ea-7889-415b-aeee-92061d4dad4a" />
</p>

<p align="center">
  Comparison Graph
</p>


<p align="center">
  In above graph x-axis represents algorithms names and y-axis represents different metric values such as precision, recall, accuracy and FSCORE with different colour bars    and in all algorithms DNN got high accuracy and now close above graph and then click on ‘ComparisonTable’ to get below comparison table of all algorithms
</p>

<p align="center">
  <img width="768" height="401" alt="image" src="https://github.com/user-attachments/assets/c8786609-baab-4d6a-af3c-dcb0c0e83918" />
</p>

<p align="center">
  Comparison Table
</p>

🧾 Conclusion:

The Deep Neural Network (DNN) model demonstrated superior performance in cyber threat detection within IoT-enabled CPS environments.

While PCA-optimized Decision Trees offer speed and interpretability, and AutoEncoders excel at anomaly detection, DNN provides the best trade-off between accuracy, adaptability, and scalability.

This hybrid, GUI-based solution represents a step forward in real-time, intelligent cybersecurity systems for industrial IoT.
<br><br>

🔮 Future Scope:

Real-time data stream integration for live detection

Model hyperparameter tuning for improved accuracy

Expansion to diverse IoT datasets and environments

Implementation of explainable AI (XAI) for interpretability
