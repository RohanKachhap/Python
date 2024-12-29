{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a176fb83-da70-42c8-8094-66ca5c305e0f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate_bmi(weight, height):\n",
    "    if height <= 0:\n",
    "        return None\n",
    "    return weight / (height ** 2)\n",
    "\n",
    "def classify_bmi(bmi):\n",
    "    if bmi < 18.5:\n",
    "        return \"Underweight\"\n",
    "    elif 18.5 <= bmi < 24.9:\n",
    "        return \"Normal weight\"\n",
    "    elif 25 <= bmi < 29.9:\n",
    "        return \"Overweight\"\n",
    "    else:\n",
    "        return \"Obesity\"\n",
    "\n",
    "def main():\n",
    "    print(\"Welcome to the BMI Calculator for India!\")\n",
    "    \n",
    "    while True:\n",
    "        try:\n",
    "            weight = float(input(\"Please enter your weight in kilograms (kg): \"))\n",
    "            if weight <= 0:\n",
    "                print(\"Weight must be a positive number. Try again.\")\n",
    "            else:\n",
    "                break\n",
    "        except ValueError:\n",
    "            print(\"Invalid input. Please enter a numeric value for weight.\")\n",
    "\n",
    "    while True:\n",
    "        try:\n",
    "            height = float(input(\"Please enter your height in meters (m): \"))\n",
    "            if height <= 0:\n",
    "                print(\"Height must be a positive number. Try again.\")\n",
    "            else:\n",
    "                break\n",
    "        except ValueError:\n",
    "            print(\"Invalid input. Please enter a numeric value for height.\")\n",
    "\n",
    "    bmi = calculate_bmi(weight, height)\n",
    "\n",
    "    if bmi is None:\n",
    "        print(\"Height must be greater than zero for BMI calculation.\")\n",
    "    else:\n",
    "        category = classify_bmi(bmi)\n",
    "        print(f\"\\nYour BMI is: {bmi:.2f}\")\n",
    "        print(f\"You are classified as: {category}\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6536b38f-6b59-4f67-b9c1-0b6349480f40",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
