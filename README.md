# Prediction of hERG channel blockers with directed message passing neural networks

This model leverages the ChemProp network (D-MPNN) to build a predictor of hERG-mediated cardiotoxicity. The model has been trained using a published dataset which contains 7889 molecules with several cut-offs for hERG blocking activity. The authors select a 10 uM cut-off. This implementation of the model does not use any specific featurizer, though the authors suggest the moe206 descriptors (closed-source) improve performance even further.

This model was incorporated on 2023-12-04.

## Information
### Identifiers
- **Ersilia Identifier:** `eos30f3`
- **Slug:** `dmpnn-herg`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Homo sapiens`
- **Tags:** `Cardiotoxicity`, `hERG`, `Toxicity`, `Descriptor`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of blocking hERG (cut-off: 10uM)

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| herg_inhibition_probability | float | high | Probability score of hERG inhibition |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos30f3](https://hub.docker.com/r/ersiliaos/eos30f3)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos30f3.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos30f3.zip)

### Resource Consumption
- **Model Size (Mb):** `34`
- **Environment Size (Mb):** `5366`


### References
- **Source Code**: [https://github.com/AI-amateur/DMPNN-hERG](https://github.com/AI-amateur/DMPNN-hERG)
- **Publication**: [https://pubs.rsc.org/en/content/articlehtml/2022/ra/d1ra07956e](https://pubs.rsc.org/en/content/articlehtml/2022/ra/d1ra07956e)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2022`
- **Ersilia Contributor:** [leilayesufu](https://github.com/leilayesufu)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [None](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos30f3
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos30f3
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
