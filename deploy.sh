GOOGLE_PROJECT_ID=iberia-project-344914

# Build a container
gcloud builds submit --tag gcr.io/$GOOGLE_PROJECT_ID/iberia-project \
    --project=$GOOGLE_PROJECT_ID

# Run and deploy the container
gcloud run deploy iberia-project \
    --image gcr.io/$GOOGLE_PROJECT_ID/iberia-project \
    --platform managed \
    --port 8080 \
    --region europe-west3 \
    --allow-unauthenticated \
    --project=$GOOGLE_PROJECT_ID