{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "74d1b72a-055f-445c-8d7e-a50b4df95b95",
   "metadata": {},
   "outputs": [],
   "source": [
    "## Unit 2 | Homework Assignment: Automate Your Day Job with Python ##\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "099b50e5-e192-485f-8ad8-42954d9362b0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import libraries and dependencies\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "from pathlib import Path\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "ec25a855-e71f-40dd-a369-b81f2bba5647",
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
       "      <th>Date</th>\n",
       "      <th>Profit/Losses</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>32</th>\n",
       "      <td>Sep-2012</td>\n",
       "      <td>475062</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>Aug-2011</td>\n",
       "      <td>668179</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>Sep-2011</td>\n",
       "      <td>899906</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44</th>\n",
       "      <td>Sep-2013</td>\n",
       "      <td>-1196225</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30</th>\n",
       "      <td>Jul-2012</td>\n",
       "      <td>506702</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>81</th>\n",
       "      <td>Oct-2016</td>\n",
       "      <td>102685</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>85</th>\n",
       "      <td>Feb-2017</td>\n",
       "      <td>671099</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mar-2010</td>\n",
       "      <td>322013</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>83</th>\n",
       "      <td>Dec-2016</td>\n",
       "      <td>60988</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>34</th>\n",
       "      <td>Nov-2012</td>\n",
       "      <td>144175</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Date  Profit/Losses\n",
       "32  Sep-2012         475062\n",
       "19  Aug-2011         668179\n",
       "20  Sep-2011         899906\n",
       "44  Sep-2013       -1196225\n",
       "30  Jul-2012         506702\n",
       "81  Oct-2016         102685\n",
       "85  Feb-2017         671099\n",
       "2   Mar-2010         322013\n",
       "83  Dec-2016          60988\n",
       "34  Nov-2012         144175"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Set the path\n",
    "file_path = Path(\"Resources/budget_data.csv\")\n",
    "# Read in the CSV as a DataFrame\n",
    "budget_csv = pd.read_csv(file_path)\n",
    "budget_csv.sample(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "e5d66f16-17bf-4e30-a059-3235744b9146",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculate total number of months included in the dataset\n",
    "total_months = len(budget_csv.index)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "da6cb712-43ea-4aa7-bbd6-521f8b24e6c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculate net total amount of Profit/Losses over the entire period.\n",
    "total_pnl = budget_csv[\"Profit/Losses\"].sum()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "6bd79531-c200-4697-8087-106f62027a18",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Created a shifted column to calculate difference between each data entry in pnl\n",
    "budget_csv['shifted_column'] = budget_csv['Profit/Losses'].shift(1)\n",
    "\n",
    "# Calculate the difference between each data entry\n",
    "budget_csv['difference'] = budget_csv['Profit/Losses'] - budget_csv['shifted_column']\n",
    "\n",
    "# Calulate the outputs required\n",
    "average_change = budget_csv['difference'].mean()\n",
    "greatest_increase = budget_csv['difference'].max()\n",
    "greatest_decrease = budget_csv['difference'].min()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "711367a4-7716-4c2a-822b-cd21a72695f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the results to an external text file\n",
    "with open(\"pybank.txt\", \"w\") as textfile:\n",
    "    print(\"Financial Analysis\", file=textfile)\n",
    "    print(\"----------------------------\", file=textfile)\n",
    "    print(f\"Total Months: {total_months}\", file=textfile)\n",
    "    print(f\"Total: ${total_pnl}\", file=textfile)\n",
    "    print(f\"Average Change: ${average_change:.2f}\", file=textfile)\n",
    "    print(f\"Greatest Increase in Profits: Feb-2012 (${greatest_increase})\", file=textfile)\n",
    "    print(f\"Greatest Decrease in Profits: Sep-2013 (${greatest_decrease})\", file=textfile)      \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ac674ab1-03e7-40ad-85ed-7170166a360c",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
