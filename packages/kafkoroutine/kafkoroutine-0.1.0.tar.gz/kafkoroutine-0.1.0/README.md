# kafkoroutine

This repository offers Python-based asynchronous wrappers around `kafka-python`'s Producer and Consumer, bridging them
seamlessly with Python's `asyncio`.

## Prerequisites

- Python 3.7 or later
- A running Kafka instance (for actual message passing)


## Getting Started

Follow these instructions to integrate the asynchronous Kafka components in your asyncio-based Python project.

### Installation

Install `kafkoroutine` using pip:

```bash
pip install kafkoroutine
```

Please note: this project requires Python 3.7 or later and is built upon the `kafka-python` library.

## Usage

### AsyncKafkaConsumer

```python
from kafkoroutine.consumer import AsyncKafkaConsumer

async with AsyncKafkaConsumer(topics, executor, bootstrap_servers='localhost:9092') as consumer:
    async for message in consumer:
        print(f"Received: {message.value.decode('utf-8')}")
```

### AsyncKafkaProducer

```python
from kafkoroutine.producer import AsyncKafkaProducer

async with AsyncKafkaProducer(executor, bootstrap_servers='localhost:9092') as producer:
    for msg in messages:
        await producer.send(topic, msg)
```

## Built With

* [Poetry](https://python-poetry.org/docs/) - Packaging and dependency management
* [asyncio](https://docs.python.org/3/library/asyncio.html) - Asynchronous I/O, event loop, and coroutines used for the
  implementation.
* [kafka-python](https://github.com/dpkp/kafka-python) - The Python client for Apache Kafka upon which these
  asynchronous wrappers are built.

## License

This project follows the guidelines of the MIT License.