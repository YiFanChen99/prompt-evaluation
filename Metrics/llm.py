"""This module is used to evaluate input by LLM"""
import json
# Package for reading config file
import configparser
# Package for using openai's api
import openai
import requests

config = configparser.ConfigParser()
config.read("config.ini")
openai.api_key = config['openai']['api_key']
openai.organization = "org-$ORG"

class OpenAILLM:
    """ This class will ask GPT3.5's opinion on input data"""
    def __init__(self, model_name) -> None:
        self.headers={
            "Authorization": f"Bearer {openai.api_key}",
            "Content-Type":"application/json"
        }
        self.model = model_name

    def _analyze_res(self, data) -> str:
        """ Extract response of LLM from http response """
        data_str = data.decode('utf-8')
        json_data = json.loads(data_str)
        response = json_data['choices'][0]['message']['content']
        return response

    def evaluate(self, input_data, prompt_data) -> list:
        """ Ask LLM's opinion """
        if len(input_data) != len(prompt_data):
            raise IndexError("input length not equal to prompt length")

        all_response = []
        for data, prompt in zip(input_data, prompt_data):
            payload={
                "model": self.model,
                "messages": [
                    {
                        "role": "user",
                        "content":  prompt[0] +
                                    f"Reference: {data[0]}\n" +
                                    f"Prediction: {data[1]}"
                    }
                ],
                "temperature": 0.2,
            }
            url = config['openai']['url']
            response = requests.post(
                url,
                data=json.dumps(payload),
                headers=self.headers,
                timeout=1000,
            )
            all_response.append(self._analyze_res(response.content))
        return all_response
