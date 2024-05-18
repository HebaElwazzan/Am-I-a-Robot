## Am I a Robot?
Submission for OMSCS Hackathon 2024.

A game where the user has to guess whether the generated text is written by humans or not.

### How to run
Since the project is not yet deployed, instructions on how to run it locally are provided below.

First, run the [main](https://github.com/HebaElwazzan/Am-I-a-Robot/blob/main/Backend/main.py) python file. You will have to provide an API key for Gemini in a file called `config.py` under the same directory. Instructions on how to create an API key can be found through [here](https://ai.google.dev/gemini-api/docs/api-key).

After the server is up and running locally, you should launch the angular project. Prereqruisites to running it locally can be found [here](https://angular.dev/tutorials/first-app#identify-the-version-of-nodejs-that-angular-requires). Afterwards, navigate to the Frontend/am-i-a-robot directory and run `ng serve`. It should be up and running on http://localhost:4200/.
