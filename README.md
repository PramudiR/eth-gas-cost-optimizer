# Ethereum Gas Optimization API
The Gas Optimization API is a RESTful API built using the FastAPI Python library and runs on the Uvicorn server. It is specifically designed for Ethereum development teams to optimize gas costs in both development testing and production environments. The API utilizes a neural network model that is trained on the last 8 hours of successful Ethereum transaction data, allowing it to predict the probabilities of gas cost changes within the next hour based on the latest 2 hours of data.

## Features
- Predicts gas cost changes: The API leverages a neural network trained on Ethereum transaction data to predict the probabilities of gas cost changes in the upcoming hour.
- Optimize gas costs: By using the predictions provided by the API, development teams can proactively optimize their gas costs, making their Ethereum transactions more efficient and cost-effective.
- Historical data analysis: The API utilizes the last 8 hours of successful Ethereum transaction data to train the neural network model, enabling it to learn from past trends and patterns.
- Real-time predictions: The API continuously updates its predictions based on the latest 2 hours of data, ensuring that the gas cost predictions remain up-to-date and accurate.

## API Endpoints
### 'GET /probmat'
Retrieves the predicted probabilities of gas cost changes within the next hour.
