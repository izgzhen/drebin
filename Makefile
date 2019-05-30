deploy:
	zrsync --exclude "gooddir" --exclude "maldir" . bicycle:~/projects/seguard-other

init:
	pip install sklearn joblib pebble psutil networkx pandas
