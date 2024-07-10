conda create -n mlops38 python=3.8
conda activate mlops38
pip install -r requirements.txt

python scripts/data_preparation.py
dvc add data/X_train.csv data/y_train.csv data/X_test.csv data/y_test.csv
dvc remote add -d s3remote s3://your-bucket
dvc push
