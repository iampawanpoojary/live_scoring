# live_scoring

Endpoint:
https://scoreboard-eg-dw2wrcimrq-ew.a.run.app/docs

# Steps:
docker build -t scoreboard-image .

docker run --name scoreboard -p 8080:80 scoreboard-image

NEW_IMAGE="gcr.io/random-client/scoreboard:v1"

gcloud builds submit --tag "${NEW_IMAGE}" . 

gcloud beta run deploy scoreboard-eg \
 --image=${NEW_IMAGE} \
 --region="europe-west1" \
 --platform managed
