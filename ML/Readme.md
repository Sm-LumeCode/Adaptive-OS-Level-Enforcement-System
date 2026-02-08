Step-by-Step Workflow
## Step 1: Collect Activity Metrics

Activity features are collected from the monitoring module (monitor.py)

<b>Feature	Description</b>
app_switches--Number of times the user switched windows during the session
idle_time--Total inactive time (no keyboard/mouse events)
keyboard_events--Count of key presses
mouse_events--Count of mouse actions
session_duration--Time since session start (seconds)
focused_duration--Time user spent on the same window (seconds)

## Step 2: Preprocess Features
The raw features may require preprocessing:
Scaling / Normalization, convert features like app_switches and idle_time to the same scale.

## Step 3: ML Model Prediction
The ML model (LogisticRegression) predicts the mode and confidence: Model predicts probabilities for each mode 
Confidence is the highest probability:

## Step 4: Generate Recommendation

## Step 5: Integration with AdaptiveOS
