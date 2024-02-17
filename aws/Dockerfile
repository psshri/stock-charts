FROM public.ecr.aws/lambda/python:3.10

# copy the requirements file to the container
COPY requirements.txt .

# install the python dependencies
RUN pip3 install -r requirements.txt

# COPY lambda_function.py ${LAMBDA_TASK_ROOT}/
# COPY info.json ${LAMBDA_TASK_ROOT}/
# COPY src/ ${LAMBDA_TASK_ROOT}/src/
# COPY ohlc-charts/ ${LAMBDA_TASK_ROOT}/ohlc-charts/
COPY . .
# copy the relevant files from src to the container
# COPY src/config/info.json config/
# COPY src/checkLiveScore/checkLiveScore.py ${LAMBDA_TASK_ROOT}/checkLiveScore/
# COPY src/checkSchedule/checkSchedule.py ${LAMBDA_TASK_ROOT}/checkSchedule/
# COPY src/main.py ${LAMBDA_TASK_ROOT}

# specify the command to run your application
CMD ["lambda_function.lambda_handler"]