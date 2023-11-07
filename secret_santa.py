{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0dc522e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import random\n",
    "\n",
    "def secret_santa_pairing(members):\n",
    "    shuffled_members = members.copy()\n",
    "    random.shuffle(shuffled_members)\n",
    "    pairs = []\n",
    "    for i in range(len(members)):\n",
    "        if members[i] == shuffled_members[i]:\n",
    "            return secret_santa_pairing(members)  # Retry if someone is paired with themselves\n",
    "        pairs.append((members[i], shuffled_members[i]))\n",
    "    return pairs\n",
    "\n",
    "st.title('Secret Santa Pairing Generator')\n",
    "\n",
    "if 'pairs' not in st.session_state:\n",
    "    st.session_state['pairs'] = []\n",
    "\n",
    "members = ['Person 1', 'Person 2', 'Person 3', 'Person 4', 'Person 5']\n",
    "\n",
    "if st.button('Generate Secret Santa Pairs'):\n",
    "    st.session_state['pairs'] = secret_santa_pairing(members)\n",
    "\n",
    "if st.session_state['pairs']:\n",
    "    st.write('Here are the Secret Santa pairs:')\n",
    "    for pair in st.session_state['pairs']:\n",
    "        st.write(f'{pair[0]} -> {pair[1]}')\n"
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
