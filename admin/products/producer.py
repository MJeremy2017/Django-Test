import pika, json

params = pika.URLParameters('amqps://mlqrwnxw:nezTSbhz9U6BZta7i8nWXMUEfne1yDGM@snake.rmq2.cloudamqp.com/mlqrwnxw')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
