import tensorflow as tf
import numpy as np
import pandas as pd

#Load data
data = pd.read_csv('app/se-dataset-real.csv')

#bifurcate into X and y
X = data.iloc[:, 1:]
y = data.Roles 

#convert to tensors
tensor_X = tf.convert_to_tensor(X, dtype=tf.float32)
tensor_y = tf.convert_to_tensor(y, dtype=tf.string)

def top_roles(inp_list):
    """
    This function inputs the client's data and displays the top matching job roles
    parameters:
    inp_list: list[int]

    return job_res: list[str] - top job roles
    """
    technologies = [
    "Java", "Python", "Javascript", "C++", "Swift", "Kotlin", "R", "SQL", "HTML", "CSS",
    "C#", "Ruby", "Shellscripting", "Git", "GitHub", "React.js", "Node.js", "Angular",
    "React Native", "Flutter", "Xamarin", "Vue.js", "Adobe XD", "Figma", "InVision",
    "Zeplin", "Sketch", "Django", "Flask", "FastAPI", "MySQL", "MongoDB", "PostgreSQL",
    "OracleDB", "AWS", "Azure", "GCP", "Wireshark", "Metasploit", "Nessus", "TCP/IP",
    "VLAN", "OSPF", "Firewalls", "Cisco", "Juniper", "Intrusion Detection Systems (IDS)",
    "Virtual Private Networks (VPN)", "Network Access Control (NAC)", "SIEM",
    "Encryption Algorithms", "Docker", "Kubernetes", "Jenkins", "Ansible", "Terraform",
    "VMWare", "PowerShell", "Linux", "Windows Server", "Remote Desktop Tools",
    "Tableu", "Power BI", "Google Analytics", "Excel", "Hadoop", "Spark", "Kafka", "Hive",
    "Scala", "Tensorflow", "PyTorch", "NLTK", "Numpy", "Pandas", "spaCy", "Transformers",
    "OpenCV", "YOLO", "CUDA", "Word2Vec", "Qiskit", "Cirq", "Ehtereum", "Solidity",
    "Cryptography", "Blockchain Platforms", "Smart Contracts", "Trello", "Jira", "Asana",
    "Slack", "Video Conferencing", "Confluence", "Embedded Linux", "Microcontrollers",
    "RTOS", "ROS", "Sensors", "CAD Software", "Selenium", "JUnit", "TestNG", "Postman",
    "Appium", "Q#", "Quipper", "Silq", "ProjectQ", "QuNetSim", "NetSquid", "QKDSim",
    "QuISP", "QuNetSimulator", "Quantum Circuits", "Quantum Algorithms", "QKD Systems",
    "Quantum Repeaters"
]
    
    inp = []
    for tech in technologies:
        if tech in inp_list:
            inp.append(1.0)
        else:
            inp.append(0.0)
    

    tensor_inp = tf.constant([inp], dtype=tf.float32)

    #dot product
    dot_product = tf.matmul(tensor_X, tf.reshape(tensor_inp, [-1,1]))

    tensor_X_norm = tf.norm(tensor_X,axis=1, keepdims=True)
    tensor_inp_norm = tf.norm(tensor_inp)

    cos_sim = dot_product / (tensor_X_norm * tensor_inp_norm)
    cos_sim = tf.squeeze(cos_sim)

    top_indices = tf.argsort(cos_sim, direction='DESCENDING')

    top_10_indices = top_indices[:10]

    res = []
    for index in top_10_indices:
        res.append(tensor_y[index].numpy().decode('utf-8'))
    
    return res
