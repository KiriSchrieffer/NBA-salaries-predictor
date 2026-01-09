# NBA Salaries Predictor

## 项目简介 (Project Overview)

### 中文介绍
NBA薪资预测器是一个基于机器学习的数据分析项目，旨在通过分析NBA球员的职业生涯统计数据来预测他们的薪资水平。该项目使用1985年至2018年的历史薪资数据和球员表现数据，探索球员统计数据（如场均得分、助攻、三分球命中率等）与薪资之间的关系，并建立预测模型。

**主要功能：**
- **数据可视化分析**：生成球员统计数据与薪资关系的交互式图表
- **薪资预测**：基于球员的场均助攻、得分和三分球命中率预测薪资
- **模型评估**：使用R²值和相对误差评估预测模型的准确性
- **薪资帽分析**：考虑NBA薪资帽对球员薪资的影响

**技术栈：**
- Python (pandas, scikit-learn, altair, plotly)
- 线性回归模型
- 数据爬取与清洗

### English Introduction
NBA Salaries Predictor is a machine learning-based data analysis project designed to predict NBA player salaries based on their career statistics. Using historical salary data from 1985 to 2018 and player performance metrics, this project explores the relationship between player statistics (such as points per game, assists, three-point field goal percentage) and salaries, and builds predictive models.

**Key Features:**
- **Data Visualization**: Generate interactive charts showing relationships between player statistics and salaries
- **Salary Prediction**: Predict salaries based on player's assists per game, points per game, and 3-point field goal percentage
- **Model Evaluation**: Assess prediction accuracy using R-squared values and relative error metrics
- **Salary Cap Analysis**: Consider the impact of NBA salary cap on player compensation

**Technology Stack:**
- Python (pandas, scikit-learn, altair, plotly)
- Linear Regression Models
- Data Scraping and Cleaning

---

## For Question 1 and 2
You should download all the files in the 'NBASalaryPredictrorQ1Q2', and you should make sure you have installed altair and pandas libraries.
Next, you should put all the files under one file folder, and then you can run 'main.py' to get the picture you want.
## For Question 3
You should download all the file in the ‘NBASalaryPredictorQ3' and place all files in the same folder, and you should make sure you have installed plotly and pandas libraries. Next you can run the relevant files according to the relationship graph you want to obtain and the related statistical values (r-square value, etc.) you want to get. Each file is independent of the other and can be run normally provided that you have downloaded the required libraries. All output plots are also given in the folder "output plots."
## For Question 4
Download the folder 'NBASalaryPredictorQ4'.  
Download Microsoft Excel App.  
Firstly, run 'q4.py' to train the model using 'salaries_1985to2018.csv', 'salary_cap.csv' and 'players.csv'.  
Then run 'main.py'. It will guide you to input data and make prediction.  
If you want to test the model, run 'q4_test.py'. It uses data from 'test_points_2023.csv' and 'test_salary_2023.csv' to test the accuracy of the prediction program.  
The test gives you R-squared values and the percentage of relative error less than 50% of training the model WITH or WITHOUT using salary cap.  
These two test files are provided in the folder, but if you want to get them by yourself, run 'get_test_points_2023.py' and 'get_test_salary_2023.py'.  
'get_test_points_2023.py' crawls data from https://www.basketball-reference.com/leagues/NBA_2023_totals.html  
'get_test_salary_2023.py' crawls data from http://www.espn.com/nba/salaries  
They save the data in csv files, encoding ANSI.  
You have to open the csv files with Excel and save them as encoding UTF-8 to make them readable for 'q4_test.py'  
To save a file as a CSV (Comma Separated Values) file in Excel, you can follow these steps:  
1.Open the Excel file you want to save as a CSV file.  
2.Click on the "File" tab in the top left corner of the Excel window.  
3.Click on "Save As" in the menu on the left side of the window.  
4.In the "Save As" dialog box, save the new file in this folder.  
5.In the "Save as type" dropdown menu, select "CSV (Comma delimited) (*.csv)".  
6.Click on the "Save" button.  
7.Excel will ask you if you want to replace the existing file with the same name, click on "OK".
