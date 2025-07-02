# 🧬 Personalized Meal Planner (QNN + Genomics + LLM)

This project builds a complete genomics-to-nutrition pipeline using synthetic SNP data, quantum-inspired neural networks, and language-model-driven recommendation logic. The goal is to generate adaptive, evidence-aligned meal plans based on a user’s polygenic risk profile—all accessible via a lightweight web interface.

## 🧪 Genetic Risk Modeling

The process begins with simulated SNP data reflecting key nutrition-relevant traits—liver cirrhosis, BMI, and iron absorption. For each individual, the code randomly generates genotypes (0, 1, 2 copies of a risk allele) across curated SNPs. Using published beta coefficients, it computes polygenic risk scores (PRS) for each trait. Based on quantized thresholds, individuals are labeled "HIGH" or "LOW" risk—creating a labeled dataset of synthetic genomic profiles.

This dataset is stored in structured CSVs (e.g., `bmi_generated_data.csv`, `liver_generated_data.csv`) and serves as the training/test bed for downstream models.

## 🧠 Quantum Neural Network (QNN) Integration

The notebook `qnn.ipynb` implements a post variational quantum neural network to learn correlations between genetic profiles and nutrition categories. While not run on real quantum hardware, the QNN architecture introduces entanglement-like interactions between features to capture non-linear dependencies that classical linear models might miss.

The model’s goal is to recommend diet types (e.g., high-protein, low-carb, etc.) given a PRS vector.

## 🧬 LLM-Powered Meal Generation

Once a nutrition class is inferred, a prompt-based system powered by OpenAI’s GPT models takes over. The `meal.py` script structures these prompts dynamically—tailoring content based on risk scores, lifestyle flags (e.g., vegetarian), and known restrictions (e.g., lactose intolerance). The generated meal plans are structured, context-aware, and consistent across runs.

This hybrid approach bridges hardcoded SNP risk scoring with generative flexibility—producing meal plans that feel both medically grounded and personalized.

## 🌐 Web Interface

The `app.py` Flask backend powers a multi-page web interface:
- `upload.html`: User uploads a CSV file with risk profile
- `index.html`: Personalized overview and instruction
- `chart.html`: Pie chart visualization of macronutrient targets using Chart.js

Once a file is uploaded, users see an auto-generated report that blends genetic insights with meal-level output.

## 🧩 Design Philosophy

This project was built as a modular proof-of-concept to show how:
- SNPs can be used beyond ancestry and disease prediction
- AI can turn genomic insights into real-world recommendations
- Lightweight UIs can make genomics understandable and actionable

All code runs locally without the need for real patient data. The synthetic SNP generator and OpenAI meal interface make it easy to scale or adapt to new traits in the future.
