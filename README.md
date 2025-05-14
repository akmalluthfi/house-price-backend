
# House Price Prediction

This is a house price prediction project developed as part of a project-based learning assignment for the Web Service Technology and Machine Learning Ops course.

The goal of this project is to build a simple system that can predict house prices based on input features, integrating both backend modeling and a user-friendly frontend interface.

## 📦 Project Structure
This project is split across three repositories:

- 🔬 **Data Analysis & Modeling** — [house-price-model](https://github.com/romzyalba/house_price_model)  
  Includes exploratory data analysis (EDA), data preprocessing, and machine learning model development.

- 🚀 **Backend API (FastAPI)** — [house-price-backend](https://github.com/akmalluthfi/house-price-backend)  
  Hosts the trained model using FastAPI and exposes REST endpoints for prediction services.

- 🖥️ **Frontend Interface (Vue)** — [house-price-frontend](https://github.com/fawzan745/house-price-frontend)  
  Provides a simple and interactive Vue-based web interface for users to input data and view predictions.

## Authors

- [@akmalluthfi](https://www.github.com/akmalluthfi)
- [@romzyalba](https://www.github.com/romzyalba)
- [@fawzan745](https://www.github.com/fawzan745)


## Tech Stack

**Client:** VueJS, TailwindCSS, DaisyUI

**Server:** FastAPI, SQLModel, Alembic

## Run Locally

Clone the project

```bash
  git clone https://github.com/akmalluthfi/house-price-backend.git
```

Create and activate virtual environment (Using Windows Powershell)

```bash
  python -m venv .venv
  .venv\Scripts\Activate.ps1
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Copy .env-example
Setting database and environment

```bash
  cp .env-example .env
```

Run migrations and seeders

```bash
  alembic upgrade head
  python -m database.seeders.main
```


Start the app

```bash
  fastapi dev app/main.py
```


## Documentation

#### Run the project and see endpoints

```http
  GET /docs
```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`POSTGRES_SERVER`

`POSTGRES_PORT`

`POSTGRES_DB`

`POSTGRES_USER`

`POSTGRES_PASSWORD`

## Related

Here are some related projects

[House Price Prediction](https://github.com/akmalluthfi/house-price-prediction)