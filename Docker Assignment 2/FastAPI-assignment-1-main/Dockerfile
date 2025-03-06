# ---------------------- STAGE 1 ----------------------
FROM python:3.11 AS build

#Initializing working diorectory
WORKDIR /app

# Copying requirement.txt file
COPY requirements.txt .

# Installing dependencies in venv file in thw container
RUN python -m venv /venv && /venv/bin/pip install --no-cache-dir -r requirements.txt

# ------------------------- STAGE 2 --------------------
FROM python:3.11-slim

#Initializing working diorectory
WORKDIR /app

# Copy installed dependencies from build stage
COPY --from=build /venv /venv

# Copying all the files
COPY . .

# path for virtual environment
ENV PATH="/venv/bin:$PATH"

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

