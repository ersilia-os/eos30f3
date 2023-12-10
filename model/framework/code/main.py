# imports
import os
import csv
import sys
import subprocess
import pandas as pd

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

print('input_file',input_file)
print('output_file',output_file)

#current file directory
root = os.path.dirname(os.path.abspath(__file__))
print('root',root)


print('starting process....')

check_fold_relative_path = "../checkpoints/I_train_rand"
check_fold_absolute_path= os.path.abspath(os.path.join(root,"..", "..","checkpoints", "I_train_rand"))
print('check_fold_absolute_path',check_fold_absolute_path)


preds_base_absolute_path= os.path.abspath(os.path.join(root,"P_I_test.csv"))

predict_absolute_path= os.path.abspath(os.path.join(root,"chemprop", "predict.py"))


for i in range(5):
    print(i)
    
    # Build the command as a list of arguments
    command = [
        'python',
        predict_absolute_path,
        f'--checkpoint_path={check_fold_absolute_path}/fold_{i}/model_0/model.pt',
        f'--test_path={input_file}',
        f'--preds_path={preds_base_absolute_path}{i}.csv'
    ]

    # Print the command for debugging
    print(' '.join(command))

    # Run the command
    subprocess.run(command, check=True)

print('done')

print('renamed')


# DMPNN-hERG/example_notebook/P_I_test.csv0.csv
relative_path0 = "P_I_test.csv0.csv"
predict_absolute_path0 = os.path.join(root, relative_path0)
print('predict_absolute_path0',predict_absolute_path0)

relative_path1 = "P_I_test.csv1.csv"
predict_absolute_path1 = os.path.join(root, relative_path1)

relative_path2 = "P_I_test.csv2.csv" 
predict_absolute_path2 = os.path.join(root, relative_path2)

relative_path3 = "P_I_test.csv3.csv"
predict_absolute_path3 = os.path.join(root, relative_path3)

relative_path4 = "P_I_test.csv4.csv"
predict_absolute_path4 = os.path.join(root,  relative_path4)


df1 = pd.read_csv(predict_absolute_path0)  
df2 = pd.read_csv(predict_absolute_path1)
df3 = pd.read_csv(predict_absolute_path2)  
df4 = pd.read_csv(predict_absolute_path3)
df5 = pd.read_csv(predict_absolute_path4)  

# Extract the 'class' column from df1 and df2
class_df1 = df1['class']
class_df2 = df2['class']
class_df3 = df3['class']
class_df4 = df4['class']
class_df5 = df5['class']

# Calculate the mean between each value of the 'class' column in df1 and df2
mean_class = (class_df1 + class_df2 + class_df3 + class_df4 + class_df5) / 5
print(mean_class)

# Create a new dataframe with 'smiles' and the calculated mean 'class'
new_df = pd.DataFrame({
     # Assuming 'smiles' is the same in both dataframes
    'predictions': mean_class
})

# Print or save the new dataframe
print(new_df)
print("hello")

# To save the new dataframe to a CSV file, 

prediction_absolute_path= os.path.abspath(os.path.join(root,"..",output_file))
new_df.to_csv(prediction_absolute_path, index=False) 

print('finally done')


# Check if the file exists before attempting to delete
if os.path.exists(predict_absolute_path0):
    # Delete the file
    os.remove(predict_absolute_path0)
    os.remove(predict_absolute_path1)
    os.remove(predict_absolute_path2)
    os.remove(predict_absolute_path3)
    os.remove(predict_absolute_path4)
    print(f"The file has been deleted.")
else:
    print(f"The file does not exist.")
