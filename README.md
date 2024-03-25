# Prediction of hERG Channel Blockers with Directed Message Passing Neural Networks

This model leverages the ChemProp network (D-MPNN, see original Stokes et al, Cell, 2020 for more information) to build a predictor of hERG-mediated cardiotoxicity. The model has been trained using a dataset published by Cai et al, J Chem Inf Model, 2019, which contains 7889 molecules with several cut-offs for hERG blocking activity. The authors select a 10 uM cut-off. This implementation of the model does not use any specific featurizer, though the authors suggest the moe206 descriptors (closed-source) improve performance even further.

## Identifiers

* EOS model ID: `eos30f3`
* Slug: `dmpnn-herg`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Score`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Probability of blocking hERG (cut-off: 10uM)

## References

* [Publication](https://pubs.rsc.org/en/content/articlehtml/2022/ra/d1ra07956e)
* [Source Code](https://github.com/AI-amateur/DMPNN-hERG)
* Ersilia contributor: [leilayesufu](https://github.com/leilayesufu)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos30f3)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos30f3.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos30f3) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://pubs.rsc.org/en/content/articlehtml/2022/ra/d1ra07956e) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!