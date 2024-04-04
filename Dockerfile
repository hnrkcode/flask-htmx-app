FROM node:21-alpine as build
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM python:3.11-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
COPY ./requirements/prod.txt ./requirements/
RUN pip install --upgrade --no-cache-dir pip && pip install --no-cache-dir -r ./requirements/prod.txt
COPY . .
COPY --from=build /usr/src/app/app/static/dist /usr/src/app/app/static/dist
COPY --from=build /usr/src/app/app/blueprints/home/static/dist /usr/src/app/app/blueprints/home/static/dist
RUN rm -rf /usr/src/app/app/static/js /usr/src/app/app/blueprints/home/static/js
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]