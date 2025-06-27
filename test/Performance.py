import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score 
import logging
import os
from dotenv import load_dotenv
from scipy.stats import chi2_contingency
load_dotenv()

file_path = os.getenv("file_path")

class Performance:
    def __init__(self):
        self.file = file_path
        self.data = None
        
    def read_file(self):
        try:
            self.data = pd.read_csv(self.file)
        except FileNotFoundError:
            logging.error(f"File not found {self.file}")
        
    def check_for_missing_values(self):
        if self.data.empty:
            logging.error(f"Dataframe: {self.data} is empty")
            return
        checkForNaN = self.data.isna().sum()
        return checkForNaN.any()
    
    def drop_missing_values(self):
        if self.check_for_missing_values():
            self.data.dropna(axis=0, how='any')
        else:
            return
    def spearman_correlation(self):
        if self.data.empty:
            logging.error(f"The dataframe: {self.file} is empty")
            return
        attr_and_score = self.data[['study_hours_per_day', 'exam_score']]
        correlation_age_examscore = attr_and_score.corr(method="spearman", numeric_only=False)
        print(correlation_age_examscore)
        
    def chi2_contingency_analysis(self):
        if self.data.empty:
            logging.error(f"The dataframe: {self.file} is empty")
            return

        # Create contingency table
        contingency_table = pd.crosstab(self.data['gender'], self.data['exam_score'])
        print("Contingency Table:\n", contingency_table)

        # Perform chi-square test
        stat, p, dof, expected = chi2_contingency(contingency_table)

        # Display results
        print("\nChi-Square Test Results:")
        print(f"Statistic: {stat:.4f}")
        print(f"p-value: {p:.4e}")
        print(f"Degrees of Freedom: {dof}")
        print("Expected Frequencies:\n", pd.DataFrame(expected, index=contingency_table.index, columns=contingency_table.columns))

        alpha = 0.05
        if p <= alpha:
            print("\nResult: Hypothesis rejected - There is a significant association between gender and exam score.")
        else:
            print("\nResult: Hypothesis accepted - No significant association between gender and exam score.")
    def corr_parent_edu_exam_score(self):
        if self.data.empty:
            logging.error(f"The dataframe: {self.file} is empty")
            return
        contingency_table = pd.crosstab(self.data['parental_education_level'], self.data['exam_score'])
        stat, p, dof, expected = chi2_contingency(contingency_table)
        alpha = 0.05
        if p <= alpha:
            print("Hypothesis rejected - significant association between the two variables")
        else:
            print("Hypothesis accepted - no significant association between the two variables")
            
    def average_study_hours_for_high_score(self):
        high_scores = self.data[(self.data['exam_score'] >= 90) & (self.data['exam_score'] <= 100)]
        avg_working_hours = high_scores['study_hours_per_day'].mean()
        print(f"Average working hours per week for students with exam scores between 90 and 100: {avg_working_hours:.2f}")
    
    def group_the_scores_and_avg_study_hour(self):
        exam_score = self.data['exam_score']
        study_hours = ['study_hours_per_day']
        avg_study_hours = {
            'high_scores': float(self.data[(exam_score >= 90) & (exam_score <= 100)][study_hours].mean()),
            'avg_scores': float(self.data[(exam_score >= 70) & (exam_score < 90)][study_hours].mean()),
            'low_scores': float(self.data[(exam_score >= 50) & (exam_score < 70)][study_hours].mean()),
            'failing_scores': float(self.data[(exam_score >= 0) & (exam_score < 50)][study_hours].mean())
        }
        for key, value in avg_study_hours.items():
            print(f"{key}: {value:.2f}")
            
    def pearson_correlation_test(self):
       pearson_test = self.data.corr(method='pearson', numeric_only=True)
       print(pearson_test)
            

        
        
    def average_score_female(self):
        df = self.data
        if self.data.empty:
            logging.error("The dataframe is empty")
            return
        #female_avg_exam_score = df[(df['gender'] == "Female") & (df['part_time_job'] == "No")]['exam_score'].mean()
        #print(f"The average exam score for females is: {female_avg_exam_score:.2f}")
        
        job_exam_score = df[df['gender'] == "Female"].groupby(['diet_quality'])['exam_score'].mean()
        print(job_exam_score)
    def average_exam_score_specific_study_hours(self, study_hours):
        df = self.data
        avg_exam_score = df[df['study_hours_per_day'] == study_hours]['exam_score'].mean()
        print(f"Average exam score for {study_hours} is {avg_exam_score}")
    
    def add_arrays(self):
        a = np.array([1, 2, 3])
        b = np.array([1, 2, 3])
        c = np.array([1, 2, 3])
        result = np.add(np.add(a,b), c)
        print(result)
    
    def main(self):
        #self.read_file()
        #self.drop_missing_values()
        #self.spearman_correlation()
        #self.chi2_contingency_analysis()
        #self.average_study_hours_for_high_score()
        #self.group_the_scores_and_avg_study_hour()
        #self.train_features_exam_score()
        #self.corr_parent_edu_exam_score()
        #self.pearson_correlation_test()
        #self.average_exam_score_specific_study_hours(5)
        #self.average_score_female()
        self.add_arrays()
if __name__ == "__main__":
    pf = Performance()
    pf.main()        