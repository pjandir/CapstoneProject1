# Predicting a player's NFL Draft round

## Introduction
This analysis is my first Capstone project in the Springboard Data Science Career Track course. The primary dataset for 
this analysis is NFL Combine (Combine) data. The Combine is an invitation-only showcase for aspiring NFL players. They
perform various physical and mental drills and tasks. The Combine is a part of the total evaluation process by NFL teams 
prior to the seven-round NFL Draft. This completed project uses these Combine results to predict which round a player might be
selected in the NFL Draft.

This repo contains the code, data, documentation and reports for this project. 

## Results

Using a metric of F1 score (in [this case](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html) 
with a weighted average), various models are tested to predict the multi-class output. A stacked ensemble classifier is found
to perform best. It achieves a score of 0.29, improving upon the baseline score of 0.19. 

## Overview

| Step | Description | File(s) |
| --- | --- | --- |
| Proposal | Full project proposal and idea | [report](https://github.com/pjandir/CapstoneProject1/blob/master/Proposal.md) |
| Data wrangling | Data cleaning, wrangling, and munging | [code](https://nbviewer.jupyter.org/github/pjandir/CapstoneProject1/blob/master/data-wrangling.ipynb), [report](https://github.com/pjandir/CapstoneProject1/blob/master/data-wrangling.pdf) |
| Data story | Looking into Quarterback trends | [code](https://nbviewer.jupyter.org/github/pjandir/CapstoneProject1/blob/master/data-story.ipynb) |
| Inferential statistics | Closer statistical look between various distributions | [code](https://nbviewer.jupyter.org/github/pjandir/CapstoneProject1/blob/master/inferential-stats.ipynb), [report](https://github.com/pjandir/CapstoneProject1/blob/master/inferential-stats.pdf) |
| Milestone report | Summary of all steps completed so far | [report](https://github.com/pjandir/CapstoneProject1/blob/master/milestone-report.pdf) |
| Model building | In-depth analysis and machine learning | [code](https://nbviewer.jupyter.org/github/pjandir/CapstoneProject1/blob/master/model-building.ipynb) |
| Final report | Discussion and overview of completed project | [report](https://github.com/pjandir/CapstoneProject1/blob/master/full-report.pdf), [slide deck](https://github.com/pjandir/CapstoneProject1/blob/master/slide-deck.pdf) |
| Bonus Prediction | Predicting 2018 draft with final model | [code](https://nbviewer.jupyter.org/github/pjandir/CapstoneProject1/blob/master/predict-2018.ipynb) |

