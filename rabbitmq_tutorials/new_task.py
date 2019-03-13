import pika
import sys


messages = ['First message.',
            'Second message..',
            'Third message...',
            'Fourth message....',
            'Fifth message.....']

# message = ' '.join(sys.argv[1:]) or "Hello World!"
for message in messages:
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)

    channel.basic_publish(exchange='',
                          routing_key='task_queue',
                          body=message,
                          properties=pika.BasicProperties(
                              delivery_mode=2
                          ))
    print('[x] Sent %s' % message)
    connection.close()


