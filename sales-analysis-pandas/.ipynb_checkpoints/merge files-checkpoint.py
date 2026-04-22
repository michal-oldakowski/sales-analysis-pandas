{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9362ae06-38a7-4c2d-b669-e343b4fd5cfb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "80c0f51e-1bbe-4b12-8aed-323e957c7eab",
   "metadata": {},
   "outputs": [],
   "source": [
    "def merge_files():\n",
    "    files = [file for file in os.listdir('./SalesAnalysis/Sales_Data')]\n",
    "    all_months_data = pd.DataFrame()\n",
    "\n",
    "    for file in files:\n",
    "        df = pd.read_csv('./SalesAnalysis/Sales_Data/'+file)\n",
    "        all_months_data = pd.concat([all_months_data, df])\n",
    "\n",
    "    all_months_data.to_csv('all_data.csv', index=False)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "bb313f97-57d5-489b-8060-603e04d73df5",
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    merge_files()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "68650fae-ecd1-4093-96ed-454f572d18a4",
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
   "version": "3.13.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
