rm iris.model
vw -f iris.model --passes=3 --cache_file=iris.cache --kill_cache  --oaa 3 --loss_function=logistic --adaptive< training_data.vw 
