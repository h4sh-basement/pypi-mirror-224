from collections import namedtuple
from typing import Dict, Optional, Any

from clean_confluent_kafka.utils import flatten_dict, reverse_flatten_dict, unflatten_dict


class KafkaConfigParser:
    ParsedConfigResult = namedtuple("ParsedConfigResult", ["consumer", "producer", "app"])
    ParsedConfig = namedtuple("ParsedConfig", ["config", "topic", "app"])

    @staticmethod
    def from_path(path):
        import yaml
        with open(path) as f:
            config = yaml.safe_load(f)
        return KafkaConfigParser(config)

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config if config is not None else dict()
        self.config = flatten_dict(self.config)

    def update_config(self, config: Dict[str, Any]):
        self.config.update(flatten_dict(config))

    def _get(self, name):
        _configs = unflatten_dict(self.config).get(name, None)
        if _configs is None:
            _configs = dict()
        return _configs

    def _create_parsed_config(self, name):
        kafka_configs = self._get(name)
        if name == "consumer":
            topic = kafka_configs.pop("topics", [])
            if not isinstance(topic, list):
                topic = [topic]
        else:
            topic = kafka_configs.pop("topic", "")
        config_app = kafka_configs.pop("app", None)
        return self.ParsedConfig(flatten_dict(kafka_configs), topic, config_app)

    def parse(self):
        app_configs = reverse_flatten_dict(self._get("app"))
        return self.ParsedConfigResult(
            consumer=self._create_parsed_config("consumer"),
            producer=self._create_parsed_config("producer"),
            app=app_configs
        )

    def export_config(self):
        return unflatten_dict(self.config)