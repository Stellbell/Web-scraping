import pymongo
from bs4 import BeautifulSoup
import requests
import scrapy

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.marsmissionDB

