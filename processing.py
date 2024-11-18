import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd



# Load the Excel file from the source code
# file_path = 'assign1_be303.xlsx'
data = pd.read_excel("assign1_be303.xlsx")

# Display the first few rows of the dataset and summary information
data.head()

#variance calculation
variance_age = np.var(data['Age year'])
variance_height = np.var(data['Height m'])
variance_weight = np.var(data['Weight kg'])

# Figure 1: Table with Summary Statistics

summary_table = pd.DataFrame({
    'Statistic': ['Mean', 'Variance', 'Median', 'Minimum', 'Maximum'],
    'Age (years)': [data['Age year'].mean(), variance_age, data['Age year'].median(), data['Age year'].min(), data['Age year'].max()],
    'Height (m)': [data['Height m'].mean(), variance_height, data['Height m'].median(), data['Height m'].min(), data['Height m'].max()],
    'Weight (kg)': [data['Weight kg'].mean(), variance_weight, data['Weight kg'].median(), data['Weight kg'].min(), data['Weight kg'].max()]
})
print
summary_table.set_index('Statistic', inplace=True)

print("\n Solution table of  (a) question \n\n")
print(summary_table)
print("\n\n")

#for plots of height weight and
# Figure 2: Histograms
plt.figure(figsize=(15, 5))

# Age Histogram
plt.subplot(1, 3, 1)
sns.histplot(data['Age year'],kde=True, color='blue')
plt.title('Histogram of Age')
plt.legend(['Age'])
plt.xlabel('Age (years)')
plt.ylabel('Frequency')

# Height Histogram
plt.subplot(1, 3, 2)
sns.histplot(data['Height m'],kde=True, color='green')
plt.title('Histogram of Height')
plt.legend(['Height'])
plt.xlabel('Height (m)')
plt.ylabel('Frequency')

# Weight Histogram
plt.subplot(1, 3, 3)
sns.histplot(data['Weight kg'], kde=True, color='red')

plt.title('Histogram of Weight')
plt.xlabel('Weight (kg)')
plt.legend(['Weight'])
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

#part 3: Box-Plots of age height and weight
plt.figure(figsize=(15, 5))

# Age Box Plot
plt.subplot(1, 3, 1)
sns.boxplot(y=data['Age year'], color='blue')
plt.legend(['Age'])
plt.title('Box-Plot of Age')
plt.ylabel('Age (years)')

# Height Box Plot
plt.subplot(1, 3, 2)
sns.boxplot(y=data['Height m'], color='green')
plt.legend(['Height'])
plt.title('Box-Plot of Height')
plt.ylabel('Height (m)')

# Weight Box Plot
plt.subplot(1, 3, 3)
sns.boxplot(y=data['Weight kg'], color='red')
plt.title('Box-Plot of Weight')
plt.legend(['Weight'])
plt.ylabel('Weight (kg)')
plt.tight_layout()
plt.show()


from scipy.stats import pearsonr

# Figure 4: Scatterplots with Pearson Correlation Coefficients
plt.figure(figsize=(15, 5))

# Scatterplot: Age vs Weight
plt.subplot(1, 3, 1)
sns.regplot(x=data['Age year'], y=data['Weight kg'], color='blue')
r_age_weight, _ = pearsonr(data['Age year'], data['Weight kg'])
plt.title(f'Age vs Weight (r = {r_age_weight:.2f})')
plt.legend(['Age'])
plt.xlabel('Age (years)')
plt.ylabel('Weight (kg)')

# Scatterplot: Age vs Height
plt.subplot(1, 3, 2)
sns.regplot(x=data['Age year'], y=data['Height m'], color='green')
r_age_height, _ = pearsonr(data['Age year'], data['Height m'])
plt.title(f'Age vs Height (r = {r_age_height:.2f})')
plt.legend(['Height'])
plt.xlabel('Age (years)')
plt.ylabel('Height (m)')

# Scatterplot: Height vs Weight
plt.subplot(1, 3, 3)
sns.regplot(x=data['Height m'], y=data['Weight kg'], color='red')
r_height_weight, _ = pearsonr(data['Height m'], data['Weight kg'])
plt.title(f'Height vs Weight (r = {r_height_weight:.2f})')
plt.legend(['Weight'])
plt.xlabel('Height (m)')
plt.ylabel('Weight (kg)')

plt.tight_layout()
plt.show()


gender_counts = data['Gender'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightgreen', 'lightcoral'])
plt.legend(gender_counts.index, title="Gender", loc="best")

plt.title('Gender Proportions')
plt.show()
