{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "eda3e509",
   "metadata": {},
   "source": [
    "# G2M insight for Cab Investment firm EDA Notebook "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bef66734",
   "metadata": {},
   "source": [
    "# The client"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8823c724",
   "metadata": {},
   "source": [
    "\n",
    "XYZ is a private firm in US. Due to remarkable growth in the Cab Industry in last few years and multiple key players in the market, it is planning for an investment in Cab industry and as per their Go-to-Market(G2M) strategy they want to understand the market before taking final decision."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fe526687",
   "metadata": {},
   "source": [
    "# Project delivery:"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "078dd0eb",
   "metadata": {},
   "source": [
    "You have been provided with multiple data sets that contains information on 2 cab companies. Each file (data set) provided represents different aspects of the customer profile. XYZ is interested in using your actionable insights to help them identify the right company to make their investment.\n",
    "<br>\n",
    "\n",
    "The outcome of your delivery will be a presentation to XYZ’s Executive team. This presentation will be judged based on the visuals provided, the quality of your analysis and the value of your recommendations and insights.</code>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5abb5587",
   "metadata": {},
   "source": [
    "# Data Set:"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b54b2c67",
   "metadata": {},
   "source": [
    "* Cab_Data.csv – this file includes details of transaction for 2 cab companies. \n",
    "* Customer_ID.csv – this is a mapping table that contains a unique identifier which links the customer’s demographic details.\n",
    "* Transaction_ID.csv – this is a mapping table that contains transaction to customer mapping and payment mode.\n",
    "* City.csv – this file contains list of US cities, their population and number of cab users."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6d800695",
   "metadata": {},
   "source": [
    "# Hypothesis Analysis:"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "66ad8cd1",
   "metadata": {},
   "source": [
    "* Does margin proportionally increase with increase in number of customers?\n",
    "* What are the attributes of these customer segments?\n",
    "* Which company has maximum cab users at a particular time period?\n",
    "* What is the business problem?\n",
    "* What are the properties of the data provided (data intake report)\n",
    "* What steps did you take in order to create an applicable data set? How did you prepare and perform your analysis?\n",
    "* What type of analysis did you perform? \n",
    "* Why did you choose to use certain analytical techniques over others?\n",
    "* What were the results?\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "32566643",
   "metadata": {},
   "source": [
    "# Import Library "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d7e44bb5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import datetime\n",
    "import seaborn as sns\n",
    "import requests\n",
    "import io\n",
    "import matplotlib.pyplot as plt\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "739b9b01",
   "metadata": {},
   "source": [
    "# Read CSV Files"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b1d22e3a",
   "metadata": {},
   "outputs": [],
   "source": [
    "url1 = \"https://raw.githubusercontent.com/aperezace20/G2M-insight-for-Cab-Investment-firm-/main/Dataset/Cab_Data.csv\"\n",
    "# Downloading the csv file from GitHub account\n",
    "download = requests.get(url1).content\n",
    "# Reading the data\n",
    "Cab_Data = pd.read_csv(io.StringIO(download.decode('utf-8')))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "63c7f68d",
   "metadata": {},
   "outputs": [],
   "source": [
    "url2 = \"https://raw.githubusercontent.com/aperezace20/G2M-insight-for-Cab-Investment-firm-/main/Dataset/City.csv\" \n",
    "download = requests.get(url2).content\n",
    "City = pd.read_csv(io.StringIO(download.decode('utf-8')))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "262e4b76",
   "metadata": {},
   "outputs": [],
   "source": [
    "url3 = \"https://raw.githubusercontent.com/aperezace20/G2M-insight-for-Cab-Investment-firm-/main/Dataset/Customer_ID.csv\" \n",
    "download = requests.get(url3).content\n",
    "Customer_ID = pd.read_csv(io.StringIO(download.decode('utf-8')))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "63091c32",
   "metadata": {},
   "outputs": [],
   "source": [
    "url4 = \"https://raw.githubusercontent.com/aperezace20/G2M-insight-for-Cab-Investment-firm-/main/Dataset/Transaction_ID.csv\"\n",
    "download = requests.get(url4).content\n",
    "Transaction_ID = pd.read_csv(io.StringIO(download.decode('utf-8')))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "70b09ab6",
   "metadata": {},
   "source": [
    "# Inspecting Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "eeeeec57",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Transaction ID</th>\n",
       "      <th>Date of Travel</th>\n",
       "      <th>Company</th>\n",
       "      <th>City</th>\n",
       "      <th>KM Travelled</th>\n",
       "      <th>Price Charged</th>\n",
       "      <th>Cost of Trip</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>10000011</td>\n",
       "      <td>42377</td>\n",
       "      <td>Pink Cab</td>\n",
       "      <td>ATLANTA GA</td>\n",
       "      <td>30.45</td>\n",
       "      <td>370.95</td>\n",
       "      <td>313.635</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>10000012</td>\n",
       "      <td>42375</td>\n",
       "      <td>Pink Cab</td>\n",
       "      <td>ATLANTA GA</td>\n",
       "      <td>28.62</td>\n",
       "      <td>358.52</td>\n",
       "      <td>334.854</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10000013</td>\n",
       "      <td>42371</td>\n",
       "      <td>Pink Cab</td>\n",
       "      <td>ATLANTA GA</td>\n",
       "      <td>9.04</td>\n",
       "      <td>125.20</td>\n",
       "      <td>97.632</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>10000014</td>\n",
       "      <td>42376</td>\n",
       "      <td>Pink Cab</td>\n",
       "      <td>ATLANTA GA</td>\n",
       "      <td>33.17</td>\n",
       "      <td>377.40</td>\n",
       "      <td>351.602</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>10000015</td>\n",
       "      <td>42372</td>\n",
       "      <td>Pink Cab</td>\n",
       "      <td>ATLANTA GA</td>\n",
       "      <td>8.73</td>\n",
       "      <td>114.62</td>\n",
       "      <td>97.776</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Transaction ID  Date of Travel   Company        City  KM Travelled  \\\n",
       "0        10000011           42377  Pink Cab  ATLANTA GA         30.45   \n",
       "1        10000012           42375  Pink Cab  ATLANTA GA         28.62   \n",
       "2        10000013           42371  Pink Cab  ATLANTA GA          9.04   \n",
       "3        10000014           42376  Pink Cab  ATLANTA GA         33.17   \n",
       "4        10000015           42372  Pink Cab  ATLANTA GA          8.73   \n",
       "\n",
       "   Price Charged  Cost of Trip  \n",
       "0         370.95       313.635  \n",
       "1         358.52       334.854  \n",
       "2         125.20        97.632  \n",
       "3         377.40       351.602  \n",
       "4         114.62        97.776  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Cab_Data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "1200be2b",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Transaction ID</th>\n",
       "      <th>Date of Travel</th>\n",
       "      <th>Company</th>\n",
       "      <th>City</th>\n",
       "      <th>KM Travelled</th>\n",
       "      <th>Price Charged</th>\n",
       "      <th>Cost of Trip</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>359387</th>\n",
       "      <td>10440101</td>\n",
       "      <td>43108</td>\n",
       "      <td>Yellow Cab</td>\n",
       "      <td>WASHINGTON DC</td>\n",
       "      <td>4.80</td>\n",
       "      <td>69.24</td>\n",
       "      <td>63.3600</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>359388</th>\n",
       "      <td>10440104</td>\n",
       "      <td>43104</td>\n",
       "      <td>Yellow Cab</td>\n",
       "      <td>WASHINGTON DC</td>\n",
       "      <td>8.40</td>\n",
       "      <td>113.75</td>\n",
       "      <td>106.8480</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>359389</th>\n",
       "      <td>10440105</td>\n",
       "      <td>43105</td>\n",
       "      <td>Yellow Cab</td>\n",
       "      <td>WASHINGTON DC</td>\n",
       "      <td>27.75</td>\n",
       "      <td>437.07</td>\n",
       "      <td>349.6500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>359390</th>\n",
       "      <td>10440106</td>\n",
       "      <td>43105</td>\n",
       "      <td>Yellow Cab</td>\n",
       "      <td>WASHINGTON DC</td>\n",
       "      <td>8.80</td>\n",
       "      <td>146.19</td>\n",
       "      <td>114.0480</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>359391</th>\n",
       "      <td>10440107</td>\n",
       "      <td>43102</td>\n",
       "      <td>Yellow Cab</td>\n",
       "      <td>WASHINGTON DC</td>\n",
       "      <td>12.76</td>\n",
       "      <td>191.58</td>\n",
       "      <td>177.6192</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Transaction ID  Date of Travel     Company           City  \\\n",
       "359387        10440101           43108  Yellow Cab  WASHINGTON DC   \n",
       "359388        10440104           43104  Yellow Cab  WASHINGTON DC   \n",
       "359389        10440105           43105  Yellow Cab  WASHINGTON DC   \n",
       "359390        10440106           43105  Yellow Cab  WASHINGTON DC   \n",
       "359391        10440107           43102  Yellow Cab  WASHINGTON DC   \n",
       "\n",
       "        KM Travelled  Price Charged  Cost of Trip  \n",
       "359387          4.80          69.24       63.3600  \n",
       "359388          8.40         113.75      106.8480  \n",
       "359389         27.75         437.07      349.6500  \n",
       "359390          8.80         146.19      114.0480  \n",
       "359391         12.76         191.58      177.6192  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Cab_Data.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "320c77ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(359392, 7)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Cab_Data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "7ae62ebc",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Transaction ID    0\n",
       "Date of Travel    0\n",
       "Company           0\n",
       "City              0\n",
       "KM Travelled      0\n",
       "Price Charged     0\n",
       "Cost of Trip      0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Cab_Data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "20693d23",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>City</th>\n",
       "      <th>Population</th>\n",
       "      <th>Users</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>NEW YORK NY</td>\n",
       "      <td>8,405,837</td>\n",
       "      <td>302,149</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>CHICAGO IL</td>\n",
       "      <td>1,955,130</td>\n",
       "      <td>164,468</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>LOS ANGELES CA</td>\n",
       "      <td>1,595,037</td>\n",
       "      <td>144,132</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>MIAMI FL</td>\n",
       "      <td>1,339,155</td>\n",
       "      <td>17,675</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>SILICON VALLEY</td>\n",
       "      <td>1,177,609</td>\n",
       "      <td>27,247</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             City   Population      Users\n",
       "0     NEW YORK NY   8,405,837    302,149 \n",
       "1      CHICAGO IL   1,955,130    164,468 \n",
       "2  LOS ANGELES CA   1,595,037    144,132 \n",
       "3        MIAMI FL   1,339,155     17,675 \n",
       "4  SILICON VALLEY   1,177,609     27,247 "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "City.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "df5332d6",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>City</th>\n",
       "      <th>Population</th>\n",
       "      <th>Users</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>SACRAMENTO CA</td>\n",
       "      <td>545,776</td>\n",
       "      <td>7,044</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>PITTSBURGH PA</td>\n",
       "      <td>542,085</td>\n",
       "      <td>3,643</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>WASHINGTON DC</td>\n",
       "      <td>418,859</td>\n",
       "      <td>127,001</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>NASHVILLE TN</td>\n",
       "      <td>327,225</td>\n",
       "      <td>9,270</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>BOSTON MA</td>\n",
       "      <td>248,968</td>\n",
       "      <td>80,021</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             City Population      Users\n",
       "15  SACRAMENTO CA   545,776      7,044 \n",
       "16  PITTSBURGH PA   542,085      3,643 \n",
       "17  WASHINGTON DC   418,859    127,001 \n",
       "18   NASHVILLE TN   327,225      9,270 \n",
       "19      BOSTON MA   248,968     80,021 "
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "City.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "73aea767",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(20, 3)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "City.shape "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "db1e5b19",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "City          0\n",
       "Population    0\n",
       "Users         0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "City.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "831a7f93",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Customer ID</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Income (USD/Month)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>29290</td>\n",
       "      <td>Male</td>\n",
       "      <td>28</td>\n",
       "      <td>10813</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>27703</td>\n",
       "      <td>Male</td>\n",
       "      <td>27</td>\n",
       "      <td>9237</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>28712</td>\n",
       "      <td>Male</td>\n",
       "      <td>53</td>\n",
       "      <td>11242</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>28020</td>\n",
       "      <td>Male</td>\n",
       "      <td>23</td>\n",
       "      <td>23327</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>27182</td>\n",
       "      <td>Male</td>\n",
       "      <td>33</td>\n",
       "      <td>8536</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Customer ID Gender  Age  Income (USD/Month)\n",
       "0        29290   Male   28               10813\n",
       "1        27703   Male   27                9237\n",
       "2        28712   Male   53               11242\n",
       "3        28020   Male   23               23327\n",
       "4        27182   Male   33                8536"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Customer_ID.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "205390e1",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Customer ID</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Income (USD/Month)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>49166</th>\n",
       "      <td>12490</td>\n",
       "      <td>Male</td>\n",
       "      <td>33</td>\n",
       "      <td>18713</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49167</th>\n",
       "      <td>14971</td>\n",
       "      <td>Male</td>\n",
       "      <td>30</td>\n",
       "      <td>15346</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49168</th>\n",
       "      <td>41414</td>\n",
       "      <td>Male</td>\n",
       "      <td>38</td>\n",
       "      <td>3960</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49169</th>\n",
       "      <td>41677</td>\n",
       "      <td>Male</td>\n",
       "      <td>23</td>\n",
       "      <td>19454</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49170</th>\n",
       "      <td>39761</td>\n",
       "      <td>Female</td>\n",
       "      <td>32</td>\n",
       "      <td>10128</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Customer ID  Gender  Age  Income (USD/Month)\n",
       "49166        12490    Male   33               18713\n",
       "49167        14971    Male   30               15346\n",
       "49168        41414    Male   38                3960\n",
       "49169        41677    Male   23               19454\n",
       "49170        39761  Female   32               10128"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Customer_ID.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "fbf7b545",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(49171, 4)"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Customer_ID.shape "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "53b80eb9",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Customer ID           0\n",
       "Gender                0\n",
       "Age                   0\n",
       "Income (USD/Month)    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Customer_ID.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "c4da6b0a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Transaction ID</th>\n",
       "      <th>Customer ID</th>\n",
       "      <th>Payment_Mode</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>10000011</td>\n",
       "      <td>29290</td>\n",
       "      <td>Card</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>10000012</td>\n",
       "      <td>27703</td>\n",
       "      <td>Card</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10000013</td>\n",
       "      <td>28712</td>\n",
       "      <td>Cash</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>10000014</td>\n",
       "      <td>28020</td>\n",
       "      <td>Cash</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>10000015</td>\n",
       "      <td>27182</td>\n",
       "      <td>Card</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Transaction ID  Customer ID Payment_Mode\n",
       "0        10000011        29290         Card\n",
       "1        10000012        27703         Card\n",
       "2        10000013        28712         Cash\n",
       "3        10000014        28020         Cash\n",
       "4        10000015        27182         Card"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Transaction_ID.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "6c28d0d3",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Transaction ID</th>\n",
       "      <th>Customer ID</th>\n",
       "      <th>Payment_Mode</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>440093</th>\n",
       "      <td>10440104</td>\n",
       "      <td>53286</td>\n",
       "      <td>Cash</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>440094</th>\n",
       "      <td>10440105</td>\n",
       "      <td>52265</td>\n",
       "      <td>Cash</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>440095</th>\n",
       "      <td>10440106</td>\n",
       "      <td>52175</td>\n",
       "      <td>Card</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>440096</th>\n",
       "      <td>10440107</td>\n",
       "      <td>52917</td>\n",
       "      <td>Card</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>440097</th>\n",
       "      <td>10440108</td>\n",
       "      <td>51587</td>\n",
       "      <td>Card</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Transaction ID  Customer ID Payment_Mode\n",
       "440093        10440104        53286         Cash\n",
       "440094        10440105        52265         Cash\n",
       "440095        10440106        52175         Card\n",
       "440096        10440107        52917         Card\n",
       "440097        10440108        51587         Card"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Transaction_ID.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "95349055",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(440098, 3)"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Transaction_ID.shape "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "8355152b",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Transaction ID    0\n",
       "Customer ID       0\n",
       "Payment_Mode      0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Transaction_ID.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bfb07437",
   "metadata": {},
   "source": [
    "# Data Cleaning and Visualization "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7692316e",
   "metadata": {},
   "source": [
    "# 1. Does margin proportionally increase with increase in number of customers?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "995378b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# What cab company is the most popular? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "5fc76624",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Yellow Cab'"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Cab_Data['Company'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "38c5bca9",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Company', ylabel='Count'>"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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e3vx4sWWJCs7O9veV1BQYEmytm3bdt3HR+1ixgq4gjVr1qhRo0a69957FR0drR49emjevHlXrH/ooYfk5eVlb4eEhKi0tNSjZvbs2XrjjTe0efNmtWvX7qrntyxLDofjG/ssLS3V888/rzZt2sjlcsnlcun06dM1Fv1GR0fX2GbGCreLwMBA/fznP1fbtm31ox/9SLm5udq4caMaNWpkvx588EFJ0qeffvqNxysoKFBYWJjCwsLsfREREWrcuLH9v/uePXvq448/1oULF7Rp0yb17NlTPXv21KZNm1RSUqL9+/dfccbK+v9/tORafkY3btyo2NhYNWvWTL6+vnrmmWd0/Phx+8swklSvXj116tTJ3n7wwQc9ekXdQbACrqBXr17Ky8vTvn37dO7cOa1atUqBgYFXrK9fv77HtsPh0IULFzz2/eAHP1B1dbX++te/fuP527Rpc03/Uk1KSlJubq7mzp2rLVu2KC8vT02bNlVlZeU3vvdafikA35Z69eqpXr2v/oTthQsXNGDAAOXl5Xm8Dhw4oB49enzjsa70f0y+vr9Hjx46deqUdu7cqY8//lg9e/ZUTEyMNm3apI0bNyowMFBt27a97PFbt24th8PxjT+jn3/+uR599FFFRkZq5cqVys3N1WuvvSZJNZYWXK5ffkbrHoIVcAU+Pj564IEH1Lx58xqh6UY98sgjysjI0PTp0/XHP/7xqrUJCQnav3+//va3v9UYsyxLbrdbkvTxxx9r7NixevTRR/XQQw/J6XRedoHv1xfTXty+OAMA3G46duyoPXv2qEWLFnrggQc8Xpdb03SpiIgIFRYWeiwA37t3r9xutx2WLq6zmj9/vhwOhyIiIvSDH/xAu3bt0po1a644WyVJTZo0UXx8vF577TWPmaeLTp48KUnasWOHzp8/r9mzZ6tr165q06aNjhw5UqP+/Pnz2rFjh729b98+nTx5kp/ROohgBXzLoqOj9Y9//ENTp07VnDlzrlg3dOhQDRs2TE8++aRmzJihHTt26PPPP9eaNWvUp08fbdy4UZL0wAMPaNmyZSooKNC2bdv01FNPydvbu8bx3nnnHS1atEj79+/XSy+9pJycHI0ePfqWfU7gZowaNUonTpzQk08+qZycHH322WfKzMzUT3/6U1VXV3/j+/v06aP27dvrqaee0s6dO5WTk6NnnnlGMTExHrfcevbsqeXLlysmJkYOh0P+/v6KiIjQ22+/rZ49e171HK+//rqqq6v1yCOPaOXKlTpw4IAKCgr06quv2rfev/vd7+r8+fOaN2+ePvvsMy1btkx/+tOfahyrfv36GjNmjLZt26adO3fq2WefVdeuXfXII49c34VDrSNYAbWge/fuWrt2rSZPnqxXX331sjUOh0MrVqxQamqqVq9erZiYGLVv315TpkzRoEGD7IcqLlq0SGVlZfre976nxMREjR079rK3LF9++WWlp6erffv2Wrp0qdLS0hQREXFLPydwo0JDQ/XPf/5T1dXVio+PV2RkpH7xi1/I5XLpnnu++VfXxb824O/vrx49eqhPnz5q1aqV3n77bY+6Xr16qbq62iNExcTEqLq6+qozVpLUsmVL7dy5U7169dL48eMVGRmp2NhYrV+/XgsWLJAkdejQQampqfrDH/6gyMhIpaWlacaMGTWO1bBhQ/3qV79SQkKCoqOj5e3trfT09Gu4UrjdOKyLK/AAAABwU5ixAgAAMIRgBQAAYAjBCgAAwBCCFQAAgCEEKwAAAEMIVgAAAIYQrAAAAAwhWAEAABhCsAIAADCEYAXgjlNSUqIxY8aoVatWcjqdCgsL04ABA7R+/frabg3AHa5ebTcAACYdOnRI3bt3V+PGjTVz5ky1b99eVVVV+uCDDzRq1Cj9+9//ru0WAdzBmLECcEcZOXKkHA6HcnJy9OMf/1ht2rTRQw89pJSUFGVnZ0uSCgsLNWjQIDVq1Eh+fn4aOnSojh49ah9jypQp6tChgxYtWqT7779fjRo10gsvvKDq6mrNnDlTwcHBCgwM1LRp0zzO7XA4tGDBAvXr10/e3t5q2bKl3nnnHY+aX/3qV2rTpo0aNmyoVq1aafLkyaqqqqpx7mXLlqlFixZyuVx64okndOrUKUnSW2+9paZNm6qiosLjuEOGDNEzzzxj9FoCuH4EKwB3jBMnTigjI0OjRo2Sj49PjfHGjRvLsiwNHjxYJ06c0KZNm5SVlaVPP/1Uw4YN86j99NNP9Y9//EMZGRn6y1/+okWLFumxxx7T4cOHtWnTJv3hD3/Qb3/7WzusXTR58mQNGTJE//rXv/T000/rySefVEFBgT3u6+urJUuWaO/evXrllVe0cOFCzZkzp8a53333Xa1Zs0Zr1qzRpk2b9L//+7+SpJ/85Ceqrq7We++9Z9cfO3ZMa9as0bPPPnvT1xDATbIA4A6xbds2S5K1atWqK9ZkZmZaXl5eVmFhob1vz549liQrJyfHsizLeumll6yGDRta5eXldk18fLzVokULq7q62t4XHh5uzZgxw96WZD3//PMe5+vSpYv1wgsvXLGfmTNnWlFRUfb25c79P//zP1aXLl3s7RdeeMHq16+fvT137lyrVatW1oULF654HgDfDtZYAbhjWJYl6atbcldSUFCgsLAwhYWF2fsiIiLUuHFjFRQUqHPnzpKkFi1ayNfX164JCgqSl5eX7rnnHo99paWlHsePjo6usZ2Xl2dv/9///Z/mzp2r//znPzp9+rTOnz8vPz8/j/dceu6QkBCP8yQnJ6tz58764osv1KxZMy1evFhJSUlX/dwAvh3cCgRwx2jdurUcDofHrbdLWZZ12QBy6f769et7jDscjsvuu3Dhwjf2dfG42dnZeuKJJ9SvXz+tWbNGu3bt0qRJk1RZWelR/03n+d73vqeHH35Yb731lnbu3Kndu3crKSnpG/sAcOsRrADcMZo0aaL4+Hi99tprOnPmTI3xkydPKiIiQoWFhSoqKrL37927V263W23btr3pHi5dc5Wdna0HH3xQkvTPf/5TzZs316RJk9SpUye1bt1an3/++Q2d52c/+5kWL16sRYsWqU+fPh4zcABqD8EKwB3l9ddfV3V1tR555BGtXLlSBw4cUEFBgV599VVFR0erT58+at++vZ566int3LlTOTk5euaZZxQTE6NOnTrd9PnfeecdLVq0SPv379dLL72knJwcjR49WpL0wAMPqLCwUOnp6fr000/16quvavXq1Td0nqeeekpffPGFFi5cqJ/+9Kc33TcAMwhWAO4oLVu21M6dO9WrVy+NHz9ekZGRio2N1fr167VgwQI5HA69++678vf3V48ePdSnTx+1atVKb7/9tpHzv/zyy0pPT1f79u21dOlSpaWlKSIiQpI0aNAg/fKXv9To0aPVoUMHbdmyRZMnT76h8/j5+WnIkCFq1KiRBg8ebKR3ADfPYV1c7QkAuCkOh0OrV6/+1oJObGys2rZtq1dfffVbOR+Ab8a3AgGgjjlx4oQyMzO1YcMGzZ8/v7bbAfA1BCsAqGM6duyosrIy/eEPf1B4eHhttwPga7gVCAAAYAiL1wEAAAwhWAEAABhCsAIAADCEYAUAAGAIwQoAAMAQghUAAIAhBCsAAABDCFYAAACG/D+8eLIBgGvUlQAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.histplot(Cab_Data['Company'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "3a5b677b",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Company', ylabel='Price Charged'>"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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YLz88su4cuUK+vfvj7feeksb/RJpja+vb43TqY9e7ZyIiIxLvQPRJ598gn//+98aXxy2traIjIzE4sWLYW1tjQ8++ACpqamN2iiRtpmZmeGDDz6otjZ//nzuLiMiMmL1/g2vUqmQn59fZfn169el3Q0tWrSQTo0nMga8SjURkXF7ol1mr732Gnbu3ImcnBxcuXIFO3fuxOTJkzFy5EgAQHJyMjw9PRu7VyKtqqysRGRkZLW1yMhIhiIiIiNW70C0Zs0aDBo0CCEhIfDw8IC7uztCQkIwaNAgfPHFFwCAZ555Bl999VWjN0ukTUlJSSguLq62VlxcjKSkJB13REREulKvs8zUajVSU1OxaNEiLF26FH/++SdEUcRTTz2F5s2bS+OeffbZxu6TSOse3O7lSetERGS46hWIzM3NERQUhMzMTLRr1w5du3bVVl9EOufh4QFra2vcvXu3Ss3a2hoeHh4ydEVERLpQ711m3t7e+PPPP7XRC5GssrOzqw1DAHD37l1kZ2fruCMiItKVJ7q565w5c7B3717k5uaiqKhI40FkqNzd3eHt7V1trWvXrnB3d9dxR0REpCv1vlL1kCFDANy/QerDN7oURRGCINR4t3AiQ8Zb/hERGbd6B6LDhw9row8i2WVlZSEjI6PaWkZGBrKysngcERGRkap3IBowYIA2+iCSnZubG2xtbavd9Wtraws3NzcZuiIiIl2odyB64O7du8jKyqpyRWqeeUaGKjs7+7E3d83OzuYMERGRkap3ILp+/TpeffVVxMXFVVvnMURkqNzc3B572j1niIiIjFe9zzILDw9HYWEhkpKSYGVlhfj4eGzatAkdOnTAd999p40eiXTi8uXLjz3t/vLlyzruiIiIdKXeM0SHDh3C7t270bt3b5iZmcHDwwODBw+Gra0toqKi8MILL2ijTyKty83NrbXerl07HXVDRES6VO8Zojt37sDR0REAYGdnh+vXrwO4f8HGtLS0xu2OSId8fX1hbm5ebc3c3By+vr467oiIiHSl3oGoY8eOOHv2LID79yxbs2YNrly5gi+++IL3eiKDlpOTU+MxcGq1Gjk5OTruiIiIdKXeu8zCw8OlXQvz589HUFAQoqOj0bRpU2zcuLGx+yPSmdatWzeoTkREhqvegWj8+PHSz927d8elS5fw+++/w93dHQ4ODo3aHJEu7du3r9b6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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(x='Company',y='Price Charged',data=Cab_Data)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e2604153",
   "metadata": {},
   "source": [
    "# Answer: The margin proportionally does increase because the yellow cab has more customers and charges more than the pink cab."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ea4fb559",
   "metadata": {},
   "source": [
    "# 2. What is the average price charged for Cab companies to customers? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "a64af2a6",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "423.44331125901897"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Cab_Data[\"Price Charged\"].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "85a83dc0",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Transaction ID</th>\n",
       "      <th>Date of Travel</th>\n",
       "      <th>KM Travelled</th>\n",
       "      <th>Price Charged</th>\n",
       "      <th>Cost of Trip</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>3.593920e+05</td>\n",
       "      <td>359392.000000</td>\n",
       "      <td>359392.000000</td>\n",
       "      <td>359392.000000</td>\n",
       "      <td>359392.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>1.022076e+07</td>\n",
       "      <td>42964.067998</td>\n",
       "      <td>22.567254</td>\n",
       "      <td>423.443311</td>\n",
       "      <td>286.190113</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1.268058e+05</td>\n",
       "      <td>307.467197</td>\n",
       "      <td>12.233526</td>\n",
       "      <td>274.378911</td>\n",
       "      <td>157.993661</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000001e+07</td>\n",
       "      <td>42371.000000</td>\n",
       "      <td>1.900000</td>\n",
       "      <td>15.600000</td>\n",
       "      <td>19.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>1.011081e+07</td>\n",
       "      <td>42697.000000</td>\n",
       "      <td>12.000000</td>\n",
       "      <td>206.437500</td>\n",
       "      <td>151.200000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>1.022104e+07</td>\n",
       "      <td>42988.000000</td>\n",
       "      <td>22.440000</td>\n",
       "      <td>386.360000</td>\n",
       "      <td>282.480000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>1.033094e+07</td>\n",
       "      <td>43232.000000</td>\n",
       "      <td>32.960000</td>\n",
       "      <td>583.660000</td>\n",
       "      <td>413.683200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>1.044011e+07</td>\n",
       "      <td>43465.000000</td>\n",
       "      <td>48.000000</td>\n",
       "      <td>2048.030000</td>\n",
       "      <td>691.200000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Transaction ID  Date of Travel   KM Travelled  Price Charged  \\\n",
       "count    3.593920e+05   359392.000000  359392.000000  359392.000000   \n",
       "mean     1.022076e+07    42964.067998      22.567254     423.443311   \n",
       "std      1.268058e+05      307.467197      12.233526     274.378911   \n",
       "min      1.000001e+07    42371.000000       1.900000      15.600000   \n",
       "25%      1.011081e+07    42697.000000      12.000000     206.437500   \n",
       "50%      1.022104e+07    42988.000000      22.440000     386.360000   \n",
       "75%      1.033094e+07    43232.000000      32.960000     583.660000   \n",
       "max      1.044011e+07    43465.000000      48.000000    2048.030000   \n",
       "\n",
       "        Cost of Trip  \n",
       "count  359392.000000  \n",
       "mean      286.190113  \n",
       "std       157.993661  \n",
       "min        19.000000  \n",
       "25%       151.200000  \n",
       "50%       282.480000  \n",
       "75%       413.683200  \n",
       "max       691.200000  "
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Cab_Data.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "87a990e6",
   "metadata": {},
   "source": [
    "# The average price charge for Cab companies is $4.23."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fc3bc200",
   "metadata": {},
   "source": [
    "# KM Travelled and Cost of Trip are correlated."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "57e725cb",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Transaction ID</th>\n",
       "      <th>Date of Travel</th>\n",
       "      <th>KM Travelled</th>\n",
       "      <th>Price Charged</th>\n",
       "      <th>Cost of Trip</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Transaction ID</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.993030</td>\n",
       "      <td>-0.001429</td>\n",
       "      <td>-0.052902</td>\n",
       "      <td>-0.003462</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date of Travel</th>\n",
       "      <td>0.993030</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.001621</td>\n",
       "      <td>-0.055559</td>\n",
       "      <td>-0.004484</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>KM Travelled</th>\n",
       "      <td>-0.001429</td>\n",
       "      <td>-0.001621</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.835753</td>\n",
       "      <td>0.981848</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Price Charged</th>\n",
       "      <td>-0.052902</td>\n",
       "      <td>-0.055559</td>\n",
       "      <td>0.835753</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.859812</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Cost of Trip</th>\n",
       "      <td>-0.003462</td>\n",
       "      <td>-0.004484</td>\n",
       "      <td>0.981848</td>\n",
       "      <td>0.859812</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                Transaction ID  Date of Travel  KM Travelled  Price Charged  \\\n",
       "Transaction ID        1.000000        0.993030     -0.001429      -0.052902   \n",
       "Date of Travel        0.993030        1.000000     -0.001621      -0.055559   \n",
       "KM Travelled         -0.001429       -0.001621      1.000000       0.835753   \n",
       "Price Charged        -0.052902       -0.055559      0.835753       1.000000   \n",
       "Cost of Trip         -0.003462       -0.004484      0.981848       0.859812   \n",
       "\n",
       "                Cost of Trip  \n",
       "Transaction ID     -0.003462  \n",
       "Date of Travel     -0.004484  \n",
       "KM Travelled        0.981848  \n",
       "Price Charged       0.859812  \n",
       "Cost of Trip        1.000000  "
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr = Cab_Data.corr()\n",
    "corr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "bc3437fb",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Correlation Heatmap')"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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rw3qDVMDfVz8txBv/7hHvFE3NdBDWyMDMb6mhgZG9XdFezMTVFcrcPzSVcyI2oG84v86+b5PSIYAAeMH90MbQ30U37qNv89exMbYpEdePnoyHcu6An2ZNnx7OsFYTwc510uwYf9hcRqakZ4OntH/70e5I+cvQUeqhYFOHRHQtwduV1Ti7LV/8VvyKTHOjbLb+CL6L4zo54KFAd4ovnUb8afP48CpjHrnJ2pOXazaInzcf8seTPMbCACIPi7HRzsPtlS2iFoFiVB33CG1uKioKMyaNUuczvSg/pk4tGkyREREDVrc4aWWzgLRfXG2Vv10GaLH2cnsnJbOAtF9i1s6raWz0CySw15rtmP3Xv19sx27qbT4SBQiIiIiIiIiaiWe8kcct+jCskRERERERERErQU7UR5D48aNe+ipPERERERERERNTRAUzfZqDdiJQkRERERERESkBq6JQkRERERERETqecqfTcORKEREREREREREamAnChERERERERGRGjidh4iIiIiIiIjUIihaxwKwzYUjUYiIiIiIiIiI1MCRKERERERERESkHo5EISIiIiIiIiKixnAkChERERERERGpRRA4EoWIiIiIiIiIiBrBThQiIiIiIiIiapW++OIL2NvbQ0dHB25ubkhISLhn/Pj4eLi5uUFHRwcODg7YsGHDfZ2PnShEREREREREpB6F0Hyv+/TTTz9h1qxZ+N///odjx45h4MCBePHFF5Gdna0yflZWFoYOHYqBAwfi2LFjePvttzFjxgxs375d7XOyE4WIiIiIiIiIWp3Vq1djwoQJmDhxIpycnBAeHg4bGxtERESojL9hwwbY2toiPDwcTk5OmDhxIkJDQ7Fq1Sq1z8lOFCIiIiIiIiJSi6CobrZXeXk5SkpKlF7l5eUq81FRUYGUlBQMGTJEKXzIkCFITExUmebvv/+uF9/X1xfJycmorKxUq/zsRCEiIiIiIiKiFrdixQoYGxsrvVasWKEybkFBAaqrq9GuXTul8Hbt2iE3N1dlmtzcXJXxq6qqUFBQoFYe+YhjIiIiIiIiIlJPMz7ieNGiRQgLC1MKk8lk90wjkUiUtgVBqBfWWHxV4Q1hJwoRERERERERtTiZTNZop0mtNm3aQFNTs96ok/z8/HqjTWpZWFiojK+lpQUzMzO1zsvpPERERERERESkFkEQmu11P7S1teHm5oaYmBil8JiYGHh4eKhM4+7uXi/+/v370bt3b0ilUrXOy04UIiIiIiIiImp1wsLC8M0332Djxo2Qy+WYPXs2srOzMXnyZAA104PGjh0rxp88eTIuXbqEsLAwyOVybNy4Ed9++y3mzp2r9jk5nYeIiIiIiIiIWp2goCAUFhZi2bJlyMnJQffu3bF371506NABAJCTk4Ps7Gwxvr29Pfbu3YvZs2dj/fr1sLKywtq1azFy5Ei1z8lOFCIiIiIiIiJSj+L+pt00tylTpmDKlCkq90VFRdUL8/T0RGpq6gOfj9N5iIiIiIiIiIjUwJEoRERERERERKQWQVHd0lloURyJQkRERERERESkBo5EISIiIiIiIiL1CIqWzkGL4kgUIiIiIiIiIiI1sBOFiIiIiIiIiEgNnM5DREREREREROp5zB5x/KhxJAoRERERERERkRo4EoWIiIiIiIiI1MJHHBMRERERERERUaM4EoWIiIiIiIiI1CLwEcdERERERERERNQYdqIQEREREREREamB03mIiIiIiIiISD0CH3FMRERERERERESN4EgUIiIiIiIiIlKPgiNRiIiIiIiIiIioERJBeMonNBHdh/LycqxYsQKLFi2CTCZr6ewQqYX1lloj1ltqbVhnqTVivSW6f+xEIboPJSUlMDY2RnFxMYyMjFo6O0RqYb2l1oj1llob1llqjVhvie4fp/MQEREREREREamBnShERERERERERGpgJwoRERERERERkRrYiUJ0H2QyGZYsWcKFt6hVYb2l1oj1llob1llqjVhvie4fF5YlIiIiIiIiIlIDR6IQEREREREREamBnShERERERERERGpgJwoRERERERERkRrYiULUTC5evAiJRILjx4+3dFboKffVV1/BxsYGGhoaCA8Pb+nsqC0qKgomJiYtnQ16QixduhQ9e/YUt8eNG4eAgICHOmZcXBwkEglu3LjxUMehpjF48GDMmjWrpbPRJHXrUWN7S6rk5ubCx8cH+vr6TVY/2G7Sk4CdKPRISSSSe77GjRvX0ll8IKpumGxsbJCTk4Pu3bs367nrfjFYunSp+H5qaWmhTZs2GDRoEMLDw1FeXt6seXmSjRs3TnxfpVIp2rVrBx8fH2zcuBEKheK+jvUob1ZLSkowbdo0LFiwAFevXsWkSZPq5aWxz2VcXNwjySs1P1Vt1S+//AId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Z2d89NFHWLVqlVJ6MzMzHDp0CKWlpfD09ISbmxu+/vpr8dexN998E126dEHv3r1hbm6Ow4cP18uDtbU19u7diyNHjsDV1RWTJ0/GhAkTsHjx4gd+bxpy+vRpWFpawtbWFoMHD8a2bduwaNEiJCQkcKrEQ4iOjoalpSXs7Ozg5+eH2NhYrF27Frt27RKHTffs2ROrV6/Gxx9/jO7du+OHH37AihUrlI7j4eGByZMnIygoCObm5li5ciUAIDIyEmPHjsWcOXPQpUsXvPLKK0hKSmrwiToSiQQ7d+7EM888g0GDBsHb2xsODg746aefmvV90NDQwNatW5GSkoLu3btj9uzZ+OSTT1TGDQkJwYkTJzBw4EDY2toq7bvf8lLTs7a2Rnx8PG7cuAEfHx/xl9C76evrN1sHCgC12uBatfVpxIgRStM1JBIJ9u7di0GDBiE0NBSOjo4YPXo0Ll68iHbt2qmVj+XLl+Pdd9/FihUr4OTkBF9fX+zevVucqmdra4vt27dj9+7dcHV1xYYNG/Dhhx8+/BtAzSYiIgKvvvoqpkyZgq5du+LNN98URwBYWVnh8OHDqK6uhq+vL7p3746ZM2fC2Ni4wR82JBIJtmzZgtWrV+PXX3+Fp6cnXFxcsHTpUvj7+8PX11etfN1Pna9r9erVcHd3x0svvQRvb28MGDAATk5O0NHREeM01rb2798f33zzDdatW4eePXti//79zXIvQvXZ29sjNTUVXl5emDNnDrp37w4fHx8cPHgQERERABq/tmtqaqKwsBBjx46Fo6MjAgMD8eKLL+K9994D0PA9Rl0BAQH47LPP8Mknn6Bbt2748ssvERkZKa7P8yjp6elhwYIFCA4Ohru7O3R1dbF169ZHng8idUkETowkIiIiImp1ysrKYG1tjU8//RQTJkxo6ewQ3beoqCjMmjVLZSc+0eOKC8sSEREREbUCx44dQ3p6Ovr27Yvi4mIsW7YMAJSmtxERUfNiJwoRERERUSuxatUqZGRkQFtbG25ubkhISFBrAWUiImoanM5DRERERERERKQGLixLRERERERERKQGdqIQEREREREREamBnShERERERERERGpgJwoRERERERERkRrYiUJEREREREREpAZ2ohARERERERERqYGdKEREREREREREamAnChERERERERGRGtiJQkRERERERESkhv8PWO0kyJAnqU4AAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 1400x600 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "plt.figure(figsize=(14, 6))\n",
    "sns.heatmap(corr, annot = True,cmap = sns.diverging_palette(20, 220, n=200))\n",
    "plt.title('Correlation Heatmap')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "79135791",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(359392, 7)\n"
     ]
    }
   ],
   "source": [
    "Cab_Data.dropna(inplace=True)\n",
    "print(Cab_Data.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "e80df088",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Transaction ID</th>\n",
       "      <th>Date of Travel</th>\n",
       "      <th>Company</th>\n",
       "      <th>City</th>\n",
       "      <th>KM Travelled</th>\n",
       "      <th>Price Charged</th>\n",
       "      <th>Cost of Trip</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>10000011</td>\n",
       "      <td>42377</td>\n",
       "      <td>Pink Cab</td>\n",
       "      <td>ATLANTA GA</td>\n",
       "      <td>30.45</td>\n",
       "      <td>370.95</td>\n",
       "      <td>313.635</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>10000012</td>\n",
       "      <td>42375</td>\n",
       "      <td>Pink Cab</td>\n",
       "      <td>ATLANTA GA</td>\n",
       "      <td>28.62</td>\n",
       "      <td>358.52</td>\n",
       "      <td>334.854</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10000013</td>\n",
       "      <td>42371</td>\n",
       "      <td>Pink Cab</td>\n",
       "      <td>ATLANTA GA</td>\n",
       "      <td>9.04</td>\n",
       "      <td>125.20</td>\n",
       "      <td>97.632</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>10000014</td>\n",
       "      <td>42376</td>\n",
       "      <td>Pink Cab</td>\n",
       "      <td>ATLANTA GA</td>\n",
       "      <td>33.17</td>\n",
       "      <td>377.40</td>\n",
       "      <td>351.602</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>10000015</td>\n",
       "      <td>42372</td>\n",
       "      <td>Pink Cab</td>\n",
       "      <td>ATLANTA GA</td>\n",
       "      <td>8.73</td>\n",
       "      <td>114.62</td>\n",
       "      <td>97.776</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Transaction ID  Date of Travel   Company        City  KM Travelled  \\\n",
       "0        10000011           42377  Pink Cab  ATLANTA GA         30.45   \n",
       "1        10000012           42375  Pink Cab  ATLANTA GA         28.62   \n",
       "2        10000013           42371  Pink Cab  ATLANTA GA          9.04   \n",
       "3        10000014           42376  Pink Cab  ATLANTA GA         33.17   \n",
       "4        10000015           42372  Pink Cab  ATLANTA GA          8.73   \n",
       "\n",
       "   Price Charged  Cost of Trip  \n",
       "0         370.95       313.635  \n",
       "1         358.52       334.854  \n",
       "2         125.20        97.632  \n",
       "3         377.40       351.602  \n",
       "4         114.62        97.776  "
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Cab_Data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d33b857c",
   "metadata": {},
   "source": [
    "# 3. Which company has maximum cab users at a particular time period?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "bd25b6f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "for col in Cab_Data.columns:\n",
    "    if ' ' in col:\n",
    "        Cab_Data = Cab_Data.rename(columns={col:col.replace(' ','_')})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "05d1327c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Transaction_ID', 'Date_of_Travel', 'Company', 'City', 'KM_Travelled',\n",
       "       'Price_Charged', 'Cost_of_Trip'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Cab_Data.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "a470c186",
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import datetime, timedelta\n",
    "def to_date_format(n):\n",
    "    date_str =(datetime(1899,12,30) + timedelta(n-1)).strftime(\"%d-%m-%Y\")\n",
    "    date_date =  datetime.strptime(date_str, \"%d-%m-%Y\")\n",
    "    return date_date"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "193af984",
   "metadata": {},
   "outputs": [],
   "source": [
    "Cab_Data['Date_of_Travel'] = Cab_Data['Date_of_Travel'].apply(lambda x:to_date_format(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "06f183c5",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Transaction_ID</th>\n",
       "      <th>Date_of_Travel</th>\n",
       "      <th>Company</th>\n",
       "      <th>City</th>\n",
       "      <th>KM_Travelled</th>\n",
       "      <th>Price_Charged</th>\n",
       "      <th>Cost_of_Trip</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>10000011</td>\n",
       "      <td>2016-01-07</td>\n",
       "      <td>Pink Cab</td>\n",
       "      <td>ATLANTA GA</td>\n",
       "      <td>30.45</td>\n",
       "      <td>370.95</td>\n",
       "      <td>313.635</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>10000012</td>\n",
       "      <td>2016-01-05</td>\n",
       "      <td>Pink Cab</td>\n",
       "      <td>ATLANTA GA</td>\n",
       "      <td>28.62</td>\n",
       "      <td>358.52</td>\n",
       "      <td>334.854</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Transaction_ID Date_of_Travel   Company        City  KM_Travelled  \\\n",
       "0        10000011     2016-01-07  Pink Cab  ATLANTA GA         30.45   \n",
       "1        10000012     2016-01-05  Pink Cab  ATLANTA GA         28.62   \n",
       "\n",
       "   Price_Charged  Cost_of_Trip  \n",
       "0         370.95       313.635  \n",
       "1         358.52       334.854  "
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Cab_Data.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "a6d3a07f",
   "metadata": {},
   "outputs": [],
   "source": [
    "months=[]\n",
    "years =[]\n",
    "for i in range(len(Cab_Data['Date_of_Travel'])):\n",
    "    months.append(Cab_Data['Date_of_Travel'][i].month)\n",
    "    years.append(Cab_Data['Date_of_Travel'][i].year)\n",
    "Cab_Data['Month'] = months\n",
    "Cab_Data['Year'] = years\n",
    "\n",
    "Cab_Data.drop('Date_of_Travel', axis=1, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "ff6ff593",
   "metadata": {},
   "outputs": [],
   "source": [
    "PinkCab = Cab_Data[Cab_Data['Company']=='Pink Cab']\n",
    "YellowCab = Cab_Data[Cab_Data['Company']=='Yellow Cab']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "cf56cc13",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Transaction_ID</th>\n",
       "      <th>Company</th>\n",
       "      <th>City</th>\n",
       "      <th>KM_Travelled</th>\n",
       "      <th>Price_Charged</th>\n",
       "      <th>Cost_of_Trip</th>\n",
       "      <th>Month</th>\n",
       "      <th>Year</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>10000011</td>\n",
       "      <td>Pink Cab</td>\n",
       "      <td>ATLANTA GA</td>\n",
       "      <td>30.45</td>\n",
       "      <td>370.95</td>\n",
       "      <td>313.635</td>\n",
       "      <td>1</td>\n",
       "      <td>2016</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>10000012</td>\n",
       "      <td>Pink Cab</td>\n",
       "      <td>ATLANTA GA</td>\n",
       "      <td>28.62</td>\n",
       "      <td>358.52</td>\n",
       "      <td>334.854</td>\n",
       "      <td>1</td>\n",
       "      <td>2016</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10000013</td>\n",
       "      <td>Pink Cab</td>\n",
       "      <td>ATLANTA GA</td>\n",
       "      <td>9.04</td>\n",
       "      <td>125.20</td>\n",
       "      <td>97.632</td>\n",
       "      <td>1</td>\n",
       "      <td>2016</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Transaction_ID   Company        City  KM_Travelled  Price_Charged  \\\n",
       "0        10000011  Pink Cab  ATLANTA GA         30.45         370.95   \n",
       "1        10000012  Pink Cab  ATLANTA GA         28.62         358.52   \n",
       "2        10000013  Pink Cab  ATLANTA GA          9.04         125.20   \n",
       "\n",
       "   Cost_of_Trip  Month  Year  \n",
       "0       313.635      1  2016  \n",
       "1       334.854      1  2016  \n",
       "2        97.632      1  2016  "
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Cab_Data.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "437e9017",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Month\n",
       "1      4825\n",
       "2      3392\n",
       "3      4228\n",
       "4      4140\n",
       "5      5023\n",
       "6      5820\n",
       "7      6585\n",
       "8      8061\n",
       "9      9647\n",
       "10    10366\n",
       "11    11324\n",
       "12    11300\n",
       "Name: Transaction_ID, dtype: int64"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "plot0 = Cab_Data[Cab_Data.Company=='Pink Cab'].groupby(['Month']).Transaction_ID.count()\n",
    "plot0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "f265468a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABJsAAAIiCAYAAABv4smaAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAABRs0lEQVR4nO3dfbzX8/0/8MfRxelCHarVKUK2pLkcNoqRRckqYy6bhGZ8XeZiLoYp27LZhk1jmGSq4TvC2JpcLF8TkmU0Y8PISExORSr1+f2xW5/fjpMu7F2njvv9dvvcbj6v9/Pzfj/fL+fTrfPo9X6/K0qlUikAAAAAUIAN6rsBAAAAABoOYRMAAAAAhRE2AQAAAFAYYRMAAAAAhRE2AQAAAFAYYRMAAAAAhRE2AQAAAFAYYRMAAAAAhRE2AQAAAFAYYRMAFKyiomKVXn/4wx/qu9VaxowZk4qKivzjH/9Yae0tt9ySbbbZJs2bN09FRUWmT5++xvv7JNliiy3Sv3//NX6cZT+LRx999HK3X3zxxeWaVfm5+Ljee++9DB8+fLnfieHDh6eioiJvvfXWf3WM3r1754QTTii//8Mf/lDr+9ioUaN06NAhhxxySJ599tk6x/84ln2nnnjiiY/d94svvpiTTz45W221VZo3b54WLVpkm222yQUXXJB//vOfq72/1ZnPPffcM8OGDfsYXQPwSde4vhsAgIZmypQptd5/5zvfyYMPPpgHHnig1vhnP/vZtdlWYd58880MHjw4++23X6666qpUVlZmq622qu+2+JhatWqV//3f/82VV16ZVq1alcdLpVLGjBmT1q1bZ+7cuWu0h/feey8jRoxIkvTq1avw/d9555354x//mF/+8pd1to0cOTJ77713Fi1alCeeeCIXX3xx7r///jz99NPZZJNN8vWvfz377bdf4T2tirvvvjuHH3542rVrl5NPPjmf+9znUlFRkaeffjqjR4/OPffckz/96U9r7Pjf+c53su++++Z//ud/0q1btzV2HAAaHmETABRst912q/X+U5/6VDbYYIM64x/23nvvpUWLFmuytUI8//zzWbx4cY488sjstddeK6xdX87pk+yAAw7IbbfdlptvvjnHHXdcefyBBx7ISy+9lOOOOy7XXXddPXb43xs5cmQOPPDAbLLJJnW2de3atfzd3HPPPbPRRhtl6NChGTNmTM4///xsuumm2XTTTdd2y3nppZdy+OGHZ6uttsqDDz6Yqqqq8rYvfelLOfXUUzNhwoQ12sNee+2Vbt265cc//nGuvfbaNXosABoWl9EBQD3o1atXtt122zz00EPp2bNnWrRokWOPPTbJvy9R69OnTzp27JjmzZune/fuOffcc/Puu++WP3/FFVekoqIif//73+vs+5xzzknTpk1rXSZz3333pXfv3mndunVatGiR3XffPffff/9q93300Udnjz32SJIcdthhqaioKK9EOfroo7Phhhvm6aefTp8+fdKqVav07t07SbJo0aJ897vfzdZbb53Kysp86lOfyjHHHJM333yz1v4XL16cs88+O9XV1WnRokX22GOPPP7449liiy1qXer1UZc2fdSlgLfcckt69OiRli1bZsMNN0zfvn3rrAhZ1v/f//737L///tlwww3TuXPnnHnmmVm4cGGt2oULF+biiy9O9+7d06xZs7Rt2zZ77713HnnkkST/vmRr6623TqlUqvW5UqmUz3zmM/nyl7+8SvM9YcKEbL/99mnWrFm23HLL/PSnPy1vmz9/fjbaaKMcf/zxdT73j3/8I40aNcoPf/jDlR6jqqoqBx54YEaPHl1rfPTo0dl9990/ctXa6NGjs8MOO6RZs2Zp06ZNDjzwwFqXnyWrNqf/+Mc/8qlPfSpJMmLEiI+8tO+NN97IEUcckaqqqnTo0CHHHntsampqVnp+f/rTn/L4449n8ODBK61N/n9Y/PLLLydZ/s/assscJ06cmJ122inNmzfP1ltvXWcOl+f111/PzjvvnK5du+Zvf/vbR9Zddtlleffdd3PVVVfVCpqWqaioyEEHHVR+P2nSpBxwwAHZdNNN06xZs3zmM5/J8ccf/5GXy82cOTMHHXRQWrdunaqqqhx55JF1vo9JMnjw4IwfPz7z5s1b6bkBwDLCJgCoJ6+//nqOPPLIDBo0KL/97W9z4oknJkn+9re/Zf/998/111+fiRMnZtiwYbn11lszYMCA8mePPPLING3aNGPGjKm1zyVLlmTs2LEZMGBA2rVrlyQZO3Zs+vTpk9atW+fGG2/MrbfemjZt2qRv376rHThdeOGF+dnPfpbk36tFpkyZkquuuqq8fdGiRRk4cGC+9KUv5c4778yIESOydOnSHHDAAfn+97+fQYMG5Z577sn3v//9TJo0Kb169cqCBQvKnz/uuOPyox/9KEcddVTuvPPOfPWrX81BBx2UOXPmrFaf/2nkyJE54ogj8tnPfja33nprbrrppsybNy9f/OIX85e//KVW7eLFizNw4MD07t07d955Z4499thcfvnl+cEPflCu+eCDD9KvX7985zvfSf/+/TNhwoSMGTMmPXv2zCuvvJIkOe200/Lcc8/Vmd/f/e53eeGFF3LSSSettO/p06dn2LBhOf300zNhwoT07Nkzp512Wn70ox8lSTbccMMce+yxGTduXJ3Q5aqrrkrTpk3LAebKDB06NI8++mg5LHrnnXdy++23Z+jQocutv+SSSzJ06NBss802uf322/OTn/wkf/7zn9OjR486AcrK5rRjx46ZOHFiuY8pU6ZkypQpufDCC2vt56tf/Wq22mqr3HbbbTn33HMzfvz4nH766Ss9t7vvvjuNGjXKnnvuuUpzsSzAXRaAfZSnnnoqZ555Zk4//fTceeed2X777TN06NA89NBDH/mZZ555JrvuumsqKyszZcqUdO3a9SNr77333nTo0GGlKyKXeeGFF9KjR49cffXVuffee/Ptb387jz32WPbYY48sXry4Tv2BBx6Yz3zmM/n1r3+d4cOH54477kjfvn3r1Pbq1SvvvvvuOnePOQDWcSUAYI0aMmRIqWXLlrXG9tprr1KS0v3337/Czy5durS0ePHi0uTJk0tJSk899VR520EHHVTadNNNS0uWLCmP/fa3vy0lKf3mN78plUql0rvvvltq06ZNacCAAbX2u2TJktIOO+xQ+sIXvlAeu+GGG0pJSi+99NIKe3rwwQdLSUr/+7//W+c8k5RGjx5da/xXv/pVKUnptttuqzU+derUUpLSVVddVSqVSqVnn322lKR0+umn16obN25cKUlpyJAh5bGLLrqotLy/xnz4HF555ZVS48aNS6ecckqtunnz5pWqq6tLhx56aJ3+b7311lq1+++/f6lbt27l97/85S9LSUrXXXfd8qanVCr9e3633HLL0gEHHFBrvF+/fqVPf/rTpaVLl37kZ0ulUmnzzTcvVVRUlKZPn15rfN999y21bt269O6775ZKpVLphRdeKG2wwQalyy+/vFyzYMGCUtu2bUvHHHPMCo9RKpVKSUonnXRSaenSpaUuXbqUzjrrrFKpVCr97Gc/K2244YalefPmlX74wx/WmtM5c+aUmjdvXtp///1r7euVV14pVVZWlgYNGlQeW9U5ffPNN0tJShdddFGdHpf9v7700ktrjZ944omlZs2arXQu+/XrV9p6663rjC/7Ob7llltKixcvLr333nulhx56qPSZz3ym1KhRo/J3bXk/a5tvvnmpWbNmpZdffrk8tmDBglKbNm1Kxx9/fHls2c/j1KlTS5MmTSq1bt26dPDBB5cWLFiwwp5LpVKpWbNmpd12222ldcuz7M+Nl19+uZSkdOedd5a3LTufj/qejR07ttb4okWLShUVFaVzzjnnY/UCwCeTlU0AUE823njjfOlLX6oz/uKLL2bQoEGprq5Oo0aN0qRJk/K9kf7zMqVjjjkmr776au67777y2A033JDq6ur069cvSfLII4/k7bffzpAhQ/LBBx+UX0uXLs1+++2XqVOn1ro8rwhf/epXa72/++67s9FGG2XAgAG1ethxxx1TXV1dXjHx4IMPJkm+9rWv1fr8oYcemsaNP95tJn//+9/ngw8+yFFHHVXr2M2aNctee+1VZ7VGRUVFrRVkSbL99tuXL6lK/r06qVmzZitcNbTBBhvk5JNPzt13311e7fTCCy9k4sSJOfHEE1fp6WbbbLNNdthhh1pjgwYNyty5c/Pkk08mSbbccsv0798/V111VfmSvfHjx+df//pXTj755JUeY5lll63ddNNN+eCDD3L99dfn0EMPzYYbblindsqUKVmwYEGdy9w6d+6cL33pS3VWc63KnK6KgQMH1tnH+++/n9mzZ6/wc6+99lrat2//kdsPO+ywNGnSJC1atMiee+6ZJUuW5Ne//nW23377Fe53xx13zGabbVZ+36xZs2y11VbLPa8bb7wx+++/f77+9a/n1ltvTbNmzVa4749j9uzZOeGEE9K5c+c0btw4TZo0yeabb54kdS5vTD76e7bse7hMkyZNstFGG32sJ98B8MnlBuEAUE86duxYZ2z+/Pn54he/mGbNmuW73/1uttpqq7Ro0aJ8f5X/vOSsX79+6dixY2644Yb06dMnc+bMyV133ZXTTjstjRo1SvLv+9wkycEHH/yRfbz99ttp2bJlIefUokWLtG7dutbYG2+8kXfeeSdNmzZd7meW3VPmX//6V5Kkurq61vbGjRunbdu2H6ufZef/+c9/frnbN9ig9r+7tWjRok4QUFlZmffff7/8/s0330ynTp3qfPbDjj322Hz729/Oz3/+84wcOTI/+9nP0rx581W+tO3D8/CfY8vmKvn3JXu9e/fOpEmT0qdPn/zsZz9Ljx49stNOO63ScZY55phjMmLEiIwcOTJPPvlkrrzyyuXWLTv28n5+O3XqlEmTJtUaW5U5XRUf/hmorKxMklrfieVZsGBBOnTo8JHbf/CDH+RLX/pSGjVqlHbt2qVz584fq59lPS2vn5tvvjnNmzfP17/+9VUKGpNks802y0svvbRKtUuXLk2fPn3y2muv5cILL8x2222Xli1bZunSpdltt92W29NHfc/+82drmWbNmq10ngHgPwmbAKCeLO+XzgceeCCvvfZa/vCHP9R60ts777xTp7ZRo0YZPHhwfvrTn+add97J+PHjs3DhwhxzzDHlmmX3bbryyis/8t4vK/pFfHUt75zatWuXtm3blu/L82GtWrVK8v9/eZ81a1atp4Z98MEHdX4BXhZeLFy4sBw6JKlzM+Rl5//rX/+6vMrjv/WpT30qDz/8cJYuXbrCwKmqqipDhgzJL37xi5x11lm54YYbMmjQoGy00UardJxZs2Z95Nh/Bh1f+tKXsu2222bUqFHZcMMN8+STT2bs2LGrd1L598qkffbZJyNGjEi3bt3Ss2fP5dYtO/brr79eZ9trr71WnvN1Rbt27fL2229/5PYtt9wyu+yyyxrtYdy4cbnggguy11575d57782OO+640s/07ds3V155ZR599NGV3rfpmWeeyVNPPZUxY8ZkyJAh5fHlPUBgmY/6ni0vRJszZ8469/8VgHWby+gAYB2yLKz5zwAlSa655prl1h9zzDF5//3386tf/SpjxoxJjx49svXWW5e377777tloo43yl7/8JbvssstyXx+14qgo/fv3z7/+9a8sWbJkucfv1q1bkpSfajdu3Lhan7/11lvzwQcf1BrbYostkiR//vOfa43/5je/qfW+b9++ady4cV544YWPPP/V1a9fv7z//vt1bs6+PKeeemreeuutHHzwwXnnnXdW69K2GTNm5Kmnnqo1Nn78+LRq1arOqqVTTz0199xzT84777x06NAhhxxyyCof5z+deeaZGTBgQJ2bc/+nHj16pHnz5nUCrVdffTUPPPBA+QmEq2NVVyl9HFtvvXVefPHFwve7Otq0aZP7778/3bt3z957751HH310pZ85/fTT07Jly5x44onLfepeqVTKhAkTkqz+nxvJR3/Pln0Pl3nttdfy/vvv57Of/exKewaAZaxsAoB1SM+ePbPxxhvnhBNOyEUXXZQmTZpk3LhxdUKHZbbeeuv06NEjl1xySWbOnJlrr7221vYNN9wwV155ZYYMGZK33347Bx98cNq3b58333wzTz31VN58881cffXVa/ScDj/88IwbNy77779/TjvttHzhC19IkyZN8uqrr+bBBx/MAQcckAMPPDDdu3fPkUcemSuuuCJNmjTJPvvsk2eeeSY/+tGP6lyat//++6dNmzYZOnRoLr744jRu3DhjxozJzJkza9VtscUWufjii3P++efnxRdfzH777ZeNN944b7zxRh5//PG0bNkyI0aMWK3zOeKII3LDDTfkhBNOyHPPPZe99947S5cuzWOPPZbu3bvn8MMPL9dutdVW2W+//fK73/0ue+yxR517MK1Ip06dMnDgwAwfPjwdO3bM2LFjM2nSpPzgBz9IixYtatUeeeSROe+88/LQQw/lggsu+NgBYp8+fdKnT58V1my00Ua58MIL861vfStHHXVUjjjiiPzrX//KiBEj0qxZs1x00UWrfdxWrVpl8803z5133pnevXunTZs2adeuXTlU/G/06tUro0ePzvPPP5+tttrqv97fx9WqVatMnDgxBx10UPbdd9/cdddd2XvvvT+yvkuXLrn55ptz2GGHZccdd8zJJ5+cz33uc0mSv/zlLxk9enRKpVIOPPDAbL311vn0pz+dc889N6VSKW3atMlvfvObOpc0/qfbb789jRs3zr777psZM2bkwgsvzA477JBDDz20Vt2yYGxFvQLAh1nZBADrkLZt2+aee+5JixYtcuSRR+bYY4/NhhtumFtuueUjP3PMMcdk5syZad68eQ477LA624888sg8+OCDmT9/fo4//vjss88+Oe200/Lkk09+rFUoq6tRo0a566678q1vfSu33357DjzwwHzlK1/J97///TRr1izbbbddufb666/PGWeckTFjxmTgwIG59dZbc9ttt2XjjTeutc/WrVtn4sSJadWqVY488siccMIJ2XbbbXP++efXOf55552XX//613n++eczZMiQ9O3bN2effXZefvnl7Lnnnqt9Po0bN85vf/vbnHfeeZkwYUIOOOCAHHXUUXn44YeXe6nesv8nq7OqKfn3Dagvu+yy/PjHP84BBxyQP/7xj7nsssty9tln16lt3rx5BgwYkMaNG+eEE05Y7XNaXeedd15+8Ytf5KmnnspXvvKVnHzyydlmm23yyCOPpGvXrh9rn9dff31atGiRgQMH5vOf/3yGDx9eSK8HHHBANtxww9x5552F7O+/0bx589x5553p27dv9t9///z2t79dYX3//v3z9NNPZ//998/Pf/7z7L///unfv3+uvvrq7L333uWVTU2aNMlvfvObbLXVVjn++ONzxBFHZPbs2bUeHvBht99+e/7617/moIMOyre//e0MGDAg9957b52g8o477sh2221X63sKACtTUVr26BIAgHXUFltskV69eq3SpWvrmq9+9at59NFH849//CNNmjRZI8dYtGhRtthii+yxxx659dZb18gx1mennHJK7r///syYMWOVb9BNMnfu3HTq1CmXX355jjvuuPpuB4D1iJVNAAAFW7hwYaZMmZKf/OQnmTBhQr75zW+ukaDpzTffzMMPP5z/+Z//yRtvvJFzzz238GM0BBdccEH++c9/5rbbbqvvVtYrl19+eTbbbLNaDx0AgFXhnk0AAAV7/fXX07Nnz7Ru3TrHH398TjnllDVynHvuuSfHHHNMOnbsmKuuuqrOjcP5tw4dOmTcuHGZM2dOfbeyXmndunXGjBmTxo39ygDA6nEZHQAAAACFcRkdAAAAAIURNgEAAABQGGETAAAAAIVxt7+CLV26NK+99lpatWrl0boAAABAg1EqlTJv3rx06tQpG2zw0euXhE0Fe+2119K5c+f6bgMAAABgjZg5c2Y23XTTj9wubCpYq1atkvx74lu3bl3P3QAAAAAUY+7cuencuXM5+/gowqaCLbt0rnXr1sImAAAAoMFZ2W2D3CAcAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMI0ru8GAAAA4JPsH1fMqu8W1mlbDKuu7xZYTcImAAAAoMF74ydT6ruFdV6H03oUsh+X0QEAAABQGGETAAAAAIURNgEAAABQGGETAAAAAIURNgEAAABQGGETAAAAAIURNgEAAABQGGETAAAAAIURNgEAAABQGGETAAAAAIURNgEAAABQGGETAAAAAIURNgEAAABQGGETAAAAAIURNgEAAABQGGETAAAAAIURNgEAAABQGGETAAAAAIURNgEAAABQGGETAAAAAIURNgEAAABQGGETAAAAAIURNgEAAABQGGETAAAAAIURNgEAAABQGGETAAAAAIURNgEAAABQGGETAAAAAIURNgEAAABQGGETAAAAAIURNgEAAABQGGETAAAAAIURNgEAAABQGGETAAAAAIURNgEAAABQmMb13QAAAADrnt/d8lZ9t7DO63dYu/puAdZJVjYBAAAAUBhhEwAAAACFETYBAAAAUBhhEwAAAACFETYBAAAAUBhhEwAAAACFETYBAAAAUBhhEwAAAACFETYBAAAAUJh6D5seeuihDBgwIJ06dUpFRUXuuOOOWttLpVKGDx+eTp06pXnz5unVq1dmzJhRq2bhwoU55ZRT0q5du7Rs2TIDBw7Mq6++Wqtmzpw5GTx4cKqqqlJVVZXBgwfnnXfeqVXzyiuvZMCAAWnZsmXatWuXU089NYsWLVoTpw0AAADQINV72PTuu+9mhx12yKhRo5a7/dJLL81ll12WUaNGZerUqamurs6+++6befPmlWuGDRuWCRMm5Oabb87DDz+c+fPnp3///lmyZEm5ZtCgQZk+fXomTpyYiRMnZvr06Rk8eHB5+5IlS/LlL3857777bh5++OHcfPPNue2223LmmWeuuZMHAAAAaGAa13cD/fr1S79+/Za7rVQq5Yorrsj555+fgw46KEly4403pkOHDhk/fnyOP/741NTU5Prrr89NN92UffbZJ0kyduzYdO7cOffdd1/69u2bZ599NhMnTsyjjz6aXXfdNUly3XXXpUePHnnuuefSrVu33HvvvfnLX/6SmTNnplOnTkmSH//4xzn66KPzve99L61bt14LswEAAACwfqv3lU0r8tJLL2XWrFnp06dPeayysjJ77bVXHnnkkSTJtGnTsnjx4lo1nTp1yrbbbluumTJlSqqqqspBU5LstttuqaqqqlWz7bbbloOmJOnbt28WLlyYadOmfWSPCxcuzNy5c2u9AAAAAD6p1umwadasWUmSDh061Brv0KFDedusWbPStGnTbLzxxiusad++fZ39t2/fvlbNh4+z8cYbp2nTpuWa5bnkkkvK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AADQIK3zK5u++c1v5txzz83hhx+eJNluu+3y8ssv55JLLsmQIUNSXV2d5N8rkzp27Fj+3OzZs8urnaqrq7No0aLMmTOn1uqm2bNnp2fPnuWaN954o87x33zzzTqrpv5TZWVlKisr//sTBQAAAGgA1vmVTe+991422KB2m40aNcrSpUuTJF26dEl1dXUmTZpU3r5o0aJMnjy5HCTtvPPOadKkSa2a119/Pc8880y5pkePHqmpqcnjjz9ernnsscdSU1NTrgEAAABgxdb5lU0DBgzI9773vWy22WbZZptt8qc//SmXXXZZjj322CT/vvRt2LBhGTlyZLp27ZquXbtm5MiRadGiRQYNGpQkqaqqytChQ3PmmWembdu2adOmTc4666xst9125afTde/ePfvtt1+OO+64XHPNNUmSb3zjG+nfv78n0QEAAACsonU+bLryyitz4YUX5sQTT8zs2bPTqVOnHH/88fn2t79drjn77LOzYMGCnHjiiZkzZ0523XXX3HvvvWnVqlW55vLLL0/jxo1z6KGHZsGCBendu3fGjBmTRo0alWvGjRuXU089tfzUuoEDB2bUqFFr72QBAAAA1nMVpVKpVN9NNCRz585NVVVVampq0rp16/puBwCAtegrv76/vltYp91xcO9C9nPqBA/lWZGfHti5kP387pa3CtlPQ9bvsHaF7OcfV3z0E9BJthhWXch+3vjJlEL205B1OK3HCrevauaxzt+zCQAAAID1h7AJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMI0ru8GAABYs/r/elx9t7DOu/vgr9V3CwDQYKz2yqY///nPeeihh8rv58+fnxNPPDG77bZbvv3tb6dUKhXaIAAAAADrj9UOm84444zcfffd5ffnn39+rrvuuixatCiXXHJJRo0aVWiDAAAAAKw/VjtseuaZZ9KzZ88kSalUyrhx4zJixIg8+eSTOeecczJ69OjCmwQAAABg/bDaYdM777yTdu3aJUmeeuqpzJkzJ4ceemiSpHfv3nnxxReL7RAAAACA9cZqh01t27bNzJkzkyQPPvhgOnTokM985jNJkkWLFrlnEwAAAMAn2Go/je6LX/xihg8fnrfeeiuXX355vvzlL5e3/e1vf0vnzp0LbRAAAACA9cdqr2y65JJLUlFRkdNOOy2VlZX59re/Xd72v//7v9ltt90KbRAAAACA9cdqr2zq0qVL/vrXv+btt99OmzZtam0bNWpUqqurC2sOAAAAgPXLaodNy3w4aEqS7bbb7r9qBgAAAID122pfRpckf/3rX3PEEUekY8eOadq0aZ588skkyYgRI/Lggw8W2iAAAAAA64/VDpumT5+ez3/+85k8eXJ69eqVJUuWlLfNnz8/P//5zwttEAAAAID1x2qHTeeee2623377/P3vf89NN92UUqlU3vaFL3whU6dOLbRBAAAAANYfq33Ppj/+8Y8ZO3ZsWrRoUWtVU5J06NAhs2bNKqw5AAAAANYvq72yqVQqpWnTpsvdNmfOnFRWVv7XTQEAAACwflrtsGn77bfPhAkTlrtt4sSJ2Xnnnf/rpgAAAABYP632ZXSnnXZaBg0alJYtW2bw4MFJkldeeSUPPPBARo8enV//+teFNwkAAADA+mG1w6bDDjssL7zwQoYPH56f/vSnSZKvfvWrady4cUaMGJEBAwYU3iQAAAAA64fVDpuS5Fvf+laOOuqo/P73v88bb7yRdu3apW/fvtl8882L7g8AAACA9chq37NpmU033TRDhw7Nt771rXzjG99Yo0HTP//5zxx55JFp27ZtWrRokR133DHTpk0rby+VShk+fHg6deqU5s2bp1evXpkxY0atfSxcuDCnnHJK2rVrl5YtW2bgwIF59dVXa9XMmTMngwcPTlVVVaqqqjJ48OC88847a+y8AAAAABqa1Q6bXnnllZW+ijRnzpzsvvvuadKkSX73u9/lL3/5S3784x9no402KtdceumlueyyyzJq1KhMnTo11dXV2XfffTNv3rxyzbBhwzJhwoTcfPPNefjhhzN//vz0798/S5YsKdcMGjQo06dPz8SJEzNx4sRMnz69fF8qAAAAAFZutS+j22KLLVJRUbHCmv8McP5bP/jBD9K5c+fccMMNtXpYplQq5Yorrsj555+fgw46KEly4403pkOHDhk/fnyOP/741NTU5Prrr89NN92UffbZJ0kyduzYdO7cOffdd1/69u2bZ599NhMnTsyjjz6aXXfdNUly3XXXpUePHnnuuefSrVu3ws4JAAAAoKFa7bBp9OjRdcKmt956K3fddVdeffXVXHDBBYU1lyR33XVX+vbtm0MOOSSTJ0/OJptskhNPPDHHHXdckuSll17KrFmz0qdPn/JnKisrs9dee+WRRx7J8ccfn2nTpmXx4sW1ajp16pRtt902jzzySPr27ZspU6akqqqqHDQlyW677Zaqqqo88sgjHxk2LVy4MAsXLiy/nzt3bqHnDwAAALA+We2w6eijj17u+JlnnplDDjkkM2fO/G97quXFF1/M1VdfnTPOOCPf+ta38vjjj+fUU09NZWVljjrqqMyaNStJ0qFDh1qf69ChQ15++eUkyaxZs9K0adNsvPHGdWqWfX7WrFlp3759neO3b9++XLM8l1xySUaMGPFfnSMAAABAQ/GxbxC+PEcffXR+8YtfFLnLLF26NDvttFNGjhyZz33uczn++ONz3HHH5eqrr65V9+HVVqVSaaWX+324Znn1K9vPeeedl5qamvKr6LANAAAAYH1SaNj0wQcfFP70to4dO+azn/1srbHu3buXb0ReXV2dJHVWH82ePbu82qm6ujqLFi3KnDlzVljzxhtv1Dn+m2++WWfV1H+qrKxM69ata70AAAAAPqkKCZsWL16cadOm5aKLLsoOO+xQxC7Ldt999zz33HO1xp5//vlsvvnmSZIuXbqkuro6kyZNKm9ftGhRJk+enJ49eyZJdt555zRp0qRWzeuvv55nnnmmXNOjR4/U1NTk8ccfL9c89thjqampKdcAAAAAsGKrfc+mDTbY4CMvK9t4443z+9///r9u6j+dfvrp6dmzZ0aOHJlDDz00jz/+eK699tpce+21Sf596duwYcMycuTIdO3aNV27ds3IkSPTokWLDBo0KElSVVWVoUOH5swzz0zbtm3Tpk2bnHXWWdluu+3KT6fr3r179ttvvxx33HG55pprkiTf+MY30r9/f0+iAwAAAFhFqx02ffvb364TNjVr1ixbbLFF9t9//7Rq1aqw5pLk85//fCZMmJDzzjsvF198cbp06ZIrrrgiX/va18o1Z599dhYsWJATTzwxc+bMya677pp77723Vi+XX355GjdunEMPPTQLFixI7969M2bMmDRq1KhcM27cuJx66qnlp9YNHDgwo0aNKvR8AAAAABqy1Q6bhg8fvgbaWLH+/funf//+H7m9oqIiw4cPX2FvzZo1y5VXXpkrr7zyI2vatGmTsWPH/jetAgAAAHyirXbYBABQlC9P+GF9t7BOu+fAb9Z3CwAAq22VwqaLL754lXdYUVGRCy+88GM3BAAAAMD6a5XCptW5dE7YBAAAAPDJtUph09KlS9d0HwAAAAA0ABvUdwMAAAAANBzCJgAAAAAK87GeRvfQQw/lpz/9aZ599tksWLCg1raKioq88MILhTQHAAAAwPpltVc2Pfzww+ndu3dqamry7LPPZuutt84mm2ySV155JY0bN86ee+65JvoEAAAAYD2w2mHTRRddlGOOOSYTJ05Mknz3u9/N//3f/+XJJ5/M/Pnzc9BBBxXeJAAAAADrh9UOm5555pkceOCBqaioSJIsWbIkSbL99tvnwgsvzMUXX1xshwAAAACsN1Y7bHrvvfey4YYbZoMNNkhlZWXeeuut8ratt946f/nLXwptEAAAAID1x2qHTZtttlneeOONJMlnP/vZ3HPPPeVtkydPTtu2bYvrDgAAAID1yio9je7NN9/Mpz71qSTJXnvtlT/84Q85+OCDc9xxx+XEE0/Ms88+m8rKytx7770588wz12jDAAAAAKy7Vils2mSTTTJw4MAMHTo0I0aMyJw5c5IkJ5xwQt57772MGzcuFRUVueCCC3L++eev0YYBAAAAWHetUth0yCGH5I477siECRPSsWPHHH300TnmmGPy6U9/OmeccUbOOOOMNd0nAAAAAOuBVbpn07hx4/L666/nZz/7WTbZZJOMHDkyW221Vfbee++MHTs277///pruEwAAAID1wCrfILx169Y54YQT8thjj2XGjBk5/fTT89e//jVHHXVUqqur8z//8z+ZOnXqmuwVAAAAgHXcaj+NLkm6d++eH/3oR3n11Vdzxx13pFevXhk9enR22223bL/99kX3CAAAAMB64mOFTcs0atQoAwcOzDXXXJOTTz45STJjxoxCGgMAAABg/bNKNwhfniVLluSuu+7KDTfckIkTJ+aDDz7I9ttvn6FDhxbZHwAAAADrkdUOm2bMmJHRo0dn7Nixeeutt9K6det8/etfz9ChQ7PzzjuviR4BAAAAWE+sUtg0d+7cjB8/PqNHj860adOSJHvuuWeGDh2agw8+OM2aNVujTQIAAACwflilsKm6ujoLFy5Mx44dc+655+bYY4/Npz/96TXdGwAAAADrmVUKm/bbb78MHTo0/fr1ywYb/Ff3FAcAAACgAVulsOn2229f030AAAAA0ABYpgQAAABAYYRNAAAAABRG2AQAAABAYYRNAAAAABRG2AQAAABAYYRNAAAAABSmcX03AADrmmMm7FffLazzbjhwYn23AADAOsrKJgAAAAAKI2wCAAAAoDDCJgAAAAAKI2wCAAAAoDDCJgAAAAAKI2wCAAAAoDCN67uBT6o3rx5b3y2s0z71P0fWdwsAAADAx2BlEwAAAACFETYBAAAAUBhhEwAAAACFETYBAAAAUBhhEwAAAACFETYBAAAAUBhhEwAAAACFETYBAAAAUBhhEwAAAACFETYBAAAAUBhhEwAAAACFETYBAAAAUBhhEwAAAACFETYBAAAAUBhhEwAAAACFETYBAAAAUBhhEwAAAACFETYBAAAAUBhhEwAAAACFETYBAAAAUBhhEwAAAACFETYBAAAAUJjG9d0A0DD8/vr967uFdVrfob+t7xYAAADWCiubAAAAACiMsAkAAACAwgibAAAAACiMezYBrEeuualvfbewTjt+8O/ruwUAAPjEW+9WNl1yySWpqKjIsGHDymOlUinDhw9Pp06d0rx58/Tq1SszZsyo9bmFCxfmlFNOSbt27dKyZcsMHDgwr776aq2aOXPmZPDgwamqqkpVVVUGDx6cd955Zy2cFQAAAEDDsF6FTVOnTs21116b7bffvtb4pZdemssuuyyjRo3K1KlTU11dnX333Tfz5s0r1wwbNiwTJkzIzTffnIcffjjz589P//79s2TJknLNoEGDMn369EycODETJ07M9OnTM3jw4LV2fgAAAADru/UmbJo/f36+9rWv5brrrsvGG29cHi+VSrniiity/vnn56CDDsq2226bG2+8Me+9917Gjx+fJKmpqcn111+fH//4x9lnn33yuc99LmPHjs3TTz+d++67L0ny7LPPZuLEifnFL36RHj16pEePHrnuuuty991357nnnquXcwYAAABY36w3YdNJJ52UL3/5y9lnn31qjb/00kuZNWtW+vTpUx6rrKzMXnvtlUceeSRJMm3atCxevLhWTadOnbLtttuWa6ZMmZKqqqrsuuuu5ZrddtstVVVV5ZrlWbhwYebOnVvrBQAAAPBJtV7cIPzmm2/OtGnT8sQTT9TZNmvWrCRJhw4dao136NAhL7/8crmmadOmtVZELatZ9vlZs2alffv2dfbfvn37cs3yXHLJJRkxYsTqnRAAAABAA7XOr2yaOXNmTjvttIwbNy7NmjX7yLqKiopa70ulUp2xD/twzfLqV7af8847LzU1NeXXzJkzV3hMAAAAgIZsnQ+bpk2bltmzZ2fnnXdO48aN07hx40yePDk//elP07hx4/KKpg+vPpo9e3Z5W3V1dRYtWpQ5c+assOaNN96oc/w333yzzqqp/1RZWZnWrVvXegEAAAB8Uq3zYVPv3r3z9NNPZ/r06eXXLrvskq997WuZPn16ttxyy1RXV2fSpEnlzyxatCiTJ09Oz549kyQ777xzmjRpUqvm9ddfzzPPPFOu6dGjR2pqavL444+Xax577LHU1NSUawAAAABYsXX+nk2tWrXKtttuW2usZcuWadu2bXl82LBhGTlyZLp27ZquXbtm5MiRadGiRQYNGpQkqaqqytChQ3PmmWembdu2adOmTc4666xst9125RuOd+/ePfvtt1+OO+64XHPNNUmSb3zjG+nfv3+6deu2Fs8YAAAAYP21zodNq+Lss8/OggULcuKJJ2bOnDnZddddc++996ZVq1blmssvvzyNGzfOoYcemgULFqR3794ZM2ZMGjVqVK4ZN25cTj311PJT6wYOHJhRo0at9fMBAAAAWF+tl2HTH/7wh1rvKyoqMnz48AwfPvwjP9OsWbNceeWVufLKKz+ypk2bNhk7dmxBXQIAAAB88qzz92wCAAAAYP0hbAIAAACgMMImAAAAAAojbAIAAACgMMImAAAAAAojbAIAAACgMMImAAAAAAojbAIAAACgMMImAAAAAAojbAIAAACgMMImAAAAAAojbAIAAACgMMImAAAAAAojbAIAAACgMMImAAAAAAojbAIAAACgMMImAAAAAArTuL4bgDXplZ8eXN8trNM2O/XX9d0CAAAADYyVTQAAAAAURtgEAAAAQGGETQAAAAAURtgEAAAAQGGETQAAAAAURtgEAAAAQGGETQAAAAAURtgEAAAAQGGETQAAAAAURtgEAAAAQGGETQAAAAAURtgEAAAAQGGETQAAAAAURtgEAAAAQGGETQAAAAAURtgEAAAAQGGETQAAAAAURtgEAAAAQGGETQAAAAAURtgEAAAAQGGETQAAAAAURtgEAAAAQGGETQAAAAAURtgEAAAAQGGETQAAAAAURtgEAAAAQGGETQAAAAAURtgEAAAAQGGETQAAAAAURtgEAAAAQGGETQAAAAAURtgEAAAAQGGETQAAAAAURtgEAAAAQGGETQAAAAAURtgEAAAAQGGETQAAAAAURtgEAAAAQGGETQAAAAAURtgEAAAAQGGETQAAAAAURtgEAAAAQGGETQAAAAAURtgEAAAAQGGETQAAAAAURtgEAAAAQGGETQAAAAAURtgEAAAAQGGETQAAAAAUZp0Pmy655JJ8/vOfT6tWrdK+fft85StfyXPPPVerplQqZfjw4enUqVOaN2+eXr16ZcaMGbVqFi5cmFNOOSXt2rVLy5YtM3DgwLz66qu1aubMmZPBgwenqqoqVVVVGTx4cN555501fYoAAAAADcY6HzZNnjw5J510Uh599NFMmjQpH3zwQfr06ZN33323XHPppZfmsssuy6hRozJ16tRUV1dn3333zbx588o1w4YNy4QJE3LzzTfn4Ycfzvz589O/f/8sWbKkXDNo0KBMnz49EydOzMSJEzN9+vQMHjx4rZ4vAAAAwPqscX03sDITJ06s9f6GG25I+/btM23atOy5554plUq54oorcv755+eggw5Kktx4443p0KFDxo8fn+OPPz41NTW5/vrrc9NNN2WfffZJkowdOzadO3fOfffdl759++bZZ5/NxIkT8+ijj2bXXXdNklx33XXp0aNHnnvuuXTr1m3tnjgAAADAemidX9n0YTU1NUmSNm3aJEleeumlzJo1K3369CnXVFZWZq+99sojjzySJJk2bVoWL15cq6ZTp07ZdtttyzVTpkxJVVVVOWhKkt122y1VVVXlmuVZuHBh5s6dW+sFAAAA8Em1XoVNpVIpZ5xxRvbYY49su+22SZJZs2YlSTp06FCrtkOHDuVts2bNStOmTbPxxhuvsKZ9+/Z1jtm+fftyzfJccskl5Xs8VVVVpXPnzh//BAEAAADWc+tV2HTyySfnz3/+c371q1/V2VZRUVHrfalUqjP2YR+uWV79yvZz3nnnpaampvyaOXPmyk4DAAAAoMFab8KmU045JXfddVcefPDBbLrppuXx6urqJKmz+mj27Nnl1U7V1dVZtGhR5syZs8KaN954o85x33zzzTqrpv5TZWVlWrduXesFAAAA8Em1zodNpVIpJ598cm6//fY88MAD6dKlS63tXbp0SXV1dSZNmlQeW7RoUSZPnpyePXsmSXbeeec0adKkVs3rr7+eZ555plzTo0eP1NTU5PHHHy/XPPbYY6mpqSnXAAAAALBi6/zT6E466aSMHz8+d955Z1q1alVewVRVVZXmzZunoqIiw4YNy8iRI9O1a9d07do1I0eOTIsWLTJo0KBy7dChQ3PmmWembdu2adOmTc4666xst9125afTde/ePfvtt1+OO+64XHPNNUmSb3zjG+nfv78n0QEAAACsonU+bLr66quTJL169ao1fsMNN+Too49Okpx99tlZsGBBTjzxxMyZMye77rpr7r333rRq1apcf/nll6dx48Y59NBDs2DBgvTu3TtjxoxJo0aNyjXjxo3LqaeeWn5q3cCBAzNq1Kg1e4IAAAAADcg6HzaVSqWV1lRUVGT48OEZPnz4R9Y0a9YsV155Za688sqPrGnTpk3Gjh37cdoEAAAAIOvBPZsAAAAAWH8ImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIImwAAAAAojLAJAAAAgMIIm5bjqquuSpcuXdKsWbPsvPPO+b//+7/6bgkAAABgvSBs+pBbbrklw4YNy/nnn58//elP+eIXv5h+/frllVdeqe/WAAAAANZ5wqYPueyyyzJ06NB8/etfT/fu3XPFFVekc+fOufrqq+u7NQAAAIB1XuP6bmBdsmjRokybNi3nnnturfE+ffrkkUceWe5nFi5cmIULF5bf19TUJEnmzp27wmPNW7Dgv+y2YatcyfytqnnvLy5kPw3Vyn5OV8e7C8z1ihQ11wsWfFDIfhqqouZ50XvmeWWKmuvF771fyH4aquLm+b1C9tOQFTfX7xayn4aquD+n5xWyn4aqqHl+zzyv1Ny5TQvZz7z3zfWKzJ3bopD9zHvfn9Er03wlf34s+/OlVCqtsK6itLKKT5DXXnstm2yySf74xz+mZ8+e5fGRI0fmxhtvzHPPPVfnM8OHD8+IESPWZpsAAAAA9WbmzJnZdNNNP3K7lU3LUVFRUet9qVSqM7bMeeedlzPOOKP8funSpXn77bfTtm3bj/zMumbu3Lnp3LlzZs6cmdatW9d3Ow2WeV57zPXaYZ7XHnO9dpjntcM8rz3meu0wz2uPuV47zPPasb7Oc6lUyrx589KpU6cV1gmb/kO7du3SqFGjzJo1q9b47Nmz06FDh+V+prKyMpWVlbXGNtpoozXV4hrVunXr9eqHfH1lntcec712mOe1x1yvHeZ57TDPa4+5XjvM89pjrtcO87x2rI/zXFVVtdIaNwj/D02bNs3OO++cSZMm1RqfNGlSrcvqAAAAAFg+K5s+5IwzzsjgwYOzyy67pEePHrn22mvzyiuv5IQTTqjv1gAAAADWecKmDznssMPyr3/9KxdffHFef/31bLvttvntb3+bzTffvL5bW2MqKytz0UUX1bkckGKZ57XHXK8d5nntMddrh3leO8zz2mOu1w7zvPaY67XDPK8dDX2ePY0OAAAAgMK4ZxMAAAAAhRE2AQAAAFAYYRMAAAAAhRE2AQAAAFAYYdMn2EMPPZQBAwakU6dOqaioyB133FHfLTVIl1xyST7/+c+nVatWad++fb7yla/kueeeq++2Gpyrr74622+/fVq3bp3WrVunR48e+d3vflffbTV4l1xySSoqKjJs2LD6bqXBGT58eCoqKmq9qqur67utBuuf//xnjjzyyLRt2zYtWrTIjjvumGnTptV3Ww3KFltsUednuqKiIieddFJ9t9agfPDBB7ngggvSpUuXNG/ePFtuuWUuvvjiLF26tL5ba5DmzZuXYcOGZfPNN0/z5s3Ts2fPTJ06tb7bWq+t7HeUUqmU4cOHp1OnTmnevHl69eqVGTNm1E+z67mVzfXtt9+evn37pl27dqmoqMj06dPrpc/13YrmefHixTnnnHOy3XbbpWXLlunUqVOOOuqovPbaa/XXcEGETZ9g7777bnbYYYeMGjWqvltp0CZPnpyTTjopjz76aCZNmpQPPvggffr0ybvvvlvfrTUom266ab7//e/niSeeyBNPPJEvfelLOeCAA/zlYw2aOnVqrr322my//fb13UqDtc022+T1118vv55++un6bqlBmjNnTnbfffc0adIkv/vd7/KXv/wlP/7xj7PRRhvVd2sNytSpU2v9PE+aNClJcsghh9RzZw3LD37wg/z85z/PqFGj8uyzz+bSSy/ND3/4w1x55ZX13VqD9PWvfz2TJk3KTTfdlKeffjp9+vTJPvvsk3/+85/13dp6a2W/o1x66aW57LLLMmrUqEydOjXV1dXZd999M2/evLXc6fpvZXP97rvvZvfdd8/3v//9tdxZw7KieX7vvffy5JNP5sILL8yTTz6Z22+/Pc8//3wGDhxYD50Wq6JUKpXquwnqX0VFRSZMmJCvfOUr9d1Kg/fmm2+mffv2mTx5cvbcc8/6bqdBa9OmTX74wx9m6NCh9d1KgzN//vzstNNOueqqq/Ld7343O+64Y6644or6bqtBGT58eO644w7/irgWnHvuufnjH/+Y//u//6vvVj5Rhg0blrvvvjt/+9vfUlFRUd/tNBj9+/dPhw4dcv3115fHvvrVr6ZFixa56aab6rGzhmfBggVp1apV7rzzznz5y18uj++4447p379/vvvd79Zjdw3Dh39HKZVK6dSpU4YNG5ZzzjknSbJw4cJ06NAhP/jBD3L88cfXY7frtxX9PviPf/wjXbp0yZ/+9KfsuOOOa723hmRVfu+eOnVqvvCFL+Tll1/OZptttvaaK5iVTbCW1dTUJPl3EMKasWTJktx88815991306NHj/pup0E66aST8uUvfzn77LNPfbfSoP3tb39Lp06d0qVLlxx++OF58cUX67ulBumuu+7KLrvskkMOOSTt27fP5z73uVx33XX13VaDtmjRoowdOzbHHnusoKlge+yxR+6///48//zzSZKnnnoqDz/8cPbff/967qzh+eCDD7JkyZI0a9as1njz5s3z8MMP11NXDdtLL72UWbNmpU+fPuWxysrK7LXXXnnkkUfqsTMoTk1NTSoqKtb7FdaN67sB+CQplUo544wzsscee2Tbbbet73YanKeffjo9evTI+++/nw033DATJkzIZz/72fpuq8G5+eabM23atDzxxBP13UqDtuuuu+aXv/xlttpqq7zxxhv57ne/m549e2bGjBlp27ZtfbfXoLz44ou5+uqrc8YZZ+Rb3/pWHn/88Zx66qmprKzMUUcdVd/tNUh33HFH3nnnnRx99NH13UqDc84556SmpiZbb711GjVqlCVLluR73/tejjjiiPpurcFp1apVevToke985zvp3r17OnTokF/96ld57LHH0rVr1/pur0GaNWtWkqRDhw61xjt06JCXX365PlqCQr3//vs599xzM2jQoLRu3bq+2/mvCJtgLTr55JPz5z//2b92rSHdunXL9OnT88477+S2227LkCFDMnnyZIFTgWbOnJnTTjst9957b51/yaVY/fr1K//3dtttlx49euTTn/50brzxxpxxxhn12FnDs3Tp0uyyyy4ZOXJkkuRzn/tcZsyYkauvvlrYtIZcf/316devXzp16lTfrTQ4t9xyS8aOHZvx48dnm222yfTp0zNs2LB06tQpQ4YMqe/2Gpybbropxx57bDbZZJM0atQoO+20UwYNGpQnn3yyvltr0D68IrJUKlklyXpv8eLFOfzww7N06dJcddVV9d3Of03YBGvJKaeckrvuuisPPfRQNt100/pup0Fq2rRpPvOZzyRJdtlll0ydOjU/+clPcs0119RzZw3HtGnTMnv27Oy8887lsSVLluShhx7KqFGjsnDhwjRq1KgeO2y4WrZsme222y5/+9vf6ruVBqdjx451Qunu3bvntttuq6eOGraXX3459913X26//fb6bqVB+uY3v5lzzz03hx9+eJJ/h9Uvv/xyLrnkEmHTGvDpT386kydPzrvvvpu5c+emY8eOOeyww9KlS5f6bq1BWvZU1lmzZqVjx47l8dmzZ9dZ7QTrk8WLF+fQQw/NSy+9lAceeGC9X9WUuGcTrHGlUiknn3xybr/99jzwwAP+8rEWlUqlLFy4sL7baFB69+6dp59+OtOnTy+/dtlll3zta1/L9OnTBU1r0MKFC/Pss8/W+ss1xdh9993z3HPP1Rp7/vnns/nmm9dTRw3bDTfckPbt29e6oTLFee+997LBBrX/it+oUaMsXbq0njr6ZGjZsmU6duyYOXPm5Pe//30OOOCA+m6pQerSpUuqq6vLT7NM/n0PuMmTJ6dnz5712Bl8fMuCpr/97W+57777GsztEqxs+gSbP39+/v73v5ffv/TSS5k+fXratGmzXt/1fl1z0kknZfz48bnzzjvTqlWr8rXmVVVVad68eT1313B861vfSr9+/dK5c+fMmzcvN998c/7whz9k4sSJ9d1ag9KqVas69xtr2bJl2rZt6z5kBTvrrLMyYMCAbLbZZpk9e3a++93vZu7cuVYmrAGnn356evbsmZEjR+bQQw/N448/nmuvvTbXXnttfbfW4CxdujQ33HBDhgwZksaN/TV0TRgwYEC+973vZbPNNss222yTP/3pT7nsssty7LHH1ndrDdLvf//7lEqldOvWLX//+9/zzW9+M926dcsxxxxT362tt1b2O8qwYcMycuTIdO3aNV27ds3IkSPTokWLDBo0qB67Xj+tbK7ffvvtvPLKK3nttdeSpPwPM9XV1eVVZqzciua5U6dOOfjgg/Pkk0/m7rvvzpIlS8q/L7Zp0yZNmzatr7b/eyU+sR588MFSkjqvIUOG1HdrDcry5jhJ6YYbbqjv1hqUY489trT55puXmjZtWvrUpz5V6t27d+nee++t77Y+Efbaa6/SaaedVt9tNDiHHXZYqWPHjqUmTZqUOnXqVDrooINKM2bMqO+2Gqzf/OY3pW233bZUWVlZ2nrrrUvXXnttfbfUIP3+978vJSk999xz9d1KgzV37tzSaaedVtpss81KzZo1K2255Zal888/v7Rw4cL6bq1BuuWWW0pbbrllqWnTpqXq6urSSSedVHrnnXfqu6312sp+R1m6dGnpoosuKlVXV5cqKytLe+65Z+npp5+u36bXUyub6xtuuGG52y+66KJ67Xt9s6J5fumllz7y98UHH3ywvlv/r1SUSqXSmgyzAAAAAPjkcM8mAAAAAAojbAIAAACgMMImAAAAAAojbAIAAACgMMImAAAAAAojbAIAAACgMMImAAAAAAojbAIAAACgMMImAIA1aMyYMamoqEhFRUX+8Ic/1NleKpXymc98JhUVFenVq9ca6+ORRx7J8OHD884779TZtsUWW6R///5r7NgAwCeLsAkAYC1o1apVrr/++jrjkydPzgsvvJBWrVqt0eM/8sgjGTFixHLDJgCAIgmbAADWgsMOOyy33XZb5s6dW2v8+uuvT48ePbLZZpvVU2cAAMUSNgEArAVHHHFEkuRXv/pVeaympia33XZbjj322Dr1b7/9dk488cRssskmadq0abbccsucf/75WbhwYa26ioqKnHzyybnpppvSvXv3tGjRIjvssEPuvvvucs3w4cPzzW9+M0nSpUuXj7ysb+LEidlpp53SvHnzbL311hk9enRRpw8AfIIImwAA1oLWrVvn4IMPrhXg/OpXv8oGG2yQww47rFbt+++/n7333ju//OUvc8YZZ+See+7JkUcemUsvvTQHHXRQnX3fc889GTVqVC6++OLcdtttadOmTQ488MC8+OKLSZKvf/3rOeWUU5Ikt99+e6ZMmZIpU6Zkp512Ku/jqaeeyplnnpnTTz89d955Z7bffvsMHTo0Dz300JqYDgCgAWtc3w0AAHxSHHvssdl7770zY8aMbLPNNhk9enQOOeSQOvdruvHGG/PnP/85t956aw455JAkyb777psNN9ww55xzTiZNmpR99923XL9gwYLcd9995f3stNNO6dSpU2699dace+652XTTTcuX6X3uc5/LFltsUae3t956K3/84x/LdXvuuWfuv//+jB8/PnvuueeamA4AoIGysgkAYC3Za6+98ulPfzqjR4/O008/nalTpy73EroHHnggLVu2zMEHH1xr/Oijj06S3H///bXG995771qBVYcOHdK+ffu8/PLLq9zbjjvuWOu+Uc2aNctWW221WvsAAEisbAIAWGsqKipyzDHH5Kc//Wnef//9bLXVVvniF79Yp+5f//pXqqurU1FRUWu8ffv2ady4cf71r3/VGm/btm2dfVRWVmbBggWr3FsR+wAASKxsAgBYq44++ui89dZb+fnPf55jjjlmuTVt27bNG2+8kVKpVGt89uzZ+eCDD9KuXbu10SoAwMcibAIAWIs22WSTfPOb38yAAQMyZMiQ5db07t078+fPzx133FFr/Je//GV5++qqrKxMEiuVAIA1zmV0AABr2fe///0Vbj/qqKPys5/9LEOGDMk//vGPbLfddnn44YczcuTI7L///tlnn31W+5jbbbddkuQnP/lJhgwZkiZNmqRbt251bk4OAPDfsrIJAGAd06xZszz44IP52te+lh/+8Ifp169fxowZk7POOiu33377x9pnr169ct555+U3v/lN9thjj3z+85/PtGnTCu4cACCpKH34ZgAAAAAA8DFZ2QQAAABAYYRNAAAAABRG2AQAAABAYYRNAAAAABRG2AQAAABAYYRNAAAAABRG2AQAAABAYYRNAAAAABRG2AQAAABAYYRNAAAAABRG2AQAAABAYf4fhSFFOk4Qf24AAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 1400x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(14,6))\n",
    "sns.barplot(x=plot0.index,y=plot0.values)\n",
    "plt.title('Travel frequency by Month (Pink Cab)',fontsize = 12)\n",
    "plt.xlabel('Month', fontsize = 12)\n",
    "plt.ylabel('Values',fontsize = 12)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "35fa228d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Month\n",
       "1     17468\n",
       "2     14928\n",
       "3     17516\n",
       "4     17535\n",
       "5     18809\n",
       "6     18656\n",
       "7     21074\n",
       "8     24328\n",
       "9     27356\n",
       "10    29609\n",
       "11    32609\n",
       "12    34793\n",
       "Name: Transaction_ID, dtype: int64"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "plot1 = Cab_Data[Cab_Data.Company=='Yellow Cab'].groupby(['Month']).Transaction_ID.count()\n",
    "plot1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "637009ea",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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4OBgg/UuX35oaKjR/gGIXr166U27efOmaNeunQAgevbsKd58800xbtw44ezsLCwtLcXOnTv16nv16iX16uHhIcaPHy9ef/114ezsLACIL774Qq++rKxMjBo1SgAQjz32mJg4caJ4++23xciRI0XTpk2l+W/atEkAEHPnzjXoOzs7W1hbWwt/f/9Kfz4PboOePXsKBwcH0b9/f/Huu++KESNGiEaNGommTZuKc+fOSfW1tVwh7m9fHx8fce3aNWFhYSEiIyP1xl9//XVhbW0tsrOzhaenp1AqlXrjZWVlYvjw4QKAaN26tZg+fbqYOHGicHJyEgDEJ598ole/du1aAUAMHz5cWFtbixEjRojp06eLzp07S7+H5X7++WcxdepUAUB06NBB+r2dPXu2SEtLE0L8733w4osvCjs7OxESEiLefPNN0aZNGwFAhISEVGs7CCFEhw4dRJMmTURpaanR8Z07dwoAIjAwUAghxKRJkwQA8fHHH0s1NXmvHD582OD9IMT/fl/lbueysjLh5OQk2rdvrzeP8n4BiB9++EGafu7cOQFAvP7661Vuo1deecXoe6YqEyZMEBqNRowePVq89dZbYvLkydJ7ePjw4Qb1np6ewt3dXTz99NOiTZs24q233hLh4eHC3t5eKBQKERsba3Q577//vgAg4uPja9RfQ8cgRbWusiAFQMyaNcvo63777TeDafn5+cLPz0+oVCpRUFAgTV+1apUAIBYuXGjwmvJAcfHiRWnazJkzBQARHR0tysrKpOl5eXmiU6dOwtraWgo2QlQ/SJULDQ0VAKQ/QNVd7/379wsAIigoSG/9ysrKxMSJEwUAsW3bNml6+R/KgQMHinv37knTT58+LaytrWslSIWEhAgAYs2aNXrTMzMzhYeHh2jWrJkoLCyUppf/YerSpYvQ6XTS9F9++UVYWloKHx8fvfl89tlnAoDo16+fuHPnjt7YnTt3xM2bN4UQ98Ovs7OzeOKJJ/R+ZkIIsXTpUgFArFixwuh6PejBn8H//d//6Y2tX79eABB9+/aVptXWcoX4X5ASQojnn39euLi4iOLiYiGEEIWFhaJp06ZixIgRQghhNEht2LBB+hkVFRVJ09PT04Wrq6uwsrISv//+uzS9/PfD0tJSJCYmStPv3bsn/UPi2LFjBtumot+P8veBSqUSv/zyizT9zp07onXr1kKh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J9fpehIREVH9YHZ7pCqTmZkJAHBzc9Ob7ubmhj/++EOqsba2hqOjo0FN+eszMzPh6upqMH9XV1e9moeX4+joCGtra6nGmKKiIhQVFUnP8/Lyqrt6REREVM/Uqz1S5RQKhd5zIYTBtIc9XGOsXk7Nw+bPny+dwK5SqeDh4VFpX0RERFR/1asgpVarAcBgj1BWVpa090itVqO4uBg5OTmV1ty4ccNg/tnZ2Xo1Dy8nJycHJSUlBnuqHjRjxgzodDrpkZ6eXsO1JCIiovqiXgUpLy8vqNVqHDhwQJpWXFyMhIQEdOvWDQDg7+8PKysrvZqMjAycOXNGqgkICIBOp8OJEyekmuPHj0On0+nVnDlzBhkZGVLN/v37oVQq4e/vX2GPSqUSDg4Oeg8iIiJqmMzuHKnbt2/j0qVL0vO0tDSkpKTAyckJLVq0QGRkJObNmwdvb294e3tj3rx5aNy4MUJCQgAAKpUKYWFhmD59OpydneHk5ISoqCj4+flJV/G1adMGAwcORHh4OFauXAkAGD9+PIKDg+Hj4wMACAwMRNu2baHVarFo0SLcunULUVFRCA8PZzgiIiIiAGYYpE6dOoU+ffpIz6dNmwYACA0Nxbp16/D222+jsLAQkyZNQk5ODrp06YL9+/fD3t5ees2yZctgaWmJkSNHorCwEP369cO6detgYWEh1WzatAkRERHS1X1DhgzRu3eVhYUF9u7di0mTJqF79+6wtbVFSEgIFi9eXNebgIiIiOoJswtSvXv3hhCiwnGFQoHo6GhER0dXWGNjY4Ply5dj+fLlFdY4OTkhNja20l5atGiBPXv2VNkzERER/T3Vq3OkiIiIiMwJgxQRERGRTAxSRERERDIxSBERERHJxCBFREREJBODFBEREZFMDFJEREREMjFIEREREcnEIEVEREQkE4MUERERkUwMUkREREQyMUgRERERycQgRURERCQTgxQRERGRTAxSRERERDIxSBERERHJxCBFREREJBODFBEREZFMDFJEREREMjFIEREREcnEIEVEREQkE4MUERERkUwMUkREREQyMUgRERERycQgRURERCQTgxQRERGRTAxSRERERDIxSBERERHJxCBFREREJBODFBEREZFMDFJEREREMjFIEREREcnEIEVEREQkE4MUERERkUwMUkREREQyMUgRERERycQgRURERCQTgxQR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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# plt.figure(figsize=(14,6))\n",
    "sns.barplot(x=plot1.index,y=plot1.values)\n",
    "plt.title('Travel frequency by Month (Yellow Cab)',fontsize = 14)\n",
    "plt.xlabel('Month', fontsize = 14)\n",
    "plt.ylabel('Values',fontsize = 14)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0ab3148f",
   "metadata": {},
   "source": [
    "# Answer: The yellow cab has more customers in December during the holidays compared to the pink cab."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b393bc08",
   "metadata": {},
   "source": [
    "# 4. What are the attributes of these customer segments?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "87d4ba72",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# K-means cluster and silhouette of Age and Income "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "69ed39ee",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Customer ID</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Income (USD/Month)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>29290</td>\n",
       "      <td>Male</td>\n",
       "      <td>28</td>\n",
       "      <td>10813</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>27703</td>\n",
       "      <td>Male</td>\n",
       "      <td>27</td>\n",
       "      <td>9237</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>28712</td>\n",
       "      <td>Male</td>\n",
       "      <td>53</td>\n",
       "      <td>11242</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>28020</td>\n",
       "      <td>Male</td>\n",
       "      <td>23</td>\n",
       "      <td>23327</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>27182</td>\n",
       "      <td>Male</td>\n",
       "      <td>33</td>\n",
       "      <td>8536</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Customer ID Gender  Age  Income (USD/Month)\n",
       "0        29290   Male   28               10813\n",
       "1        27703   Male   27                9237\n",
       "2        28712   Male   53               11242\n",
       "3        28020   Male   23               23327\n",
       "4        27182   Male   33                8536"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Customer_ID.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "e647e47a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Customer ID            int64\n",
       "Gender                object\n",
       "Age                    int64\n",
       "Income (USD/Month)     int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Customer_ID.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "0b7a809c",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "X= Customer_ID.iloc[:, [2,3]].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "7fff8d1b",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[   28, 10813],\n",
       "       [   27,  9237],\n",
       "       [   53, 11242],\n",
       "       ...,\n",
       "       [   38,  3960],\n",
       "       [   23, 19454],\n",
       "       [   32, 10128]], dtype=int64)"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "e47bb545",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-0.58442393, -0.52518936],\n",
       "       [-0.6637957 , -0.72213699],\n",
       "       [ 1.39987038, -0.47157861],\n",
       "       ...,\n",
       "       [ 0.2092938 , -1.38158667],\n",
       "       [-0.98128279,  0.55464856],\n",
       "       [-0.26693684, -0.6107916 ]])"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# standardize features\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "\n",
    "#create a scaler\n",
    "scaler= StandardScaler()\n",
    "\n",
    "# Apply the scaler\n",
    "Customer_ID_std= scaler.fit_transform(X)\n",
    "Customer_ID_std"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "5f4bcdb2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# K-means cluster analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "0043dc24",
   "metadata": {},
   "outputs": [],
   "source": [
    "# import library\n",
    "from sklearn.cluster import KMeans"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "8c402c9c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# elbow method to find the optimal k\n",
    "wcss=[]\n",
    "for i in range(1,11):\n",
    "    kmeans = KMeans(n_clusters=i, init ='k-means++', n_init=10, max_iter=300, random_state=0)\n",
    "    kmeans.fit(Customer_ID_std)\n",
    "    wcss.append(kmeans.inertia_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "d28ea7f5",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "plt.plot(range(1,11),wcss, marker = \"o\")\n",
    "plt.title('Age and Income (USD/Month)')\n",
    "plt.xlabel('Age')\n",
    "plt.ylabel('Income (USD/Month)')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aa352f87",
   "metadata": {},
   "source": [
    "# Answer: People in their 30's that make around 30 thousand take more cabs. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "b97f090b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Silhouette Score for 10 Clusters: 0.3604\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import silhouette_score\n",
    "for n_cluster in [4,5,6,7,8,9,10]:\n",
    "    kmeans = KMeans(n_clusters=n_cluster).fit(Customer_ID_std)\n",
    "\n",
    "silhouette_avg = silhouette_score(Customer_ID_std,kmeans.labels_)\n",
    "\n",
    "print('Silhouette Score for %i Clusters: %0.4f' % (n_cluster, silhouette_avg))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "af20d27e",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "km = KMeans(n_clusters= 5, init= 'k-means++', n_init= 10, max_iter= 300, random_state= 0).fit(Customer_ID_std)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "16acd853",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([3, 3, 0, ..., 3, 1, 3])"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clusters = km.fit_predict(Customer_ID_std)\n",
    "clusters"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "9d002202",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Customer ID</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Income (USD/Month)</th>\n",
       "      <th>label</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>29290</td>\n",
       "      <td>Male</td>\n",
       "      <td>28</td>\n",
       "      <td>10813</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>27703</td>\n",
       "      <td>Male</td>\n",
       "      <td>27</td>\n",
       "      <td>9237</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>28712</td>\n",
       "      <td>Male</td>\n",
       "      <td>53</td>\n",
       "      <td>11242</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>28020</td>\n",
       "      <td>Male</td>\n",
       "      <td>23</td>\n",
       "      <td>23327</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>27182</td>\n",
       "      <td>Male</td>\n",
       "      <td>33</td>\n",
       "      <td>8536</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49166</th>\n",
       "      <td>12490</td>\n",
       "      <td>Male</td>\n",
       "      <td>33</td>\n",
       "      <td>18713</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49167</th>\n",
       "      <td>14971</td>\n",
       "      <td>Male</td>\n",
       "      <td>30</td>\n",
       "      <td>15346</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49168</th>\n",
       "      <td>41414</td>\n",
       "      <td>Male</td>\n",
       "      <td>38</td>\n",
       "      <td>3960</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49169</th>\n",
       "      <td>41677</td>\n",
       "      <td>Male</td>\n",
       "      <td>23</td>\n",
       "      <td>19454</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49170</th>\n",
       "      <td>39761</td>\n",
       "      <td>Female</td>\n",
       "      <td>32</td>\n",
       "      <td>10128</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>49171 rows × 5 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       Customer ID  Gender  Age  Income (USD/Month)  label\n",
       "0            29290    Male   28               10813      3\n",
       "1            27703    Male   27                9237      3\n",
       "2            28712    Male   53               11242      0\n",
       "3            28020    Male   23               23327      2\n",
       "4            27182    Male   33                8536      3\n",
       "...            ...     ...  ...                 ...    ...\n",
       "49166        12490    Male   33               18713      1\n",
       "49167        14971    Male   30               15346      1\n",
       "49168        41414    Male   38                3960      3\n",
       "49169        41677    Male   23               19454      1\n",
       "49170        39761  Female   32               10128      3\n",
       "\n",
       "[49171 rows x 5 columns]"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Customer_ID['label'] = clusters\n",
    "Customer_ID"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "57d0b9b7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>Income (USD/Month)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.432721</td>\n",
       "      <td>-0.794938</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>-0.480465</td>\n",
       "      <td>0.114235</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>-0.485459</td>\n",
       "      <td>1.304642</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>-0.498441</td>\n",
       "      <td>-1.059375</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1.466284</td>\n",
       "      <td>0.864597</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Age  Income (USD/Month)\n",
       "0  1.432721           -0.794938\n",
       "1 -0.480465            0.114235\n",
       "2 -0.485459            1.304642\n",
       "3 -0.498441           -1.059375\n",
       "4  1.466284            0.864597"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "centroids = pd.DataFrame(km.cluster_centers_, columns = ['Age','Income (USD/Month)'])\n",
    "centroids"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "a3beac4b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>Income (USD/Month)</th>\n",
       "      <th>cluster</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.432721</td>\n",
       "      <td>-0.794938</td>\n",
       "      <td>Cluster 0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>-0.480465</td>\n",
       "      <td>0.114235</td>\n",
       "      <td>Cluster 1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>-0.485459</td>\n",
       "      <td>1.304642</td>\n",
       "      <td>Cluster 2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>-0.498441</td>\n",
       "      <td>-1.059375</td>\n",
       "      <td>Cluster 3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1.466284</td>\n",
       "      <td>0.864597</td>\n",
       "      <td>Cluster 4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Age  Income (USD/Month)    cluster\n",
       "0  1.432721           -0.794938  Cluster 0\n",
       "1 -0.480465            0.114235  Cluster 1\n",
       "2 -0.485459            1.304642  Cluster 2\n",
       "3 -0.498441           -1.059375  Cluster 3\n",
       "4  1.466284            0.864597  Cluster 4"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "centroids['cluster'] = ['Cluster {}'.format(i) for i in centroids.index]\n",
    "centroids"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "69dfb4fa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x19bad0cbf70>"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA70AAAGsCAYAAAARyMC7AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAACzDUlEQVR4nOzdeVjc5bk//vfMMAzDMjMQtgATAglDVmASGMxSNSskdW3U1mC1tnq+0dR81XqssbY10Xxzjlt7uphaT3+1rSRq3TUKicEYY5bJAolJCEuAwLCGADNss39+fxAQAoRthmV4v64rF8ww8/BgDHDP/Xnut0gQBAFEREREREREHkg81hsgIiIiIiIichcWvUREREREROSxWPQSERERERGRx2LRS0RERERERB6LRS8RERERERF5LBa9RERERERE5LFY9BIREREREZHH8hrrDbia0+lEVVUVAgICIBKJxno7REREREQ0RgRBQHNzMyIiIiAWs983WXlc0VtVVQW1Wj3W2yAiIiIionGioqICUVFRY70NGiMeV/QGBAQAAD7++GPccMMNY7wbIiIiIiIaK1999RVuueWWrhqBJiePK3o7L2n28/ODQqEY490QEREREdFY8fPzAwAee5zkeGE7EREREREReSwWvUREREREROSxWPQSERERERGRx2LRS0RERERERB6LRS8RERERERF5LBa9RERERERE5LHcWvQeOHAAN998MyIiIiASifDhhx9e8/H79++HSCTq9ef8+fPu3CYRERERERF5KLfm9La2tiIxMRH3338/1q1bN+jnFRQU9MjYDQkJccf2iIiIiIiIyMO5tehds2YN1qxZM+TnhYaGQqVSuX5DRERERERENKm4tegdLq1WC7PZjDlz5uCZZ57BsmXL+n2sxWKBxWLpum0ymQAAdrsdNpvN7XslIiIiIqLxyW63j/UWaBwYV0Xv1KlT8de//hULFy6ExWLBv/71L6xYsQL79+/H9ddf3+dztm/fji1btvS6//jx42hvb3f3lomIiIiIaJw6e/bsWG+BxoFxVfTGx8cjPj6+6/aiRYtQUVGBl156qd+id/PmzXj88ce7bptMJqjVajQ3N0MQBAQGBkKpVEKlUkGlUsHX1xcikcjtXwsREREREY0tuVw+1lugcWBcFb19ue666/Dmm2/2+3GZTAaZTNbr/rNnz6Kh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gb1792LWrFn+8/v27QuZqRqNSqUK6rj31Lffftvv2ygNZAM+9H744Ydobm7Gz372s5BvbG655RZs2bIF7733Hp577jmsXr0aP/vZz1BeXu6frtDxrcjq1avxwx/+EPfffz9+/vOfIyUlBceOHcPu3bvxhz/8Id5vi4iIiIgoYWbPno1Zs2Zh0aJFeO6551BYWIjvvvvOv9/sI488guLiYvz617/G4sWL8eWXX+LFF1/ESy+91KfX7c1n8qlTpyIzMxNffPEFrr/+ev/5Rx99FHfeeSfGjx+P+fPnw2az4eWXX8aJEydw//33A/B1am+99VasXLkSkydPhsFgwFdffYXNmzfjxhtvDHodi8WCmpoauFwunDp1Cm+88QZeeeUVbNq0yR/Sd+7cedFVpD/++GO4XK6I++g+9thjWL9+PS699FJcccUVeO2111BeXo7S0tLu/hpRUFCA1tZW7NmzB1OmTIFOp4NOp+vWc61WKw4ePIhnnnmm26832A34e3q3bNmCa665JiTwAr5Ob3l5OZqbm/HOO+/gvffew+TJk/GnP/3Jv3qzWq0G4Ps267PPPsPx48dx9dVXY+rUqVi7dq1/fjwRERER0VDy7rvvori4GEuXLsWECRPw+OOP+7uH06ZNw9tvv40333wTkyZNwrp167Bx48aLTge+mN58JpfL5Vi5cmVIKLztttuwdetWbNu2DcXFxZg/fz5OnDiBzz//HPn5+QB8qzfPmDEDzz//PGbNmoVJkyZh7dq1+PnPf44XX3wx6Hrr1q1Dbm4uCgsLsWLFCphMJuzZswerV6/2j9m5c2dIWO4qJSUlYuAFgFWrVuGRRx7BI488gssvvxy7du3yb7/aXTNnzsR//Md/YPHixcjMzMTmzZu7/dwdO3YgLy8PV199dbefM9hJItzk/CTw9NNP489//jPOnj2b6FKIiIiIiKgPamtrMXHiRBw8eNAfaOPt0KFDmDdvHurr60Pumx1MSkpK8NBDD4Wdfp2sBvz05u566aWXUFxcjOHDh+OLL77A7373O+7BS0RERESUBLKzs7FlyxZUVVUlLPS63W784Q9/GNSBt66uDrfccguWLl2a6FLiKmk6vQ8//DDeeustNDU1IS8vDytWrMCaNWugUCRNriciIiIiIqIeSprQS0RERERERNTVgF/IioiIiIiIiKi3GHqJiIiIiIgoaTH0EhERERERUdJi6CUiIiIiIqKkxdBLRERERERESYuhl4iIiIiIiJIWQy8RERERERElLYZeIiIiIiIiSlr/HzJEfMWeofgJAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 1000x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "from pandas.plotting import parallel_coordinates\n",
    "#parallel coordinates visualization\n",
    "plt.figure(figsize=(10,5))\n",
    "parallel_coordinates(centroids, class_column='cluster', colormap='Dark2', linewidth=5)\n",
    "plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "638e2a69",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.FacetGrid at 0x19bbab97760>"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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7GDjxo189atf5fnnn+eTn/wk/f393Hrrrbz88svs2LGD559/nosvvpiGhgY+8pGPABAMBrnmmmu45ZZb+POf/8z69ev5//6//4/jjjuOD37wgwAsWLCACy64gGuvvZY1a9awZs0arr32Wi666CLmz3fy7ZctW8bChQtZsWIF69ev589//jO33nor11577ajqgRRLU0VuDItCMZWwpJUTe2Nju262oZ44Add9g0xbFHDcObbzwCKEowRY0sK0TSxpIYSgs2ofSS1OKZHVsf60G2TgZduSeMR0LCSayFnQM99rmkBKxyIgpcTwam6wpy1zrRhSStIGUq8/dwGVactCKg4kHecqJan7Uxjp+20mnDRfM2EhD5ZhNiVrzu84VqK0lUFK52eONWUQhldj95tdyLw+JZg2s3JMxB4K28JxaylGTVldM/v372fFihW0trYSDAY5/vjjefrppzn//POJRqNs3LiR//zP/6Snp4eWlhbOPfdc/ud//ofq6mp3jh/84AcYhsEVV1zhFjS7//773RoiAL/+9a+56aab3OyaSy65hJ/85Cfufl3XeeKJJ7j++us544wzsgqaHQwODx5+UM6jUExWBscGpV03STuJZVuYmJmDSZJEWAYVyRqKCxDJOTGI/MGV4MRb6IOfxDPe+qo86LrmZmL4Ajrh3gQen04ybmGZEk2TGfM5PzVtwEJhJiwnDkITCF24yos9KObCTNiYicK0CSsh6WmPZAeFFvNYmvYHlcLgAGGcmBUz4Vh5sElZfrSB60q7wVLYtsQybTcTKF/mSrCxokRBR+atNW0ccaJ6oBwtE66OyGRmtAXNElaC9/36fcMWwlIoFNlkpnvn46Td5/O+PR9y3T/jRd7aFqmYhnTAZRpNcyqBnnDebF57emdu4Cfgq9SpmVZB74EolmVn1QJBk9hjlaAhBmXsmANKTHrbUO9Hi6aLvBYOj093XFypzKDM2itm0qS/03FfD1VHRNMEf/fZ45izqCFn7rbtPfz2ztdKF34YZs6v5dIvnjyu55jKTLgYkUMRr+7lsqOGzgJSKCYj460ADKeEAARjjZnClIbIeA3CNLPjQEzTdtNO09vTL9uSbuCl7tHQ9IyMnlS8ieHRaZpTRTJmYcbtlAXEcVWMmRJCSh7bdpSdQQHzg5WOsXpcHcrNYiYtjlrciM9vEOlNInCUEwHEw84D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3/3c5z7HG2+8werVq7O2p90tAIsWLeKUU05hzpw5PPHEE1x22WVDzielzMpHH5ybPtoxmdx2223cfPPN7vve3t5RKSMJxj8gVqEoB7Wx0ru9KhQTnd6u0fexUUwQi8iNN97IY489xl/+8hdmzZo17NiWlhbmzJnDtm3bAJg+fTqJRILu7uwOje3t7a6FY/r06ezfn2s66+joyBoz2PLR3d1NMpnMsZSk8fl81NTUZL0UCsUAJnmi/BSKKcaB3X3lFmFSU1ZFRErJ5z73OX73u9/x3HPPMXfu3BGP6ezsZPfu3bS0tACwePFiPB4Pzz77rDumtbWVTZs2cfrppwOwdOlSQqEQr7zyijtm7dq1hEKhrDGbNm2itbXVHfPMM8/g8/lYvHjxmFzvUPjI3ylToZjshD3FtXBXKCYjVkI5H0uhrK6ZG264gd/85jf8/ve/p7q62rVIBINBAoEA/f39fOMb3+CjH/0oLS0t7Nixg6985Ss0NDTwkY98xB17zTXXcMsttzBt2jTq6+u59dZbOe644/jgBz8IwIIFC7jgggu49tpruffeewEnffeiiy5i/vz5ACxbtoyFCxeyYsUK7rrrLrq6urj11lu59tprx93SoU0Mw5RCMeb4ZKDcIigU406wWf2dl0JZV8B77rmHUCjEOeecQ0tLi/v6n//5HwB0XWfjxo18+MMfZt68eVx11VXMmzePl19+merqgQIyP/jBD7j00ku54oorOOOMM6ioqODxxx93a4gA/PrXv+a4445j2bJlLFu2jOOPP54HH3zQ3a/rOk888QR+v58zzjiDK664gksvvZTvf//7434fYij/omJqolwzikOBliOUW74UJlQdkcnOaOuIHPfAceMolUJRPj70+meZFXGsjqKsNdsVivHj+HNnctbH55dbjElLUa6ZUCjEI488wosvvsiOHTuIRCI0NjZy0kknsXz5cjfeQqFQKAD8lip9rZj6tO0YXQ0phUNBrpnW1lauvfZaWlpauP322wmHw5x44omcd955zJo1i7/85S+cf/75LFy40HWrKBQKhW7rIw9SKCY5fZ3KvV4KBVlETjjhBP7+7/+eV155JavYWCbRaJRHH32Uf/u3f2P37t3ceuutYyqoQqGYfAipArEVUx8hVIRDKRSkiGzevJnGxsZhxwQCAT7xiU/wiU98go6OjjERTqFQTG5s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bV544QXeeustt+HeZz/7WR5//HHuv/9+pk2bxi233EJXVxfr1q1DT5m5L7zwQvbs2cPPfvYzAK677joOP/xwHn/8cQAsy+LEE0+ksbGRf/3Xf6Wzs5OrrrqKyy67jLvvvrug6ylVEYHhF+WhFtU0Iy1AwzHceQs593D7R1rcSmEkucbrWIXDb9u/Tpt94gijlEKimNrUTvfzyW+cXm4xJi0FKyKZhEIhnnzySX7/+9/z9NNPU1dX5yolZ599trv4F0tHRwdNTU2sWrWK97///UgpmTFjBl/4whf40pe+BDjWj+bmZu68804+/elPEwqFaGxs5MEHH+TjH/844KQZz549myeffJLly5ezZcsWFi5cyJo1a1iyxNFa16xZw9KlS9m6dSvz58/nqaee4qKLLmL37t2uteehhx5i5cqVtLe3F6RYjIUiolBMJh4/cCu7zEK+gJUyopi6TD+qmo/eemq5xZi0jOoBMBgM8olPfIKHHnqIAwcOcO+992LbNp/61KdobGzMqldfDKFQCHDq4ANs376dtrY2li1b5o7x+XycffbZvPTSS4BTIz+ZTGaNmTFjBosWLXLHvPzyywSDQVcJATjttNMIBoNZYxYtWpTlclq+fDnxeJx169bllTcej9Pb25v1GhVCpUErJidSFTRTKKiqG9+mcFOdki3RhmGwbNky7r77bnbu3Mmf//xn5s2bV/Q8UkpuvvlmzjzzTLeZXltbGwDNzc1ZY5ubm919bW1teL1e6urqhh3T1NSUc86mpqasMYPPU1dXh9frdccM5o477iAYDLqvdIndotErR3ecQlFmkqJQ55/KKlBMXSpqlEJeCkU/im/bto3f//737NixAyEEc+fO5dJLL+WII44A4KSTThqVIJ/73Od44403WL16dc6+wWnDUsoRU4kHj8k3fjRjMrntttu4+eab3fe9vb2jVEbsURyjUJSfen0XbebCkQcqFFMY5XgsjaIsInfccQcLFy7kS1/6Er/97W95+OGH+cd//EeOOeaYIcvKFsKNN97IY489xl/+8pesTJfp06cD5Fgk2tvbXevF9OnTSSQSdHd3Dztm//79Oeft6OjIGjP4PN3d3SSTyRxLSRqfz0dNTU3Wa1SYKvVLMTlp8W0ttwgKRdmRShUpiYIVkb/85S/83//7f/nqV7/KgQMHaG1tpa2tjY6ODr785S/z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3bsX9957LwBApVJhypQpePfdd13lN910k9trbr75ZrffDxw4gFWrViEmJsb1GDNmDJxOJ06cONE1B0JEQUElOgAiCi0rV66E3W7Hdddd53pOlmWo1WqYTCbIsgxJktxe07zj1el04rHHHsOMGTNabJ+DXokiCxMRImo3u92ONWvW4I9//CNGjx7tVvbTn/4Ua9euRW5uLjZt2uRWtn//frffb7zxRhw+fBi9e/cOeMxEFNw4RoSI2u3jjz/GlClTUF1dDYPB4Fb24osvYtOmTdiwYQNycnLw61//Gg8//DBKSkowa9YsVFRUoKamBgaDAQcPHkR+fj4eeughTJ8+HXq9HkePHsW2bdvwn//5n4KOjohE4BgRImq3lStXYtSoUS2SEKCpR6SkpAQmkwl/+9vfsGHDBgwYMABLly513TWj1WoBAAMGDMDOnTtRVlaGW2+9FYMHD8ZLL72E9PT0Lj0eIhKPPSJEFHDz58/H22+/jfLyctGhEFGQ4RgRIup0f/7zn3HTTTchKSkJX375JV5//XXOEUJErWIiQkSdrqysDK+88gouXLiA7t27Y9asWZgzZ47osIgoCPHSDBEREQnDwapEREQkDBMRIiIiEoaJCBEREQnDRISIiIiEYSJCREREwjARISIiImGYiBAREZEwTESIiIhImP8P0y4dTYcYduwAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 558.875x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.lmplot(data=Customer_ID, x='Age', y='Income (USD/Month)', hue='label', fit_reg=False,legend=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
