PORT="${PORT:-7011}"
NAME="${NAME:-tensorboard}"

screen -dmS $NAME
screen -x -S $NAME -p 0 -X stuff "tensorboard --logdir tb_logger/ --port $PORT  --bind_all"
screen -x -S $NAME -p 0 -X stuff $"\n"
