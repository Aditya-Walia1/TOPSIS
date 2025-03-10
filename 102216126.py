# -*- coding: utf-8 -*-
"""102216126.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_Obhn98J18AQAbL71Ehh-HlsaU_3TF_n
"""

import numpy as np
import warnings

class Topsis:
    def __init__(self, evaluation_matrix, weight_matrix, criteria):
        """
        Initialize the TOPSIS class.

        :param evaluation_matrix: 2D list or ndarray of alternatives x criteria.
        :param weight_matrix: List or ndarray of weights corresponding to criteria.
        :param criteria: List or ndarray indicating 1 for benefit and 0 for cost criteria.
        """
        self.evaluation_matrix = np.array(evaluation_matrix, dtype="float")
        self.weight_matrix = np.array(weight_matrix, dtype="float") / np.sum(weight_matrix)
        self.criteria = np.array(criteria, dtype="int")

        self.row_size, self.column_size = self.evaluation_matrix.shape

        self.normalized_decision = None
        self.weighted_normalized = None
        self.best_alternatives = None
        self.worst_alternatives = None
        self.best_distance = None
        self.worst_distance = None
        self.best_similarity = None
        self.worst_similarity = None

    def normalize_decision_matrix(self):
        """Normalize the decision matrix."""
        sqrd_sum = np.sqrt(np.sum(self.evaluation_matrix**2, axis=0))
        self.normalized_decision = self.evaluation_matrix / sqrd_sum

    def calculate_weighted_normalized_matrix(self):
        """Calculate the weighted normalized decision matrix."""
        self.weighted_normalized = self.normalized_decision * self.weight_matrix

    def determine_ideal_solutions(self):
        """Determine the best and worst ideal solutions."""
        self.best_alternatives = np.where(self.criteria == 1,
                                          np.max(self.weighted_normalized, axis=0),
                                          np.min(self.weighted_normalized, axis=0))
        self.worst_alternatives = np.where(self.criteria == 1,
                                           np.min(self.weighted_normalized, axis=0),
                                           np.max(self.weighted_normalized, axis=0))

    def calculate_distances(self):
        """Calculate distances to ideal solutions."""
        self.best_distance = np.sqrt(np.sum((self.weighted_normalized - self.best_alternatives)**2, axis=1))
        self.worst_distance = np.sqrt(np.sum((self.weighted_normalized - self.worst_alternatives)**2, axis=1))

    def calculate_similarity(self):
        """Calculate similarity to the ideal solutions."""
        with np.errstate(divide='ignore', invalid='ignore'):
            total_distance = self.best_distance + self.worst_distance
            self.best_similarity = np.nan_to_num(self.worst_distance / total_distance)
            self.worst_similarity = np.nan_to_num(self.best_distance / total_distance)

    def rank(self):
        """Rank the alternatives based on the similarity to the ideal solution."""
        return np.argsort(-self.best_similarity) + 1

    def evaluate(self):
        """
        Execute the TOPSIS steps and return the rankings.

        :return: Rankings of alternatives.
        """
        self.normalize_decision_matrix()
        self.calculate_weighted_normalized_matrix()
        self.determine_ideal_solutions()
        self.calculate_distances()
        self.calculate_similarity()
        return self.rank()

# Example usage
evaluation_matrix = [
    [250, 16, 12, 5],
    [200, 16, 8, 3],
    [300, 32, 16, 4],
    [275, 32, 8, 4]
]
weights = [0.4, 0.3, 0.2, 0.1]
criteria = [1, 1, 1, 0]  # 1 for benefit, 0 for cost

topsis = Topsis(evaluation_matrix, weights, criteria)
rankings = topsis.evaluate()
print("Rankings:", rankings)

import numpy as np
import pandas as pd

class Topsis:
    def __init__(self, evaluation_matrix, weight_matrix, criteria):
        """
        Initialize the TOPSIS class.

        :param evaluation_matrix: 2D list or ndarray of alternatives x criteria.
        :param weight_matrix: List or ndarray of weights corresponding to criteria.
        :param criteria: List or ndarray indicating 1 for benefit and 0 for cost criteria.
        """
        self.evaluation_matrix = np.array(evaluation_matrix, dtype="float")
        self.weight_matrix = np.array(weight_matrix, dtype="float") / np.sum(weight_matrix)
        self.criteria = np.array(criteria, dtype="int")

        self.row_size, self.column_size = self.evaluation_matrix.shape

        self.normalized_decision = None
        self.weighted_normalized = None
        self.best_alternatives = None
        self.worst_alternatives = None
        self.best_distance = None
        self.worst_distance = None
        self.best_similarity = None
        self.worst_similarity = None

    def normalize_decision_matrix(self):
        """Normalize the decision matrix."""
        sqrd_sum = np.sqrt(np.sum(self.evaluation_matrix**2, axis=0))
        self.normalized_decision = self.evaluation_matrix / sqrd_sum

    def calculate_weighted_normalized_matrix(self):
        """Calculate the weighted normalized decision matrix."""
        self.weighted_normalized = self.normalized_decision * self.weight_matrix

    def determine_ideal_solutions(self):
        """Determine the best and worst ideal solutions."""
        self.best_alternatives = np.where(self.criteria == 1,
                                          np.max(self.weighted_normalized, axis=0),
                                          np.min(self.weighted_normalized, axis=0))
        self.worst_alternatives = np.where(self.criteria == 1,
                                           np.min(self.weighted_normalized, axis=0),
                                           np.max(self.weighted_normalized, axis=0))

    def calculate_distances(self):
        """Calculate distances to ideal solutions."""
        self.best_distance = np.sqrt(np.sum((self.weighted_normalized - self.best_alternatives)**2, axis=1))
        self.worst_distance = np.sqrt(np.sum((self.weighted_normalized - self.worst_alternatives)**2, axis=1))

    def calculate_similarity(self):
        """Calculate similarity to the ideal solutions."""
        with np.errstate(divide='ignore', invalid='ignore'):
            total_distance = self.best_distance + self.worst_distance
            self.best_similarity = np.nan_to_num(self.worst_distance / total_distance)
            self.worst_similarity = np.nan_to_num(self.best_distance / total_distance)

    def rank(self):
        """Rank the alternatives based on the similarity to the ideal solution."""
        return np.argsort(-self.best_similarity) + 1

    def evaluate(self):
        """
        Execute the TOPSIS steps and return the rankings.

        :return: Rankings of alternatives.
        """
        self.normalize_decision_matrix()
        self.calculate_weighted_normalized_matrix()
        self.determine_ideal_solutions()
        self.calculate_distances()
        self.calculate_similarity()
        return self.rank()

# Load the data from the uploaded Excel file
data_path = '/content/data.xlsx'
data = pd.read_excel(data_path, sheet_name='data')

# Prepare the evaluation matrix, weights, and criteria
evaluation_matrix = data.iloc[:, 1:].values  # Exclude the first column (Fund Name)
weights = [0.2, 0.3, 0.2, 0.2, 0.1]  # Example weights for P1 to P5
criteria = [1, 1, 1, 1, 0]  # Example criteria: 1 for benefit, 0 for cost

# Run TOPSIS analysis
topsis = Topsis(evaluation_matrix, weights, criteria)
rankings = topsis.evaluate()

# Add rankings to the original data and save the result
data['Rank'] = rankings
output_path = '/mnt/data/102216126-results.xlsx'
data.to_excel(output_path, index=False)

print("TOPSIS analysis complete. Results saved to:", output_path)

import os

# Create the directory if it doesn't exist
output_dir = '/mnt/data'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the file
output_path = os.path.join(output_dir, '102216126-results.xlsx')
data.to_excel(output_path, index=False)

print("TOPSIS analysis complete. Results saved to:", output_path)

from google.colab import files

# Provide the correct path to the output file
output_path = '/mnt/data/102216126-results.xlsx'

# Trigger download
files.download(output_path)