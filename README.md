# ANTHRO: Perturbations in the Wild
![Alt text](https://github.com/lethaiq/perturbations-in-the-wild/blob/main/logo.jpg)
Repository of the paper "Perturbations in the Wild: Leveraging Human-Written Text Perturbations for Realistic Adversarial Attack and Defense", ACL22 (Findings) [[pdf]](https://arxiv.org/abs/2203.10346)

**DEMO version of ANTHRO is accepted to ICDE 2023, Demo track. Part of the system is accessible via [link](https://lethaiq.github.io/anthro)**

# Instructions
Please use the ``test.py`` file for instructions.

## Extract Potential Perturbations on External Corpus
```
from anthro_lib import ANTHRO
anthro = ANTHRO()
```
Now, we can extract potential perturbations from a text, and save the results to local disk.
```
texts = ['democrats', 'demokrats', 'democRATs', 'republicans', 'repubLIEcans', 'republiCUNTs']
anthro.process(texts)
anthro.save('./saved')
```
Then, we can use search for perturbations of an input token.
```
print(anthro.get_similars('republicans', level=1, distance=5, strict=False))
>> {'republicans', 'repubLIEcans', 'republiCUNTs'}
```
There are two modes of finding perturbations. One is ``strict``--i.e., ``strict=True`` and one is ``non-strict``--i.e., ``strict=False``. Non-strict mode outputs more perturbations (some of they are pretty creative), but more false positive. We only use ``strict=True`` in all experiments in our paper.

## Load V1.0 ANTHRO Dictionary
We have also provided a big dictionary of 2,083,037 unique cased tokens of a total 407,620 unique sounds found on social media (assumed to be written by human writers). This dictionary can be easily loaded. We encourage other researchers to use this dictionary as ANTHRO's baseline.
```
anthro = ANTHRO()
anthro.load('./ANTHRO_Data_V1.0')

print(anthro.get_similars('presidents', level=1, distance=5, strict=True))
>> {'Presidents', 'PRESIDENTS', 'prsidents', 'PRESIDENTs', 'presidents'}

print(anthro.get_similars('biden', level=1, distance=5, strict=True))
>> {'BiDEN', 'bieden', 'biiden', 'bidennn', 'biyden', 'BIDENNN', 'biDen', 'BIDEENN', 'bidenn', 'bideN', 'Bidn', 'BideN', 'BIDEN', 'bIDen', 'Biddn', 'Biden', 'BIDENN', 'bideeen', 'BIdEn', 'biddden', 'Bideeen', 'biiiden', 'BIDDDEENNN', 'Bidien', 'bidenN', 'Biiiden', 'Bideeennn', 'BIDEEEN', 'BiDen', 'BIDEn', 'BIIIDEEEN', 'bidn', 'bideen', 'BIDEEENNN', 'biden', 'bIdEn', 'BIEDEN', 'BIIIDEN', 'Bidennn', 'BIden', 'Biddeeennn', 'BIIIDENNN', 'BiDeN', 'biddeeen', 'Bieden', 'biddn', 'bIDeN', 'Bideen'}

print(anthro.get_similars('trump', level=1, distance=5, strict=True))
>> {'tRuMp', 'TRMP', 'trUmP', 'truuump', 'TRUMPP', 'Trumpp', 'tRuMP', 'trUmp', 'trrump', 'trumpP', 'Trummmp', 'trumppp', 'TRUMMMPPP', 'TRUUUMP', 'TRuMp', 'Trummp', 'Truuump', 'TRUmp', 'Trmp', 'trump', 'TrUMp', 'trumP', 'TRUMP', 'TrUMP', 'Truuummp', 'TRUMPPP', 'trummp', 'Trump', 'TruMP', 'trUMp', 'tRump', 'TRUUUMMPP', 'tRUmp', 'tRUMp', 'TrUmp', 'tRUMP', 'truump', 'TrumP', 'TrUmP', 'TruMp', 'trumpp', 'trmp', 'Trrump', 'Trumppp', 'TRump', 'tRumP', 'tRUmP'}
```

---

If you use the ``ANTHRO_Data_V1.0`` dictionary as baseline for comparison, please note that results reported in our paper is based on a richer dictionary, which was extracted from a corpus that include some private datasets, and cannot be publicly released.

---
Please cite our paper with the following Bibtex:
```
@article{le2022perturbations,
  title={Perturbations in the Wild: Leveraging Human-Written Text Perturbations for Realistic Adversarial Attack and Defense},
  author={Le, Thai and Lee, Jooyoung and Yen, Kevin and Hu, Yifan and Lee, Dongwon},
  journal={60th Annual Meeting of the Association for Computational Linguistics (ACL)},
  year={2022}
}
```
