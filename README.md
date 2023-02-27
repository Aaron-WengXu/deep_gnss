[deep_gnss](https://github.com/Stanford-NavLab/deep_gnss), developed by [Stanford-NavLab](https://github.com/Stanford-NavLab), is one of the state-of-the-art data-driven approaches to positioning with Android raw GNSS measurements, based on the set transformer architecture. It serves as the benchmark for evaluating our method, [PrNet](https://github.com/Aaron-WengXu/GNSS-ND).

Slight modifications are made for the evaluation:
* We calculate the predicted positioning results and ground truth locations in the format of latitude, longitude, and height, and write them into files (see deep_gnss/py_scripts/Corrected_Position_set_transformer.csv and deep_gnss/py_scripts/GT_set_transformer.csv). We comment the codes for computing the WLS baseline positioning results.(see codes in deep_gnss/py_scripts/eval_android.py)
* The training data are put under "train/Route1" or "train/Route2".(see codes in deep_gnss/config/train_android_conf.yaml)
* The testing data are put under "var/Route1" or "var/Route2".(see codes in deep_gnss/py_scripts/eval_android.py)
* We add the MATLAB codes to plot the positioning results of [deep_gnss](https://github.com/Stanford-NavLab/deep_gnss) and ground truth.(see codes in deep_gnss/results_plotting)
* The weights trained by us are stored under deep_gnss/weights/Route1 or Route2.

# Original "README" by Stanford-NavLab
Code repository accompanying our work on 'Improving GNSS Positioning using Neural Network-based Corrections'. In this paper, we present a Deep Neural Network (DNN) for position estimation using Global Navigation Satellite System (GNSS) measurements. This work was presented virtually at ION GNSS+ 2021 conference. The presentation can be seen [here](https://youtu.be/_ZeEkEPwtAw) and our slides can be viewed [here](https://stanford.box.com/s/dj2eg3v886u408s234p92r52nok8twst) 

<!--- Badge for paper link---> <a href="https://stanford.box.com/s/vt1pq3nppz0he5i57vux02c1349x23r1"><img src="https://img.shields.io/badge/ION%20GNSS%2B%202021-paper-informational"/></a>
<!--- Badge for slides link---><a href="https://stanford.box.com/s/dj2eg3v886u408s234p92r52nok8twst"><img src="https://img.shields.io/badge/ION%20GNSS%2B%202021-slides-informational"/></a>
<!--- Badge for video link---><a href="https://youtu.be/_ZeEkEPwtAw"><img src="https://img.shields.io/badge/ION%20GNSS%2B%202021-video-red"/></a>

## Installation Instructions
This code was developed in a `conda` environment running on CentOS 7.9.2009 in Sherlock, Stanford University's HPC. 

To create the `conda` environment, use `conda env create -f environment.yml`


## Code Overview
### Directory Structure
```
deep_gnss
|  config
|  data
|  py_scripts
|  src
   |  correction_network
   |  gnss_lib
   |  totalrecall
```
### Description
Our code is divided into two main parts: `src` and `py-scripts`. `src` contains the core functionality that our project is built on while `py-scripts` contains  standalone `python` scripts for generating simulated data and training and evaluating the neural network. `config` contains `.yml` files to set hyper-parameters for the corresponding scripts and can be modified depending on your requirements. `data` contains example data files that our code is designed to work with.

Within `src`, the `correction_network` module defines the PyTorch DataLoaders and Network models; `gnss_lib` contains code that is used to simulate/find expected GNSS measurements; `totalrecall` defines functions and code used to simulate measurements based on a pre-determined 2D NED trajectory.

## Using our code
To run the `train_*.py` scripts, run the command `python train_*.py prefix="name_of_your_experiment_here"`. 

To run the data simulation code, run the command `python data_gen.py`.

Weights for trained networks can be found [here](https://stanford.box.com/s/pai1cqayccwumfa0289388e8y662p772)

## Acknowledgements
The Deep Sets model is taken from the [original implementation](https://github.com/yassersouri/pytorch-deep-sets)

We also used the `EphemerisManager` from Jonathan Mitchell's analysis of the Android Raw GNSS Measurements Dataset ([link to file]((https://github.com/johnsonmitchelld/gnss-analysis/blob/main/gnssutils/ephemeris_manager.py)))

Our coordinate analysis code is based on CommaAI's Laika [repository](https://github.com/commaai/laika)

## Citing this work
If you use this code in your research, please cite our paper
```
@inproceedings{kanhere2021improving,
  title={ Improving GNSS Positioning using Neural Network-based Corrections},
  author={Kanhere, Ashwin Vivek and Gupta, Shubh and Shetty, Akshay and Gao, Grace Xingxin},
  booktitle={32nd International Technical Meeting of the Satellite Division of the Institute of Navigation, ION GNSS+ 2021}
  year={2021}
}
```
## Contact
For any feature requests or bug reports, please submit an issue in this GitHub repository with details or a minimal working example to replicate the bug.

For any comments, suggestions or queries about our work, please contact [Prof. Grace Gao](https://aa.stanford.edu/person/grace-gao) at gracegao [at] stanford [dot] edu
