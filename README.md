# Handwritten Line Text Recognition with Tensorflow

# Requirements
1. Tensorflow(Tested on Tensorflow-gpu 1.14.0)
2. autocorrect "pip install autocorrect"
3. OpenCv

#### Preparation of Dataset
* Download IAM dataset to the machine.
* Place lines folder and lines.txt in the data/ directory.
* All set.(Only if you wish to continue with default hyperparameters)



To Train the model from scratch
```markdown
$ cd src/
$ python main.py --train

```
To validate the model
```markdown
$ cd src/
$ python main.py --validate
```
To Get Prediction or to run a Demo
```markdown
$ cd src/
$ python scan.py --image <infer_image_path>
Example - python process.py --image "../data/test.png"
Note - Run "process.py" only if using with a custom image.
$ python main.py --infer <processed_image_path>
Example - python main.py --infer "../data/preprocessed_test.png"
```