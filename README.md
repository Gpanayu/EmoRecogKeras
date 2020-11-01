# CNN Implementation for EEG-Emotion Recognition during Music Listening (arXiv Oct 2019) 
[link](https://arxiv.org/abs/1910.09719)

This repository is a part of EEG-Emotion Recognition Research.  It manifests models used in our experiments.

![](images/modelGeneral.png)

## Models
There are 4 CNN architectures (3Conv - 6Conv).  You can see Keras implementation in /typicalModels.  Also, we have tested 3D physical electrode placement.  In this experiment, we had to adjust the models to fit the new input's size.  You can find these modified models in /3DModels.

## Citation
If you find the code useful for your research, please cite our paper:

```
@article{keelawat2019,
  title={Spatiotemporal Emotion Recognition using Deep CNN Based on EEG during Music Listening},
  author={Panayu Keelawat, Nattapong Thammasan, Masayuki Numao and Boonserm Kijsirikul},
  journal={arXiv preprint arXiv:1910.09719},
  year={2019}
}
```
