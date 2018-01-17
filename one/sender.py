import pika;
import sys;

credentials=pika.PlainCredentials("guest","guest");
connectionparameter=pika.ConnectionParameters("localhost",credentials=credentials);
conn_broker=pika.BlockingConnection(connectionparameter);

channel=conn_broker.channel();
channel.queue_declare(queue="hello");


channel.basic_publish(exchange='',routing_key="hello", body="Hello this is a message");

print("Message has been sent");
conn_broker.close();
