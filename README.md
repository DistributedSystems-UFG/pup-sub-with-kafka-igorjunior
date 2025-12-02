[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/eycvIrW-)
# Group Chat with Kafka

Topic-based group chat system using Kafka Publish-Subscribe pattern.

### First, install kafka-python (on each machine):

    pip3 install kafka-python

### Or, with virtual environments (also on each machine -- only install pip3 and venv if not yet installed):

    sudo apt update
    sudo apt install python3-pip
    sudo apt install python3-venv
    python3 -m venv myvenv
    source myvenv/bin/activate
    pip3 install kafka-python

### Next, configure the Kafka broker address and port in the const.py file

Note: Make sure that this repo is cloned in all the machines used for this experiment and that a Kafka broker is running.

### Finally, run the chat on any machine:

    python3 chat.py
