
    "import numpy as np\n",
    "import pandas as pd\n",
    "import os\n",
    "import matplotlib.pyplot as plt\n",
    "import sklearn as sk\n",
    "import seaborn as sns\n",
    "print('import done')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['.ipynb_checkpoints', 'prelim data analysis.ipynb', 'TADPOLE_D1_D2.csv', 'TADPOLE_D1_D2.py', 'TADPOLE_D1_D2_Dict.csv', 'TADPOLE_D2.m', 'TADPOLE_D3.csv', 'TADPOLE_D3.m', 'TADPOLE_readme.txt']\n",
      "<built-in function getcwd>\n"
     ]
    }
   ],
   "source": [
    "print(os.listdir('./'))\n",
    "print(os.getcwd())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py:3058: DtypeWarning: Columns (471,473,474,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,569,570,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,599,601,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,624,625,626,627,628,629,630,631,632,633,634,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,745,746,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,770,771,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,794,795,797,798,799,800,801,802,803,804,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "  interactivity=interactivity, compiler=compiler, result=result)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['011_S_0002' '011_S_0003' '022_S_0004' ... '053_S_5296' '002_S_4264'\n",
      " '036_S_4740'] 1737\n"
     ]
    }
   ],
   "source": [
    "with open('TADPOLE_D1_D2.csv', 'r') as init_data:\n",
    "    raw_data = pd.read_csv(init_data)\n",
    "patients = raw_data['PTID'].unique()\n",
    "print(patients, len(patients))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "raw_data.DXCHANGE.plot(kind = 'hist')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "572\n",
      "89\n"
     ]
    }
   ],
   "source": [
    "changers = raw_data.DXCHANGE > 3\n",
    "print(sum(changers))\n",
    "reverters = raw_data.DXCHANGE > 6\n",
    "print(sum(reverters))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(12741, 1907)\n"
     ]
    }
   ],
   "source": [
    "print(raw_data.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Therefore there are ~480 patients who's condition developed thoughout the testing, with the main group being conversion of MCI to AD (DXCHANGE = 5). This does not preclude predictive models as these cases can be used as test data for the prediction model.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2665  number of nominal constant subjects\n",
      "3924  number of MCI constant subjects\n",
      "1731  number of ad constant subjects\n",
      "12  number of ad constant subjects\n",
      "0  number of ad constant subjects\n"
     ]
    }
   ],
   "source": [
    "print(sum(raw_data.DXCHANGE == 1), ' number of nominal constant subjects')\n",
    "print(sum(raw_data.DXCHANGE == 2), ' number of MCI constant subjects')\n",
    "print(sum(raw_data.DXCHANGE == 3), ' number of ad constant subjects')\n",
    "print(sum(raw_data.DXCHANGE == 8), ' number of ad constant subjects')\n",
    "print(sum(raw_data.DXCHANGE == 9), ' number of ad constant subjects')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now we know what the data distribution of the primary types looks like, how much missing data is there?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(0, 1907) (12741, 1907)\n"
     ]
    }
   ],
   "source": [
    "complete_data = raw_data.dropna()\n",
    "print(complete_data.shape, raw_data.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Thus we can see no entry contains complete information, thus we need to identify which columns we can drop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.series.Series'> (1907,)\n",
      "2\n",
      "PIB\n",
      "PIB_bl\n",
      "['PIB', 'PIB_bl']\n",
      "(12741, 1905) (12741, 1907)\n",
      "(0, 1905)\n"
     ]
    }
   ],
   "source": [
    "counts = raw_data.count()\n",
    "\n",
    "print(type(counts), counts.shape)\n",
    "sub_10 = counts < 1274\n",
    "print(sum(sub_10))\n",
    "p_data = raw_data\n",
    "drop_list = []\n",
    "for cols in p_data.columns:\n",
    "    \n",
    "    if p_data[cols].count() < 1274:\n",
    "        print(cols)\n",
    "        drop_list.append(cols)\n",
    "        \n",
    "print(drop_list)\n",
    "p_data = p_data.drop(columns = drop_list)\n",
    "print(p_data.shape, raw_data.shape)\n",
    "complete_data = p_data.dropna()\n",
    "print(complete_data.shape)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "intended to do PCA however not possible right now due to missing, catagorical and string values code to perform PCA below\n",
    "from sklearn.decomposition import PCA\n",
    "pca = PCA()\n",
    "pca.fit(raw_data)\n",
    "pca_score = pca.explained_variance_ratio_\n",
    "pca_score\n",
    "plt.plot(pca_score)\n",
    "plt.ylabel('explained variance')\n",
    "plt.xlabel('Number of components')\n",
    "plt.xticks(np.arange(1, len(pca_score)+ 1, 5.0))\n",
    "plt.grid(True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "as removal of low population columns does not address missing data problems. lets tackle the data set from the other direction. Identify data features that show distinct populations when ploted by diagnosis. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n",
      "['NL' 'Dementia' 'MCI' 'NL to MCI' 'MCI to Dementia' 'MCI to NL'\n",
      " 'Dementia to MCI' nan 'NL to Dementia']\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "(array([0, 1, 2, 3, 4, 5, 6, 7]), <a list of 8 Text xticklabel objects>)"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#sns.distplot(raw_data.AGE)\n",
    "DX_list = raw_data.DX.unique()\n",
    "print(len(DX_list))\n",
    "print(DX_list)\n",
    "\n",
    "sns.boxplot(y = raw_data.AGE, x = raw_data.DX )\n",
    "plt.xticks(rotation = 60)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.boxplot(y = raw_data.AGE, x = raw_data.DX )"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
