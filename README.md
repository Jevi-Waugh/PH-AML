##Leveraging Persistent Homology for Topological Feature Extraction in Machine Learning: The PH-AML Pipeline

#Overview
Conventional Machine learning models often rely on purely statistical data while overlooking the rich global structure of complex datasets. In this paper, we propose PHAML (Persistent Homology-Augmented Machine Learning), a pipeline designed to address this shortcoming by effectively extracting topological descriptors from high-dimensional data and inserting them into standard supervised models. Specifically, we construct simplicial complexes through the Vietoris–Rips filtrations over the input data, compute persistent homology to obtain persistent landscapes and barcodes and convert this data into quantitative feature vectors to feed to ML models such as Support Vector Machine and Logistic Regression. Those topological features are integrated with traditional inputs, yielding an augmented representation of the data featuring global shape and general variations. PHAML is assessed on synthetic and real-world datasets, demonstrating improvements in classification performance, accuracy, and noise robustness and leveraging topological invariants' stability under perturbations. We also compare a baseline model with conventional features with a PHAML model to quantify the performance improvements attributable to persistent homology. Our results underscore the benefit of combining topological descriptors with classical features, highlighting the promise of persistent homology-based machine learning models in which global structure is preserved.

This is an active paper/project that I currently working on at the moment and i will push any relevant files as soon as i get some results.

#Installation
Specific versions must be used to prevent conflicts from dependencies requiring different package versions.

#Requirements
*Python 3.7+
*Julia 1.6
*ripser
*persim
*scikit-learn
*NumPy
*Matplotlib