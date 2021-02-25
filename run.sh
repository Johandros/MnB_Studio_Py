# run MnB_Studio

# import sub directories
PYTHONPATH=$PYTHONPATH:${PWD}/files/module_data
PYTHONPATH=$PYTHONPATH:${PWD}/files/module_system
PYTHONPATH=$PYTHONPATH:${PWD}/io
PYTHONPATH=$PYTHONPATH:${PWD}/ms_connect
PYTHONPATH=$PYTHONPATH:${PWD}/gui
PYTHONPATH=$PYTHONPATH:${PWD}/objects
PYTHONPATH=$PYTHONPATH:${PWD}/view3D
PYTHONPATH=$PYTHONPATH:${PWD}/support

# echo $PATH
# echo $PYTHONPATH

# execute startup / main script
python -B main.py
# python main.py
