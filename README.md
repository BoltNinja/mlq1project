# mlq1project

## ML Quarter 1 Project – Automating Sub-Classification for Enhanced Supply Chain Optimization and Decision-Making

**Abstract:**  
Supply chain datasets for global health logistics often include complex, categorical attributes that influence operational workflows. This project focuses on automating the classification of pharmaceutical shipments (e.g., HIV tests, pediatric drugs, antimalarials) based on a diverse range of shipment metadata. Accurate sub-classification of products streamlines logistics, improves financial forecasting, and ensures timely allocation of critical resources. Our approach uses a stratified and preprocessed version of a real-world dataset and evaluates various feature selection methods to determine the most impactful attributes. Among multiple classifiers tested, the combination of the **ReliefFAttributeEval feature selector** with the **J48 decision tree algorithm** demonstrated the lowest overall error and best balance between model simplicity and performance. The model achieved nearly perfect classification accuracy on most categories and revealed that **"dosage form"** was the most universally predictive feature across all selection strategies.

This system offers a promising avenue for improving efficiency in public health supply chains and addressing demand volatility, particularly for underrepresented categories like ACT and malaria drugs.

---

## Steps to run our code:

1. **Download the repository** and navigate to the `mlq1project` folder.

2. **Use our preprocessed and sampled dataset**:  
   `Supply_Chain_Shipment_Pricing_Dataset_FinalSampled.csv`  
   This dataset was created from `Supply_Chain_Shipment_Pricing_Dataset.csv` using the following preprocessing steps:
   - Removed special characters (e.g., Côte d'Ivoire → Cote d Ivoire)
   - Replaced missing values using Weka’s `ReplaceMissingValues` filter
   - Replaced hidden placeholders (e.g., “Date Not Captured”) with mode values
   - Removed redundant/derived columns (e.g., ID, vendor, item description)
   - Normalized numeric fields on a 1–1000 scale
   - Took a 40% stratified sample to preserve rare class instances

3. **Run our notebook** `RohithYelisetty,AaravGupta_Q1Project.ipynb` to reproduce our results:
   - Perform attribute selection using `ReliefFAttributeEval` in Weka
   - Keep features with scores > 0.1 along with the class attribute `sub_classification`
   - Use Weka’s `J48` decision tree on the training dataset (`ReliefTrain.arff`)
   - Evaluate performance on `ReliefTest.arff` using accuracy and error metrics
   - Save the model as `bestModelJ48Relief.model`

4. You can also test other feature selection techniques (e.g., `CorrelationAttributeEval`, `GainRatioAttributeEval`, `CfsSubsetEval`, `PersonalSelection`) and classifiers (`NaiveBayes`, `OneR`, `RandomForest`) using the respective datasets in:
   - `ReliefFAttributeEvalData/`
   - `CorrelationAttributeEvalData/`
   - `GainRatioAttributeEvalData/`
   - `CfsSubsetEvalData/`
   - `PersonalAttributeData/`

---
