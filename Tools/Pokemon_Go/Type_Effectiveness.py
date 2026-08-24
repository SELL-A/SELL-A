import os
import requests

def Type_Effectiveness():
    """
    :API_description: This API provides the damage multipliers for each attacking type against various defending types in Pokemon battles.
    :param None
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "Bug": {
      "type": "object",
      "properties": {
        "Bug": { "type": "number" },
        "Dark": { "type": "number" },
        "Dragon": { "type": "number" },
        "Electric": { "type": "number" },
        "Fairy": { "type": "number" },
        "Fighting": { "type": "number" },
        "Fire": { "type": "number" },
        "Flying": { "type": "number" },
        "Ghost": { "type": "number" },
        "Grass": { "type": "number" },
        "Ground": { "type": "number" },
        "Ice": { "type": "number" },
        "Normal": { "type": "number" },
        "Poison": { "type": "number" },
        "Psychic": { "type": "number" },
        "Rock": { "type": "number" },
        "Steel": { "type": "number" },
        "Water": { "type": "number" }
      },
      "required": [
        "Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting", "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice", "Normal", "Poison", "Psychic", "Rock", "Steel", "Water"
      ]
    },
    "Dark": {
      "type": "object",
      "properties": {
        "Bug": { "type": "number" },
        "Dark": { "type": "number" },
        "Dragon": { "type": "number" },
        "Electric": { "type": "number" },
        "Fairy": { "type": "number" },
        "Fighting": { "type": "number" },
        "Fire": { "type": "number" },
        "Flying": { "type": "number" },
        "Ghost": { "type": "number" },
        "Grass": { "type": "number" },
        "Ground": { "type": "number" },
        "Ice": { "type": "number" },
        "Normal": { "type": "number" },
        "Poison": { "type": "number" },
        "Psychic": { "type": "number" },
        "Rock": { "type": "number" },
        "Steel": { "type": "number" },
        "Water": { "type": "number" }
      },
      "required": [
        "Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting", "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice", "Normal", "Poison", "Psychic", "Rock", "Steel", "Water"
      ]
    },
    "Dragon": {
      "type": "object",
      "properties": {
        "Bug": { "type": "number" },
        "Dark": { "type": "number" },
        "Dragon": { "type": "number" },
        "Electric": { "type": "number" },
        "Fairy": { "type": "number" },
        "Fighting": { "type": "number" },
        "Fire": { "type": "number" },
        "Flying": { "type": "number" },
        "Ghost": { "type": "number" },
        "Grass": { "type": "number" },
        "Ground": { "type": "number" },
        "Ice": { "type": "number" },
        "Normal": { "type": "number" },
        "Poison": { "type": "number" },
        "Psychic": { "type": "number" },
        "Rock": { "type": "number" },
        "Steel": { "type": "number" },
        "Water": { "type": "number" }
      },
      "required": [
        "Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting", "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice", "Normal", "Poison", "Psychic", "Rock", "Steel", "Water"
      ]
    },
    "Electric": {
      "type": "object",
      "properties": {
        "Bug": { "type": "number" },
        "Dark": { "type": "number" },
        "Dragon": { "type": "number" },
        "Electric": { "type": "number" },
        "Fairy": { "type": "number" },
        "Fighting": { "type": "number" },
        "Fire": { "type": "number" },
        "Flying": { "type": "number" },
        "Ghost": { "type": "number" },
        "Grass": { "type": "number" },
        "Ground": { "type": "number" },
        "Ice": { "type": "number" },
        "Normal": { "type": "number" },
        "Poison": { "type": "number" },
        "Psychic": { "type": "number" },
        "Rock": { "type": "number" },
        "Steel": { "type": "number" },
        "Water": { "type": "number" }
      },
      "required": [
        "Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting", "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice", "Normal", "Poison", "Psychic", "Rock", "Steel", "Water"
      ]
    },
    "Fairy": {
      "type": "object",
      "properties": {
        "Bug": { "type": "number" },
        "Dark": { "type": "number" },
        "Dragon": { "type": "number" },
        "Electric": { "type": "number" },
        "Fairy": { "type": "number" },
        "Fighting": { "type": "number" },
        "Fire": { "type": "number" },
        "Flying": { "type": "number" },
        "Ghost": { "type": "number" },
        "Grass": { "type": "number" },
        "Ground": { "type": "number" },
        "Ice": { "type": "number" },
        "Normal": { "type": "number" },
        "Poison": { "type": "number" },
        "Psychic": { "type": "number" },
        "Rock": { "type": "number" },
        "Steel": { "type": "number" },
        "Water": { "type": "number" }
      },
      "required": [
        "Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting", "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice", "Normal", "Poison", "Psychic", "Rock", "Steel", "Water"
      ]
    },
    "Fighting": {
      "type": "object",
      "properties": {
        "Bug": { "type": "number" },
        "Dark": { "type": "number" },
        "Dragon": { "type": "number" },
        "Electric": { "type": "number" },
        "Fairy": { "type": "number" },
        "Fighting": { "type": "number" },
        "Fire": { "type": "number" },
        "Flying": { "type": "number" },
        "Ghost": { "type": "number" },
        "Grass": { "type": "number" },
        "Ground": { "type": "number" },
        "Ice": { "type": "number" },
        "Normal": { "type": "number" },
        "Poison": { "type": "number" },
        "Psychic": { "type": "number" },
        "Rock": { "type": "number" },
        "Steel": { "type": "number" },
        "Water": { "type": "number" }
      },
      "required": [
        "Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting", "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice", "Normal", "Poison", "Psychic", "Rock", "Steel", "Water"
      ]
    },
    "Fire": {
      "type": "object",
      "properties": {
        "Bug": { "type": "number" },
        "Dark": { "type": "number" },
        "Dragon": { "type": "number" },
        "Electric": { "type": "number" },
        "Fairy": { "type": "number" },
        "Fighting": { "type": "number" },
        "Fire": { "type": "number" },
        "Flying": { "type": "number" },
        "Ghost": { "type": "number" },
        "Grass": { "type": "number" },
        "Ground": { "type": "number" },
        "Ice": { "type": "number" },
        "Normal": { "type": "number" },
        "Poison": { "type": "number" },
        "Psychic": { "type": "number" },
        "Rock": { "type": "number" },
        "Steel": { "type": "number" },
        "Water": { "type": "number" }
      },
      "required": [
        "Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting", "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice", "Normal", "Poison", "Psychic", "Rock", "Steel", "Water"
      ]
    },
    "Flying": {
      "type": "object",
      "properties": {
        "Bug": { "type": "number" },
        "Dark": { "type": "number" },
        "Dragon": { "type": "number" },
        "Electric": { "type": "number" },
        "Fairy": { "type": "number" },
        "Fighting": { "type": "number" },
        "Fire": { "type": "number" },
        "Flying": { "type": "number" },
        "Ghost": { "type": "number" },
        "Grass": { "type": "number" },
        "Ground": { "type": "number" },
        "Ice": { "type": "number" },
        "Normal": { "type": "number" },
        "Poison": { "type": "number" },
        "Psychic": { "type": "number" },
        "Rock": { "type": "number" },
        "Steel": { "type": "number" },
        "Water": { "type": "number" }
      },
      "required": [
        "Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting", "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice", "Normal", "Poison", "Psychic", "Rock", "Steel", "Water"
      ]
    },
    "Ghost": {
      "type": "object",
      "properties": {
        "Bug": { "type": "number" },
        "Dark": { "type": "number" },
        "Dragon": { "type": "number" },
        "Electric": { "type": "number" },
        "Fairy": { "type": "number" },
        "Fighting": { "type": "number" },
        "Fire": { "type": "number" },
        "Flying": { "type": "number" },
        "Ghost": { "type": "number" },
        "Grass": { "type": "number" },
        "Ground": { "type": "number" },
        "Ice": { "type": "number" },
        "Normal": { "type": "number" },
        "Poison": { "type": "number" },
        "Psychic": { "type": "number" },
        "Rock": { "type": "number" },
        "Steel": { "type": "number" },
        "Water": { "type": "number" }
      },
      "required": [
        "Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting", "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice", "Normal", "Poison", "Psychic", "Rock", "Steel", "Water"
      ]
    },
    "Grass": {
      "type": "object",
      "properties": {
        "Bug": { "type": "number" },
        "Dark": { "type": "number" },
        "Dragon": { "type": "number" },
        "Electric": { "type": "number" },
        "Fairy": { "type": "number" },
        "Fighting": { "type": "number" },
        "Fire": { "type": "number" },
        "Flying": { "type": "number" },
        "Ghost": { "type": "number" },
        "Grass": { "type": "number" },
        "Ground": { "type": "number" },
        "Ice": { "type": "number" },
        "Normal": { "type": "number" },
        "Poison": { "type": "number" },
        "Psychic": { "type": "number" },
        "Rock": { "type": "number" },
        "Steel": { "type": "number" },
        "Water": { "type": "number" }
      },
      "required": [
        "Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting", "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice", "Normal", "Poison", "Psychic", "Rock", "Steel", "Water"
      ]
    },
    "Ground": {
      "type": "object",
      "properties": {
        "Bug": { "type": "number" },
        "Dark": { "type": "number" },
        "Dragon": { "type": "number" },
        "Electric": { "type": "number" },
        "Fairy": { "type": "number" },
        "Fighting": { "type": "number" },
        "Fire": { "type": "number" },
        "Flying": { "type": "number" },
        "Ghost": { "type": "number" },
        "Grass": { "type": "number" },
        "Ground": { "type": "number" },
        "Ice": { "type": "number" },
        "Normal": { "type": "number" },
        "Poison": { "type": "number" },
        "Psychic": { "type": "number" },
        "Rock": { "type": "number" },
        "Steel": { "type": "number" },
        "Water": { "type": "number" }
      },
      "required": [
        "Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting", "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice", "Normal", "Poison", "Psychic", "Rock", "Steel", "Water"
      ]
    },
    "Ice": {
      "type": "object",
      "properties": {
        "Bug": { "type": "number" },
        "Dark": { "type": "number" },
        "Dragon": { "type": "number" },
        "Electric": { "type": "number" },
        "Fairy": { "type": "number" },
        "Fighting": { "type": "number" },
        "Fire": { "type": "number" },
        "Flying": { "type": "number" },
        "Ghost": { "type": "number" },
        "Grass": { "type": "number" },
        "Ground": { "type": "number" },
        "Ice": { "type": "number" },
        "Normal": { "type": "number" },
        "Poison": { "type": "number" },
        "Psychic": { "type": "number" },
        "Rock": { "type": "number" },
        "Steel": { "type": "number" },
        "Water": { "type": "number" }
      },
      "required": [
        "Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting", "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice", "Normal", "Poison", "Psychic", "Rock", "Steel", "Water"
      ]
    },
    "Normal": {},
    "Poison": {},
    "Psychic": {},
    "Rock": {},
    "Steel": {},
    "Water": {}
    ```
    """
    url = "https://pokemon-go1.p.rapidapi.com/type_effectiveness.json"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "pokemon-go1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")