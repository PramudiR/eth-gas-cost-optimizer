# Ethereum Gas Optimization API
The Gas Optimization API is a RESTful API built using the FastAPI Python library and runs on the Uvicorn server. It is designed explicitly for Ethereum development teams to optimize gas costs in both development testing and production environments. The API utilizes a neural network model trained on the last 8 hours of successful Ethereum transaction data, allowing it to predict the probabilities of gas cost changes within the next hour based on the latest 2 hours of data.

## Features
- Predicts gas cost changes: The API leverages a neural network trained on Ethereum transaction data to predict the probabilities of gas cost changes in the upcoming hour.
- Optimize gas costs: By using the predictions provided by the API, development teams can proactively optimize their gas costs, making their Ethereum transactions more efficient and cost-effective.
- Historical data analysis: The API utilizes the last 8 hours of successful Ethereum transaction data to train the neural network model, enabling it to learn from past trends and patterns.
- Real-time predictions: The API continuously updates its forecasts based on the latest 2 hours of data, ensuring that the gas cost predictions remain up-to-date and accurate.

## API Endpoints
### 'GET /probmat'
Retrieves the predicted probabilities of gas cost changes within the next hour.
#### Response
<pre>
  ```json
  {
    "ranges": [ "<25", "<50", "<75", "<100", "<125", "<150", "<175", "<200", "<225", "<250", "<275", "<300"],
    "15s": [ 
             0.7059469223022461, 0.7943832874298096, 0.7649496793746948, 0.772125244140625, 0.7815682291984558, 0.7788654565811157, 
             0.7804185748100281, 0.7842850685119629, 0.7862213253974915, 0.7855314016342163, 0.7942007780075073, 0.7872123122215271
      ],
    "30s": [ 
             0.8660202026367188, 0.9632910490036011, 0.9631556868553162, 0.9594703316688538, 0.9636200666427612, 0.9579652547836304,
             0.9565680623054504, 0.9568857550621033, 0.9560444951057434, 0.9512422680854797, 0.9523347616195679, 0.9434801340103149
      ],
    "1min": [ 
             0.9624038934707642, 0.995834231376648, 0.9963154196739197, 0.9915763139724731, 0.9973899722099304, 0.9961696267127991,
              0.997003436088562, 0.9989051818847656, 0.9992334246635437, 0.9926904439926147, 0.9981161952018738, 0.9983747005462646
      ],
    "2min": [
             0.9616681933403015, 0.9993180632591248, 0.9977021217346191, 1.0, 1.0, 0.9992309808731079,
             0.9976043701171875, 0.9955127239227295, 0.9983821511268616, 0.996781051158905, 0.9996248483657837, 1.0
      ],
    "3min": [
             0.9624612927436829, 0.9962872862815857, 0.9992655515670776, 0.996114194393158, 0.9946007132530212, 0.9991744160652161,
             0.9962380528450012, 0.9999232888221741, 0.9973703622817993, 1.0, 0.9944555759429932, 1.0
      ],
    "5min": [
             0.9974009990692139, 1.0, 0.9964191913604736, 0.9937971234321594, 0.9973031878471375, 0.9953874945640564, 
             0.9980596303939819, 0.9967615008354187, 0.9972637295722961, 1.0, 0.9979217648506165, 0.9971233606338501
      ],
    "8min": [
             0.9963428378105164, 1.0, 0.996082067489624, 1.0, 1.0, 0.9992426037788391, 
             0.9973426461219788, 0.9998536109924316, 0.9990205764770508, 0.9976338148117065, 0.991619884967804, 0.9932622313499451
      ],
    "15min": [
              0.9978382587432861, 0.9992620944976807, 0.9975241422653198, 0.9969651699066162, 0.997079610824585, 0.9990554451942444,
              0.9964489340782166, 1.0, 1.0, 1.0, 0.9949337840080261, 1.0
      ],
    "25min": [
              0.9906360507011414, 0.9983415603637695, 0.9932413101196289, 0.9928296804428101, 0.9975571632385254, 0.999092698097229,
              0.9952103495597839, 0.9957742094993591, 0.9975624680519104, 0.9916985034942627, 0.995036780834198, 0.9991482496261597
      ],
    "30min": [
              0.9951934814453125, 0.9951688647270203, 1.0, 0.9988037943840027, 1.0, 0.9933684468269348,
              0.9988278150558472, 0.9946069121360779, 0.9968980550765991, 0.9960575699806213, 1.0, 1.0
      ],
    "40min": [
              0.996001660823822, 0.9949744343757629, 0.995665431022644, 0.9986568093299866, 0.9944230914115906, 0.9958171844482422,
              0.9969004988670349, 0.9997028112411499, 0.9996864199638367, 0.9994663596153259, 0.9984647035598755, 0.9956538081169128
      ],
    "50min": [
              0.9959649443626404, 0.9985350966453552, 0.9951665997505188, 0.9965173602104187, 0.9951213598251343, 0.99724942445755,
              0.9991470575332642, 0.9935277700424194, 1.0, 0.9974727034568787, 0.9975534081459045, 0.9965230822563171
      ],
    "55min": [
              0.9922242164611816, 0.9976848363876343, 0.9948474168777466, 0.9941098093986511, 0.9991874694824219, 0.9973484873771667,
              0.9996450543403625, 0.9964390993118286, 0.9973006844520569, 0.9938235282897949, 0.997665286064148, 0.9973194599151611
      ],
    "1hour": [
              0.9975841045379639, 1.0, 0.9962502121925354, 0.9968662858009338, 1.0, 0.9962453842163086,
              0.9927717447280884, 0.9954568147659302, 0.9978814125061035, 0.9974821209907532, 0.9983969330787659,0.9995218515396118
      ]
  }
  ```
</pre>  

### 'POST /train_nn'
Train the underlying neural net of the API using the most recent 8 hours of data.
#### Input
Input is a boolean value. It can be either 1 or 0 and "True" or "False".
<pre>
  ```json
  {
    "train" : 1
  }
  ```
</pre>
#### Response
<pre>
  ```json
  {
    "status": "Neural net retraining completed.",
    "ranges": [ "<25", "<50", "<75", "<100", "<125", "<150", "<175", "<200", "<225", "<250", "<275", "<300"],
    "15s": [ 
             0.7059469223022461, 0.7943832874298096, 0.7649496793746948, 0.772125244140625, 0.7815682291984558, 0.7788654565811157, 
             0.7804185748100281, 0.7842850685119629, 0.7862213253974915, 0.7855314016342163, 0.7942007780075073, 0.7872123122215271
      ],
    "30s": [ 
             0.8660202026367188, 0.9632910490036011, 0.9631556868553162, 0.9594703316688538, 0.9636200666427612, 0.9579652547836304,
             0.9565680623054504, 0.9568857550621033, 0.9560444951057434, 0.9512422680854797, 0.9523347616195679, 0.9434801340103149
      ],
    "1min": [ 
             0.9624038934707642, 0.995834231376648, 0.9963154196739197, 0.9915763139724731, 0.9973899722099304, 0.9961696267127991,
              0.997003436088562, 0.9989051818847656, 0.9992334246635437, 0.9926904439926147, 0.9981161952018738, 0.9983747005462646
      ],
    "2min": [
             0.9616681933403015, 0.9993180632591248, 0.9977021217346191, 1.0, 1.0, 0.9992309808731079,
             0.9976043701171875, 0.9955127239227295, 0.9983821511268616, 0.996781051158905, 0.9996248483657837, 1.0
      ],
    "3min": [
             0.9624612927436829, 0.9962872862815857, 0.9992655515670776, 0.996114194393158, 0.9946007132530212, 0.9991744160652161,
             0.9962380528450012, 0.9999232888221741, 0.9973703622817993, 1.0, 0.9944555759429932, 1.0
      ],
    "5min": [
             0.9974009990692139, 1.0, 0.9964191913604736, 0.9937971234321594, 0.9973031878471375, 0.9953874945640564, 
             0.9980596303939819, 0.9967615008354187, 0.9972637295722961, 1.0, 0.9979217648506165, 0.9971233606338501
      ],
    "8min": [
             0.9963428378105164, 1.0, 0.996082067489624, 1.0, 1.0, 0.9992426037788391, 
             0.9973426461219788, 0.9998536109924316, 0.9990205764770508, 0.9976338148117065, 0.991619884967804, 0.9932622313499451
      ],
    "15min": [
              0.9978382587432861, 0.9992620944976807, 0.9975241422653198, 0.9969651699066162, 0.997079610824585, 0.9990554451942444,
              0.9964489340782166, 1.0, 1.0, 1.0, 0.9949337840080261, 1.0
      ],
    "25min": [
              0.9906360507011414, 0.9983415603637695, 0.9932413101196289, 0.9928296804428101, 0.9975571632385254, 0.999092698097229,
              0.9952103495597839, 0.9957742094993591, 0.9975624680519104, 0.9916985034942627, 0.995036780834198, 0.9991482496261597
      ],
    "30min": [
              0.9951934814453125, 0.9951688647270203, 1.0, 0.9988037943840027, 1.0, 0.9933684468269348,
              0.9988278150558472, 0.9946069121360779, 0.9968980550765991, 0.9960575699806213, 1.0, 1.0
      ],
    "40min": [
              0.996001660823822, 0.9949744343757629, 0.995665431022644, 0.9986568093299866, 0.9944230914115906, 0.9958171844482422,
              0.9969004988670349, 0.9997028112411499, 0.9996864199638367, 0.9994663596153259, 0.9984647035598755, 0.9956538081169128
      ],
    "50min": [
              0.9959649443626404, 0.9985350966453552, 0.9951665997505188, 0.9965173602104187, 0.9951213598251343, 0.99724942445755,
              0.9991470575332642, 0.9935277700424194, 1.0, 0.9974727034568787, 0.9975534081459045, 0.9965230822563171
      ],
    "55min": [
              0.9922242164611816, 0.9976848363876343, 0.9948474168777466, 0.9941098093986511, 0.9991874694824219, 0.9973484873771667,
              0.9996450543403625, 0.9964390993118286, 0.9973006844520569, 0.9938235282897949, 0.997665286064148, 0.9973194599151611
      ],
    "1hour": [
              0.9975841045379639, 1.0, 0.9962502121925354, 0.9968662858009338, 1.0, 0.9962453842163086,
              0.9927717447280884, 0.9954568147659302, 0.9978814125061035, 0.9974821209907532, 0.9983969330787659,0.9995218515396118
      ]
  }
  ```
</pre>
## Installation
To run the Gas Optimization API locally, follow these steps:

1. Clone the repository: git clone https://github.com/dileepaj/eth-gas-cost-optimizer.git
2. Navigate to the project directory: cd gas-optimization-api
3. Install dependencies: pip install -r requirements.txt
4. Start the server: uvicorn main:app --reload
5. The API will now be accessible at http://localhost:8000.

Or else this can be hosted on your own cloud service as well.

## Requirements
To successfully run the Gas Optimization API, make sure you have the following:
- Python 3.7 or higher
- Pip (Python package manager)

## Usage
1. Send a GET request to the '/probmat' to retrieve the probability matrix for the gas cost changes that may occur within the next hour.
2. Analyze the predictions to determine the likelihood of gas cost changes in the upcoming hour.
3. Implement the necessary optimizations in your Ethereum development and testing processes.
4. If the last training of the neural network happened more than 4 hours ago you are recommended to send a POST request to '/train_nn' as explained above and retrain the model using the latest data.

## Important
This API itself does not contain any data collection API or code block, you can collect the data using [Etherscan](https://etherscan.io/login?cmd=last) and [Infura](https://app.infura.io/login) API calls. A sample of successful transaction records in each block should be collected and roughly a new block is created every 15 seconds. Then give the path to the data location to this API.

## Data Privacy and Security
The Gas Optimization API is designed with privacy and security in mind. It adheres to industry best practices to ensure the confidentiality and integrity of the data. The API does not store any personal or sensitive information related to Ethereum transactions.

## Contributions
Contributions to the Gas Optimization API are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request in the GitHub repository.

## License
This project is licensed under the [GNU General Public License (GPL)](https://www.gnu.org/licenses/gpl-3.0.en.html). Feel free to modify and use the codebase according to your requirements.
